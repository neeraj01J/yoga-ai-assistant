
# Extracts yoga preferences from user input using Gemini and LangChain.
#
# Uses a local fallback extractor when Gemini is temporarily unavailable.
#
# Returns experience, available time, and preferred intensity as JSON.


import json
import os
import random
import re
import time

import streamlit as st
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI


# ---------------------------------------------------------
# 1. Load environment variables
# ---------------------------------------------------------

load_dotenv()


# ---------------------------------------------------------
# 2. Get Gemini API key
# ---------------------------------------------------------

def get_gemini_api_key():
    """
    Loads the Gemini API key from:

    1. Streamlit Cloud Secrets
    2. Local .env file

    Supported names:
    - GOOGLE_API_KEY
    - GEMINI_API_KEY
    """

    # Try Streamlit Cloud Secrets first.
    try:

        api_key = st.secrets.get(
            "GOOGLE_API_KEY"
        )

        if api_key:
            return api_key

        api_key = st.secrets.get(
            "GEMINI_API_KEY"
        )

        if api_key:
            return api_key

    except Exception:
        # Streamlit Secrets may not exist locally.
        pass

    # Try GOOGLE_API_KEY from environment.
    api_key = os.getenv(
        "GOOGLE_API_KEY"
    )

    if api_key:
        return api_key

    # Try GEMINI_API_KEY from environment.
    return os.getenv(
        "GEMINI_API_KEY"
    )


# ---------------------------------------------------------
# 3. Load API key
# ---------------------------------------------------------

GOOGLE_API_KEY = get_gemini_api_key()


if not GOOGLE_API_KEY:

    raise ValueError(
        "GOOGLE_API_KEY is missing. "
        "Add it to Streamlit Secrets or your .env file."
    )


# ---------------------------------------------------------
# 4. Gemini model
# ---------------------------------------------------------

model = ChatGoogleGenerativeAI(

    model="gemini-3.1-flash-lite",

    google_api_key=GOOGLE_API_KEY,

    # Short timeout to avoid long waiting.
    timeout=10,

    # Disable automatic retries.
    max_retries=0,

    # Use a non-streaming response.
    disable_streaming=True,

    # Use minimal reasoning for simple JSON extraction.
    thinking_level="minimal"

)


# ---------------------------------------------------------
# 5. Temporary error detection
# ---------------------------------------------------------

def _is_temporary_api_error(error):

    """
    Checks whether the error may be temporary.
    """

    error_message = str(
        error
    ).upper()

    temporary_errors = (

        "503",
        "504",
        "UNAVAILABLE",
        "DEADLINE_EXCEEDED",
        "429",
        "RESOURCE_EXHAUSTED",
        "INTERNAL",
        "SERVICE_UNAVAILABLE"

    )

    return any(

        error_code in error_message
        for error_code in temporary_errors

    )


# ---------------------------------------------------------
# 6. Gemini request handling
# ---------------------------------------------------------

def _invoke_with_retry(prompt, max_attempts=1):

    """
    Invokes Gemini with a limited number of attempts.

    The default is one attempt to avoid long delays.
    The local fallback is used if the request fails.
    """

    for attempt in range(max_attempts):

        try:

            print(
                "Gemini preference extraction attempt "
                f"{attempt + 1}/{max_attempts}"
            )

            start_time = time.perf_counter()

            response = model.invoke(
                prompt
            )

            end_time = time.perf_counter()

            print(
                "Gemini response time: "
                f"{end_time - start_time:.2f} seconds"
            )

            return response

        except Exception as error:

            print(
                "Gemini preference extraction failed:"
            )

            print(
                str(error)
            )

            if _is_temporary_api_error(error):

                print(
                    "Temporary Gemini API error detected."
                )

            else:

                print(
                    "Non-temporary Gemini API error detected."
                )

            # Do not retry by default.
            # The local extractor will be used instead.
            raise


# ---------------------------------------------------------
# 7. Response text processing
# ---------------------------------------------------------

def _get_response_text(response):

    """
    Converts Gemini's response into plain text.
    """

    response_text = response.content

    # Handle list-based response format.
    if isinstance(response_text, list):

        text_parts = []

        for item in response_text:

            if isinstance(item, dict):

                if item.get("type") == "text":

                    text_parts.append(
                        item.get("text", "")
                    )

            elif isinstance(item, str):

                text_parts.append(
                    item
                )

        response_text = "".join(
            text_parts
        )

    if not isinstance(response_text, str):

        response_text = str(
            response_text
        )

    response_text = response_text.strip()

    # Remove Markdown JSON code fences.
    if response_text.startswith(
        "```json"
    ):

        response_text = response_text[7:].strip()

    elif response_text.startswith(
        "```"
    ):

        response_text = response_text[3:].strip()

    if response_text.endswith(
        "```"
    ):

        response_text = response_text[:-3].strip()

    return response_text


# ---------------------------------------------------------
# 8. Local fallback extractor
# ---------------------------------------------------------

def _extract_preferences_locally(user_input):

    """
    Extracts yoga preferences using local Python rules.

    This function does not require Gemini or an internet
    connection.
    """

    text = user_input.lower().strip()

    # ---------------------------------------------
    # Experience detection
    # ---------------------------------------------

    if re.search(

        r"\b(advanced|expert|experienced|pro)\b",
        text

    ):

        experience = "advanced"

    elif re.search(

        r"\b(intermediate|moderate experience)\b",
        text

    ):

        experience = "intermediate"

    elif re.search(

        r"\b(beginner|new to yoga|newbie|basic)\b",
        text

    ):

        experience = "beginner"

    else:

        # Safe default when experience is not mentioned.
        experience = "beginner"


    # ---------------------------------------------
    # Time detection
    # ---------------------------------------------

    time_minutes = None

    # Matches:
    # 60 minutes
    # 30 mins
    # 45 min

    time_match = re.search(

        r"\b(\d{1,3})\s*(?:minutes?|mins?)\b",
        text

    )

    if time_match:

        time_minutes = int(
            time_match.group(1)
        )


    # Matches:
    # 1 hour
    # 1.5 hours
    # 2 hrs

    if time_minutes is None:

        hour_match = re.search(

            r"\b(\d+(?:\.\d+)?)\s*(?:hours?|hrs?)\b",
            text

        )

        if hour_match:

            hours = float(
                hour_match.group(1)
            )

            time_minutes = int(
                hours * 60
            )


    # Default duration when time is not mentioned.
    if time_minutes is None:

        time_minutes = 30


    # Keep duration within a practical range.
    time_minutes = max(

        5,
        min(time_minutes, 180)

    )


    # ---------------------------------------------
    # Intensity detection
    # ---------------------------------------------

    if re.search(

        r"\b(active|intense|intensive|challenging|hard|"
        r"power|energetic|strong)\b",

        text

    ):

        intensity = "active"

    elif re.search(

        r"\b(gentle|relaxing|relaxed|easy|calm|"
        r"slow|restorative|stress relief)\b",

        text

    ):

        intensity = "gentle"

    elif re.search(

        r"\b(balanced|moderate|medium|normal)\b",

        text

    ):

        intensity = "balanced"

    else:

        intensity = "unknown"


    # ---------------------------------------------
    # Create preferences object
    # ---------------------------------------------

    preferences = {

        "experience": experience,
        "time_minutes": time_minutes,
        "intensity": intensity

    }


    print(
        "Local fallback preferences:",
        preferences
    )

    return preferences


# ---------------------------------------------------------
# 9. Validate Gemini preferences
# ---------------------------------------------------------

def _validate_gemini_preferences(preferences):

    """
    Performs basic validation on Gemini's JSON response.

    Returns the cleaned preferences or raises an error
    if the response is not usable.
    """

    if not isinstance(
        preferences,
        dict
    ):

        raise ValueError(
            "Gemini response is not a JSON object."
        )


    experience = preferences.get(
        "experience"
    )

    time_minutes = preferences.get(
        "time_minutes"
    )

    intensity = preferences.get(
        "intensity"
    )


    valid_experiences = {

        "beginner",
        "intermediate",
        "advanced"

    }

    valid_intensities = {

        "gentle",
        "balanced",
        "active",
        "unknown"

    }


    if experience not in valid_experiences:

        raise ValueError(
            "Invalid experience value returned by Gemini."
        )


    if intensity not in valid_intensities:

        raise ValueError(
            "Invalid intensity value returned by Gemini."
        )


    # Convert numeric time to an integer.
    time_minutes = int(
        time_minutes
    )


    # Keep duration within a practical range.
    time_minutes = max(

        5,
        min(time_minutes, 180)

    )


    return {

        "experience": experience,
        "time_minutes": time_minutes,
        "intensity": intensity

    }


# ---------------------------------------------------------
# 10. Main extraction function
# ---------------------------------------------------------

def extract_yoga_preferences(user_input):

    """
    Extracts structured yoga preferences.

    First tries Gemini once.

    If Gemini fails, returns preferences extracted
    using the local Python fallback.
    """

    prompt = f"""

You are a yoga assistant.

Analyze the user's input and extract the following information:

1. experience:
   - beginner
   - intermediate
   - advanced

2. time_minutes:
   - available time in minutes as an integer

3. intensity:
   - gentle
   - balanced
   - active
   - unknown if not mentioned

Return ONLY valid JSON in this exact format:

{{
    "experience": "beginner",
    "time_minutes": 25,
    "intensity": "gentle"
}}

User input:

{user_input}

"""


    # ---------------------------------------------
    # Try Gemini once
    # ---------------------------------------------

    try:

        response = _invoke_with_retry(
            prompt,
            max_attempts=1
        )

        response_text = _get_response_text(
            response
        )

        preferences = json.loads(
            response_text
        )

        preferences = _validate_gemini_preferences(
            preferences
        )

        print(
            "Preferences extracted using Gemini:",
            preferences
        )

        return preferences


    except Exception as error:

        print(
            "Gemini extraction unavailable. "
            "Using local fallback instead."
        )

        print(
            f"Gemini extraction error: {error}"
        )


        # -----------------------------------------
        # Local fallback
        # -----------------------------------------

        return _extract_preferences_locally(
            user_input
        )


# ---------------------------------------------------------
# 11. Local testing
# ---------------------------------------------------------

if __name__ == "__main__":

    user_input = input(
        "Describe your yoga requirements: "
    )

    result = extract_yoga_preferences(
        user_input
    )

    print(
        "\nExtracted Preferences:"
    )

    print(
        json.dumps(
            result,
            indent=4
        )
    )