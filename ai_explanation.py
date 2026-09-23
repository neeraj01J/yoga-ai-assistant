
# Generates a short explanation using Gemini and LangChain.

import time

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI


load_dotenv()


# Create Gemini model.
model = ChatGoogleGenerativeAI(
    model="gemini-3.1-flash-lite",
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