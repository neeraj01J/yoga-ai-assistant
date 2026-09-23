
# Evaluates fuzzy rules for yoga routine selection.

from fuzzy_logic.membership import calculate_time_memberships
from fuzzy_logic.experience import calculate_experience_memberships


def evaluate_beginner_short_rule(time, experience):

    return evaluate_experience_time_rule(
        time,
        experience,
        "Beginner",
        "Short"
    )


def evaluate_beginner_medium_rule(time, experience):

    return evaluate_experience_time_rule(
        time,
        experience,
        "Beginner",
        "Medium"
    )


def evaluate_experience_time_rule(
    time,
    experience,
    experience_level,
    time_level
):

    time_memberships = calculate_time_memberships(
        time
    )

    experience_memberships = calculate_experience_memberships(
        experience
    )

    return min(
        time_memberships[time_level],
        experience_memberships[experience_level]
    )


def evaluate_intensity_preference_rule(
    experience,
    requested_intensity,
    target_intensity
):

    experience_memberships = calculate_experience_memberships(
        experience
    )

    experience_strength = max(
        experience_memberships["Beginner"],
        experience_memberships["Intermediate"],
        experience_memberships["Advanced"]
    )

    if requested_intensity == target_intensity:

        return min(experience_strength, 0.6)

    return 0.0


if __name__ == "__main__":

    time = 45
    experience = 5

    intermediate_long_strength = evaluate_experience_time_rule(
        time,
        experience,
        "Intermediate",
        "Long"
    )

    active_strength = evaluate_intensity_preference_rule(
        experience,
        "active",
        "active"
    )

    print(
        "Intermediate + Long Time:",
        f"{intermediate_long_strength:.3f}"
    )

    print(
        "Active Preference:",
        f"{active_strength:.3f}"
    )