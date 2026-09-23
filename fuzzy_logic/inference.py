
# Performs fuzzy inference and defuzzification.

from fuzzy_logic.rules import (
    evaluate_beginner_short_rule,
    evaluate_beginner_medium_rule,
    evaluate_experience_time_rule,
    evaluate_intensity_preference_rule
)

from fuzzy_logic.output import calculate_output_memberships
from fuzzy_logic.membership import calculate_time_memberships
from fuzzy_logic.experience import calculate_experience_memberships
from fuzzy_logic.routine import select_routine


def aggregate_outputs(
    time,
    experience,
    requested_intensity="unknown"
):

    output_universe = [
        i / 10 for i in range(0, 101)
    ]

    aggregated_output = []

    # Beginner time-based rules.
    beginner_short_strength = evaluate_beginner_short_rule(
        time,
        experience
    )

    beginner_medium_strength = evaluate_beginner_medium_rule(
        time,
        experience
    )

    # Experience and time-based rules.
    intermediate_medium_strength = evaluate_experience_time_rule(
        time,
        experience,
        "Intermediate",
        "Medium"
    )

    intermediate_long_strength = evaluate_experience_time_rule(
        time,
        experience,
        "Intermediate",
        "Long"
    )

    advanced_medium_strength = evaluate_experience_time_rule(
        time,
        experience,
        "Advanced",
        "Medium"
    )

    advanced_long_strength = evaluate_experience_time_rule(
        time,
        experience,
        "Advanced",
        "Long"
    )

    # Intensity preference rules.
    gentle_preference = evaluate_intensity_preference_rule(
        experience,
        requested_intensity,
        "gentle"
    )

    balanced_preference = evaluate_intensity_preference_rule(
        experience,
        requested_intensity,
        "balanced"
    )

    active_preference = evaluate_intensity_preference_rule(
        experience,
        requested_intensity,
        "active"
    )

    # Combine rule strengths.
    gentle_strength = max(
        beginner_short_strength,
        beginner_medium_strength,
        gentle_preference
    )

    balanced_strength = max(
        intermediate_medium_strength,
        balanced_preference
    )

    active_strength = max(
        intermediate_long_strength,
        advanced_medium_strength,
        advanced_long_strength,
        active_preference
    )

    for intensity in output_universe:

        output_memberships = calculate_output_memberships(
            intensity
        )

        gentle_value = min(
            gentle_strength,
            output_memberships["Gentle"]
        )

        balanced_value = min(
            balanced_strength,
            output_memberships["Balanced"]
        )

        active_value = min(
            active_strength,
            output_memberships["Active"]
        )

        aggregated_value = max(
            gentle_value,
            balanced_value,
            active_value
        )

        aggregated_output.append(
            (intensity, aggregated_value)
        )

    return aggregated_output


def defuzzify(aggregated_output):

    numerator = sum(
        intensity * membership
        for intensity, membership in aggregated_output
    )

    denominator = sum(
        membership
        for _, membership in aggregated_output
    )

    if denominator == 0:

        return 0.0

    return numerator / denominator


def get_fuzzy_reasoning(
    time,
    experience,
    requested_intensity="unknown"
):
    """
    Returns membership values and rule strengths
    used by the fuzzy inference system.
    """

    time_memberships = calculate_time_memberships(
        time
    )

    experience_memberships = calculate_experience_memberships(
        experience
    )

    # Beginner time-based rules.
    beginner_short_strength = evaluate_beginner_short_rule(
        time,
        experience
    )

    beginner_medium_strength = evaluate_beginner_medium_rule(
        time,
        experience
    )

    # Experience and time-based rules.
    intermediate_medium_strength = evaluate_experience_time_rule(
        time,
        experience,
        "Intermediate",
        "Medium"
    )

    intermediate_long_strength = evaluate_experience_time_rule(
        time,
        experience,
        "Intermediate",
        "Long"
    )

    advanced_medium_strength = evaluate_experience_time_rule(
        time,
        experience,
        "Advanced",
        "Medium"
    )

    advanced_long_strength = evaluate_experience_time_rule(
        time,
        experience,
        "Advanced",
        "Long"
    )

    # Intensity preference rules.
    gentle_preference = evaluate_intensity_preference_rule(
        experience,
        requested_intensity,
        "gentle"
    )

    balanced_preference = evaluate_intensity_preference_rule(
        experience,
        requested_intensity,
        "balanced"
    )

    active_preference = evaluate_intensity_preference_rule(
        experience,
        requested_intensity,
        "active"
    )

    return {
        "time_memberships": time_memberships,

        "experience_memberships": experience_memberships,

        "rule_strengths": {

            "Beginner + Short Time": round(
                beginner_short_strength,
                3
            ),

            "Beginner + Medium Time": round(
                beginner_medium_strength,
                3
            ),

            "Intermediate + Medium Time": round(
                intermediate_medium_strength,
                3
            ),

            "Intermediate + Long Time": round(
                intermediate_long_strength,
                3
            ),

            "Advanced + Medium Time": round(
                advanced_medium_strength,
                3
            ),

            "Advanced + Long Time": round(
                advanced_long_strength,
                3
            ),

            "Gentle Preference": round(
                gentle_preference,
                3
            ),

            "Balanced Preference": round(
                balanced_preference,
                3
            ),

            "Active Preference": round(
                active_preference,
                3
            )
        }
    }


# Test fuzzy inference and reasoning.

if __name__ == "__main__":

    time = 45
    experience = 5
    requested_intensity = "active"

    aggregated_output = aggregate_outputs(
        time,
        experience,
        requested_intensity
    )

    intensity = defuzzify(
        aggregated_output
    )

    routine = select_routine(
        intensity,
        requested_intensity
    )

    fuzzy_reasoning = get_fuzzy_reasoning(
        time,
        experience,
        requested_intensity
    )

    print(
        f"Defuzzified intensity: {intensity:.3f}"
    )

    print(
        f"Selected routine: {routine['name']}"
    )

    print("\nTime Memberships:")

    for name, value in fuzzy_reasoning[
        "time_memberships"
    ].items():

        print(f"{name}: {value:.3f}")

    print("\nExperience Memberships:")

    for name, value in fuzzy_reasoning[
        "experience_memberships"
    ].items():

        print(f"{name}: {value:.3f}")

    print("\nRule Strengths:")

    for name, value in fuzzy_reasoning[
        "rule_strengths"
    ].items():

        print(f"{name}: {value:.3f}")