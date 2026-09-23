
# Extracts yoga preferences from user input using Gemini and LangChain.
# Returns experience, available time, and preferred intensity as JSON.

import json
import random
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


def _invoke_with_retry(prompt, max_attempts=3):
    """
    Invoke Gemini with retry handling for temporary API errors.
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

            # Immediately stop retrying non-temporary errors.
            if not _is_temporary_api_error(error):

                raise

            # Raise the original error after the final attempt.
            if attempt == max_attempts - 1:

                print(
                    "Gemini preference extraction failed "
                    "after all retry attempts."
                )

                raise

            # Exponential backoff with random variation.
            delay = (2 ** attempt) + random.uniform(0, 1)

            print(
                f"Retrying Gemini request in "
                f"{delay:.2f} seconds..."
            )

            time.sleep(delay)


def extract_yoga_preferences(user_input):
    """
    Extract structured yoga preferences from natural-language input.
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

    # Invoke Gemini with retry handling.
    response = _invoke_with_retry(prompt)

    response_text = response.content

    # Handle Gemini's possible list-based response format.
    if isinstance(response_text, list):

        response_text = "".join(
            item.get("text", "")
            for item in response_text
            if isinstance(item, dict)
            and item.get("type") == "text"
        )

    # Ensure the response is a string.
    if not isinstance(response_text, str):

        response_text = str(response_text)

    # Remove Markdown JSON code fences if present.
    response_text = response_text.strip()

    if response_text.startswith("```json"):

        response_text = response_text[7:]

    elif response_text.startswith("```"):

        response_text = response_text[3:]

    if response_text.endswith("```"):

        response_text = response_text[:-3]

    # Convert JSON text into a Python dictionary.
    preferences = json.loads(
        response_text.strip()
    )

    return preferences


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