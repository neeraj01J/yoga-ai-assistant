
# Connects AI extraction, validation, and fuzzy inference.

from ai_extractor import extract_yoga_preferences
from validator import validate_preferences
from fuzzy_logic.inference import aggregate_outputs, defuzzify
from fuzzy_logic.routine import select_routine


def process_yoga_request(user_input):

    # Extract preferences using Gemini
    extracted_preferences = extract_yoga_preferences(
        user_input
    )

    # Validate and clean the extracted data
    preferences = validate_preferences(
        extracted_preferences
    )

    # Get time, experience, and intensity
    time_minutes = preferences["time_minutes"]
    experience = preferences["experience"]
    requested_intensity = preferences["intensity"]

    # Convert experience level into a numerical value
    experience_values = {
        "beginner": 2,
        "intermediate": 5,
        "advanced": 8
    }

    experience_value = experience_values[experience]

    # Apply fuzzy inference
    aggregated_output = aggregate_outputs(
        time_minutes,
        experience_value,
        requested_intensity
    )

    # Calculate final intensity using centroid defuzzification
    intensity = defuzzify(
        aggregated_output
    )

    # Select the appropriate yoga routine
    routine = select_routine(
        intensity,
        requested_intensity
    )

    # Return the complete result
    return {
        "preferences": preferences,
        "intensity": round(intensity, 3),
        "routine": routine
    }


if __name__ == "__main__":

    # Test the complete workflow
    user_input = input(
        "Describe your yoga requirements: "
    )

    result = process_yoga_request(
        user_input
    )

    print("\nFinal Result:")
    print(result)