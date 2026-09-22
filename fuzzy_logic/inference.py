
from rules import (
    evaluate_beginner_short_rule,
    evaluate_beginner_medium_rule
)

from output import calculate_output_memberships

from routine import select_routine


def aggregate_outputs(time, experience):
    """
    Perform Mamdani output clipping
    and aggregation for two rules.
    """

    # Step 1: Evaluate fuzzy rules

    gentle_strength = evaluate_beginner_short_rule(
        time,
        experience
    )

    balanced_strength = evaluate_beginner_medium_rule(
        time,
        experience
    )

    # Step 2: Create an output universe

    output_universe = [
        i / 10 for i in range(0, 101)
    ]

    aggregated_output = []

    # Step 3: Clip and aggregate output functions

    for intensity in output_universe:

        memberships = calculate_output_memberships(
            intensity
        )

        gentle_value = min(
            gentle_strength,
            memberships["Gentle"]
        )

        balanced_value = min(
            balanced_strength,
            memberships["Balanced"]
        )

        active_value = 0.0

        combined_value = max(
            gentle_value,
            balanced_value,
            active_value
        )

        aggregated_output.append(
            (intensity, combined_value)
        )

    return aggregated_output


def defuzzify(aggregated_output):
    """
    Convert aggregated fuzzy output
    into one numerical intensity using
    the centroid method.
    """

    numerator = 0.0
    denominator = 0.0

    for intensity, degree in aggregated_output:

        numerator += intensity * degree

        denominator += degree

    if denominator == 0:

        raise ValueError(
            "Cannot defuzzify: total membership is zero."
        )

    crisp_output = numerator / denominator

    return crisp_output


# =====================================
# RUN COMPLETE INFERENCE SYSTEM
# =====================================

if __name__ == "__main__":

    # User inputs

    time = 25
    experience = 4

    # Step 1: Mamdani aggregation

    result = aggregate_outputs(
        time,
        experience
    )

    print("\nMAMDANI AGGREGATION")
    print("-" * 40)

    print("Available time:", time)
    print("Experience:", experience)

    print("\nSample aggregated values:")

    for intensity, degree in result[::10]:

        print(
            f"Intensity: {intensity:.1f}, "
            f"Membership: {degree:.3f}"
        )

    # Step 2: Defuzzification

    final_intensity = defuzzify(result)

    print("\nDEFUZZIFICATION")
    print("-" * 40)

    print(
        "Final defuzzified intensity:",
        round(final_intensity, 3)
    )

    # Step 3: Select yoga routine

    selected_routine = select_routine(
        final_intensity
    )

    print("\nSELECTED YOGA ROUTINE")
    print("-" * 40)

    print(
        "Routine:",
        selected_routine["name"]
    )

    print(
        "Description:",
        selected_routine["description"]
    )

    print("\nRecommended Poses:")

    for pose in selected_routine["poses"]:

        print("-", pose)