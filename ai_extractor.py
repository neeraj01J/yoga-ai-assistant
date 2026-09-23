
# Extracts yoga preferences from user input using Gemini and LangChain.
# Returns experience, available time, and preferred intensity as JSON.

import json
import time

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI


load_dotenv()


# Create Gemini model.
model = ChatGoogleGenerativeAI(
    model="gemini-3.1-flash-lite",
    timeout=20,
    max_retries=0,
    disable_streaming=True,
    thinking_level="minimal"
)


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

    # Measure Gemini response time.
    start_time = time.perf_counter()

    response = model.invoke(prompt)

    end_time = time.perf_counter()

    print(
        f"Gemini response time: "
        f"{end_time - start_time:.2f} seconds"
    )

    response_text = response.content

    # Handle Gemini's possible list-based response format.
    if isinstance(response_text, list):

        response_text = "".join(
            item.get("text", "")
            for item in response_text
            if isinstance(item, dict)
            and item.get("type") == "text"
        )

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