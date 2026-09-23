
# Generates a short explanation using Gemini and LangChain.

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

    response = model.invoke(prompt)

    response_text = response.content

    if isinstance(response_text, list):

        response_text = "".join(
            item.get("text", "")
            for item in response_text
            if isinstance(item, dict)
            and item.get("type") == "text"
        )

    return response_text.strip()


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