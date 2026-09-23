
# Generates a short explanation using Gemini and LangChain.

import os
import time
from pathlib import Path

import streamlit as st
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI


# Load the .env file from the project directory.
env_path = Path(__file__).resolve().parent / ".env"

load_dotenv(dotenv_path=env_path, override=True)


# Get API key from Streamlit Cloud Secrets or local .env.
def get_gemini_api_key():
    """
    Loads the Gemini API key from Streamlit Secrets
    or the local .env file.

    Supports both:
    - GOOGLE_API_KEY
    - GEMINI_API_KEY
    """

    # Try Streamlit Cloud Secrets first.
    try:
        api_key = st.secrets.get("GOOGLE_API_KEY")

        if api_key:
            return api_key

        # Support the alternative secret name.
        api_key = st.secrets.get("GEMINI_API_KEY")

        if api_key:
            return api_key

    except Exception:
        # Streamlit Secrets may not exist locally.
        pass

    # Read from the local .env file.
    # GOOGLE_API_KEY is your current variable name.
    api_key = os.getenv("GOOGLE_API_KEY")

    if api_key:
        return api_key

    # Fallback for GEMINI_API_KEY.
    return os.getenv("GEMINI_API_KEY")


GOOGLE_API_KEY = get_gemini_api_key()


if not GOOGLE_API_KEY:
    raise ValueError(
        "GOOGLE_API_KEY is missing. "
        "Add it to Streamlit Secrets or your .env file."
    )


# Create Gemini model.
model = ChatGoogleGenerativeAI(
    model="gemini-3.1-flash-lite",
    google_api_key=GOOGLE_API_KEY,
    timeout=60,
    max_retries=0,
    disable_streaming=True,
    thinking_level="minimal"
)


def _is_temporary_api_error(error):
    """
    Checks whether the error may be temporary
    and worth retrying.
    """

    error_text = str(error).upper()

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


def _invoke_with_retry(prompt, max_attempts=3):
    """
    Invokes Gemini with retry support for
    temporary API errors.
    """

    for attempt in range(max_attempts):

        try:
            response = model.invoke(prompt)

            response_text = response.content

            # Handle structured response content.
            if isinstance(response_text, list):

                response_text = "".join(
                    item.get("text", "")
                    for item in response_text
                    if isinstance(item, dict)
                    and item.get("type") == "text"
                )

            return response_text.strip()

        except Exception as error:

            print(
                f"Gemini API attempt "
                f"{attempt + 1}/{max_attempts} failed: {error}"
            )

            # Do not retry permanent or unrelated errors.
            if not _is_temporary_api_error(error):
                raise

            # Return a friendly fallback after the final attempt.
            if attempt == max_attempts - 1:

                return (
                    "Your yoga routine was selected successfully, "
                    "but the detailed AI explanation is temporarily "
                    "unavailable. Please try again in a moment."
                )

            # Exponential backoff: 2 seconds, then 4 seconds.
            wait_time = 2 ** (attempt + 1)

            print(
                f"Retrying Gemini request in "
                f"{wait_time} seconds..."
            )

            time.sleep(wait_time)


def generate_routine_explanation(
    preferences,
    routine,
    intensity,
    fuzzy_reasoning
):
    """
    Generates an explanation for the selected yoga routine.
    """

    prompt = f"""
You are a yoga assistant for a college project.

Explain briefly why this yoga routine was selected.

User preferences:
{preferences}

Selected routine:
{routine["name"]}

Fuzzy intensity score:
{intensity}

Fuzzy reasoning:
{fuzzy_reasoning}

Write a simple explanation in 3 to 4 sentences.
Do not use markdown headings.
Do not make medical claims.
Do not invent information about the user.
"""

    return _invoke_with_retry(prompt)


# Test AI explanation.

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

    explanation = generate_routine_explanation(
        sample_preferences,
        sample_routine,
        3.675,
        sample_reasoning
    )

    print("\nAI Explanation:")
    print(explanation)