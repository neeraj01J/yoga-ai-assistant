
# Performs fuzzy inference and defuzzification.

from fuzzy_logic.rules import (
    evaluate_beginner_short_rule,
    evaluate_beginner_medium_rule,
    evaluate_intensity_preference_rule
)

from fuzzy_logic.output import calculate_output_memberships
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

    short_strength = evaluate_beginner_short_rule(
        time,
        experience
    )

    medium_strength = evaluate_beginner_medium_rule(
        time,
        experience
    )

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

    for intensity in output_universe:

        output_memberships = calculate_output_memberships(
            intensity
        )

        gentle_strength = max(
            short_strength,
            gentle_preference
        )

        balanced_strength = max(
            medium_strength,
            balanced_preference
        )

        active_strength = active_preference

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


if __name__ == "__main__":

    time = 25
    experience = 4
    requested_intensity = "gentle"

    aggregated_output = aggregate_outputs(
        time,
        experience,
        requested_intensity
    )

    intensity = defuzzify(
        aggregated_output
    )

    routine = select_routine(
        intensity
    )

    print(f"Defuzzified intensity: {intensity:.3f}")
    print(f"Selected routine: {routine['name']}")