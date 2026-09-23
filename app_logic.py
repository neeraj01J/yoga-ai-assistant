
# Connects AI extraction, validation, fuzzy inference,
# routine selection, and optional explanation.

from ai_extractor import extract_yoga_preferences
from validator import validate_preferences

from fuzzy_logic.inference import (
    aggregate_outputs,
    defuzzify,
    get_fuzzy_reasoning
)

from fuzzy_logic.routine import select_routine


def process_yoga_request(
    user_input,
    generate_explanation=False
):
    """
    Processes the user's yoga request.

    By default, the routine is selected without waiting
    for the optional Gemini explanation.
    """

    # 1. Extract preferences
    extracted_preferences = extract_yoga_preferences(
        user_input
    )

    # 2. Validate and clean preferences
    preferences = validate_preferences(
        extracted_preferences
    )

    # 3. Read validated preferences
    time_minutes = preferences["time_minutes"]
    experience = preferences["experience"]
    requested_intensity = preferences["intensity"]

    # 4. Convert experience to numerical value
    experience_values = {
        "beginner": 2,
        "intermediate": 5,
        "advanced": 8
    }

    experience_value = experience_values[experience]

    # 5. Apply fuzzy inference
    aggregated_output = aggregate_outputs(
        time_minutes,
        experience_value,
        requested_intensity
    )

    # 6. Defuzzify the aggregated output
    intensity = defuzzify(
        aggregated_output
    )

    intensity = round(intensity, 3)

    # 7. Select a suitable yoga routine
    routine = select_routine(
        intensity,
        requested_intensity,
        time_minutes
    )

    # 8. Get fuzzy reasoning
    fuzzy_reasoning = get_fuzzy_reasoning(
        time_minutes,
        experience_value,
        requested_intensity
    )

    # 9. Prepare the result without blocking
    # on the optional Gemini explanation.
    result = {
        "preferences": preferences,
        "intensity": intensity,
        "routine": routine,
        "fuzzy_reasoning": fuzzy_reasoning,
        "explanation": None
    }

    # 10. Generate explanation only when requested
    if generate_explanation:
        from ai_explanation import (
            generate_routine_explanation
        )

        result["explanation"] = (
            generate_routine_explanation(
                preferences,
                routine,
                intensity,
                fuzzy_reasoning
            )
        )

    return result


if __name__ == "__main__":

    user_input = input(
        "Describe your yoga requirements: "
    )

    result = process_yoga_request(
        user_input,
        generate_explanation=False
    )

    print("\nFinal Result:")
    print(result)