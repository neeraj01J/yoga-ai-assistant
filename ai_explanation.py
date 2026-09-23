
# Generates a short explanation using Gemini and LangChain.
#
# This module is optional.
# The yoga routine should be selected even if Gemini
# explanation generation fails or becomes unavailable.


import os
from pathlib import Path

import streamlit as st
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI


# ---------------------------------------------------------
# 1. Load environment variables
# ---------------------------------------------------------

# Load the .env file from the project directory.
env_path = Path(__file__).resolve().parent / ".env"

load_dotenv(
    dotenv_path=env_path,
    override=True
)


# ---------------------------------------------------------
# 2. Get Gemini API key
# ---------------------------------------------------------

def get_gemini_api_key():
    """
    Loads the Gemini API key from:

    1. Streamlit Cloud Secrets
    2. Local .env file

    Supported variable names:

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

        # Support alternative secret name.
        api_key = st.secrets.get(
            "GEMINI_API_KEY"
        )

        if api_key:
            return api_key

    except Exception:
        # Streamlit Secrets may not exist locally.
        pass

    # Try GOOGLE_API_KEY from .env.
    api_key = os.getenv(
        "GOOGLE_API_KEY"
    )

    if api_key:
        return api_key

    # Try GEMINI_API_KEY from .env.
    api_key = os.getenv(
        "GEMINI_API_KEY"
    )

    return api_key


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
# 4. Create Gemini model
# ---------------------------------------------------------

model = ChatGoogleGenerativeAI(

    model="gemini-3.1-flash-lite",

    google_api_key=GOOGLE_API_KEY,

    # Short timeout to avoid long waiting.
    timeout=12,

    # Disable LangChain's automatic retries.
    max_retries=0,

    # Use non-streaming response.
    disable_streaming=True,

    # Reduce unnecessary reasoning for a short explanation.
    thinking_level="minimal"

)


# ---------------------------------------------------------
# 5. Fallback explanation
# ---------------------------------------------------------

def get_fallback_explanation():

    """
    Returns a fallback message when Gemini is
    unavailable or the request fails.
    """

    return (
        "Your yoga routine was selected successfully "
        "based on your preferences, available time, "
        "and requested intensity. "
        "The detailed AI explanation is temporarily "
        "unavailable. Please try again later."
    )


# ---------------------------------------------------------
# 6. Convert Gemini response into text
# ---------------------------------------------------------

def _get_response_text(response):

    """
    Converts the Gemini response into a plain string.

    Gemini may return text directly or structured
    content as a list.
    """

    response_text = response.content

    # Handle structured response content.
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

        response_text = "".join(
            text_parts
        )

    # Ensure the response is a string.
    if not isinstance(response_text, str):

        response_text = str(
            response_text
        )

    return response_text.strip()


# ---------------------------------------------------------
# 7. Check temporary API errors
# ---------------------------------------------------------

def _is_temporary_api_error(error):

    """
    Checks whether an error is related to a temporary
    Gemini API problem.

    This function is retained for logging and
    error classification.
    """

    error_text = str(
        error
    ).upper()

    temporary_errors = (

        "503",
        "504",
        "UNAVAILABLE",
        "DEADLINE_EXCEEDED",
        "RESOURCE_EXHAUSTED",
        "429"

    )

    return any(

        error_code in error_text
        for error_code in temporary_errors

    )


# ---------------------------------------------------------
# 8. Invoke Gemini once
# ---------------------------------------------------------

def _invoke_with_retry(prompt, max_attempts=1):

    """
    Sends a prompt to Gemini.

    Only one attempt is used by default to prevent
    repeated delays when Gemini is unavailable.

    The function always returns a user-friendly
    fallback instead of stopping the entire application.
    """

    for attempt in range(max_attempts):

        try:

            print(
                "Gemini explanation attempt "
                f"{attempt + 1}/{max_attempts}"
            )

            response = model.invoke(
                prompt
            )

            response_text = _get_response_text(
                response
            )

            # Check for an empty response.
            if not response_text:

                print(
                    "Gemini returned an empty response."
                )

                return get_fallback_explanation()

            return response_text

        except Exception as error:

            print(
                "Gemini explanation request failed:"
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
            return get_fallback_explanation()

    # Safety fallback.
    return get_fallback_explanation()


# ---------------------------------------------------------
# 9. Generate routine explanation
# ---------------------------------------------------------

def generate_routine_explanation(

    preferences,
    routine,
    intensity,
    fuzzy_reasoning

):

    """
    Generates a short explanation for the selected
    yoga routine.

    This function does not affect routine selection.
    If Gemini fails, a fallback message is returned.
    """

    # Safely read the routine name.
    routine_name = routine.get(
        "name",
        "Selected Yoga Routine"
    )

    prompt = f"""

You are a yoga assistant for a college project.

Explain briefly why this yoga routine was selected.

User preferences:
{preferences}

Selected routine:
{routine_name}

Fuzzy intensity score:
{intensity}

Fuzzy reasoning:
{fuzzy_reasoning}

Instructions:

- Write a simple explanation in 3 to 4 sentences.
- Do not use markdown headings.
- Do not make medical claims.
- Do not invent information about the user.
- Explain how the routine relates to the user's preferences.
- Use clear and beginner-friendly language.

"""

    return _invoke_with_retry(
        prompt,
        max_attempts=1
    )


# ---------------------------------------------------------
# 10. Test AI explanation
# ---------------------------------------------------------

if __name__ == "__main__":

    sample_preferences = {

        "experience": "beginner",
        "time_minutes": 25,
        "intensity": "gentle"

    }

    sample_routine = {

        "name": "Gentle Yoga"

    }

    sample_reasoning = {

        "Gentle Preference": 0.600,
        "Beginner + Short Time": 0.333,
        "Beginner + Medium Time": 0.667

    }

    print(
        "\nGenerating AI explanation..."
    )

    explanation = generate_routine_explanation(

        sample_preferences,
        sample_routine,
        3.675,
        sample_reasoning

    )

    print(
        "\nAI Explanation:"
    )

    print(
        explanation
    )