
# Extracts yoga preferences from user input using Gemini and LangChain.
# Uses a local fallback extractor when Gemini is temporarily unavailable.
# Returns experience, available time, and preferred intensity as JSON.

import json
import random
import re
import time

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI


load_dotenv()


# ---------------------------------------------------------
# Gemini model
# ---------------------------------------------------------

model = ChatGoogleGenerativeAI(
    model="gemini-3.1-flash-lite",
    timeout=60,
    max_retries=0,
    disable_streaming=True,
    thinking_level="minimal"
)


# ---------------------------------------------------------
# Temporary error detection
# ---------------------------------------------------------

def _is_temporary_api_error(error):
    """
    Check whether the error is temporary and worth retrying.
    """

    error_message = str(error).upper()

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
# Gemini retry handling
# ---------------------------------------------------------

def _invoke_with_retry(prompt, max_attempts=3):
    """
    Invoke Gemini with retry handling.
    """

    for attempt in range(max_attempts):

        try:

            print(
                f"Gemini preference extraction attempt "
                f"{attempt + 1}/{max_attempts}"
            )

            start_time = time.perf_counter()

            response = model.invoke(prompt)

            end_time = time.perf_counter()

            print(
                f"Gemini response time: "
                f"{end_time - start_time:.2f} seconds"
            )

            return response

        except Exception as error:

            print(
                f"Gemini preference extraction failed: "
                f"{error}"
            )

            if not _is_temporary_api_error(error):
                raise

            if attempt == max_attempts - 1:
                raise

            delay = (2 ** attempt) + random.uniform(0, 1)

            print(
                f"Retrying Gemini request in "
                f"{delay:.2f} seconds..."
            )

            time.sleep(delay)


# ---------------------------------------------------------
# Response text processing
# ---------------------------------------------------------

def _get_response_text(response):
    """
    Convert Gemini's response into plain text.
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

                text_parts.append(item)

        response_text = "".join(text_parts)

    if not isinstance(response_text, str):

        response_text = str(response_text)

    response_text = response_text.strip()

    # Remove Markdown JSON code fences.
    if response_text.startswith("```json"):

        response_text = response_text[7:]

    elif response_text.startswith("```"):

        response_text = response_text[3:]

    if response_text.endswith("```"):

        response_text = response_text[:-3]

    return response_text.strip()


# ---------------------------------------------------------
# Local fallback extractor
# ---------------------------------------------------------

def _extract_preferences_locally(user_input):
    """
    Extract yoga preferences using local Python rules.

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
# Main extraction function
# ---------------------------------------------------------

def extract_yoga_preferences(user_input):
    """
    Extract structured yoga preferences.

    First tries Gemini with retries.
    If Gemini fails, uses local extraction.
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
    # Try Gemini first
    # ---------------------------------------------

    try:

        response = _invoke_with_retry(prompt)

        response_text = _get_response_text(
            response
        )

        preferences = json.loads(
            response_text
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
# Local testing
# ---------------------------------------------------------

if __name__ == "__main__":

    user_input = input(
        "Describe your yoga requirements: "
    )

    result = extract_yoga_preferences(
        user_input
    )

    print("\nExtracted Preferences:")

    print(
        json.dumps(
            result,
            indent=4
        )
    )