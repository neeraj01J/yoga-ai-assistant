
# Evaluates fuzzy rules for yoga routine selection.

from fuzzy_logic.membership import calculate_time_memberships
from fuzzy_logic.experience import calculate_experience_memberships


def evaluate_beginner_short_rule(time, experience):

    time_memberships = calculate_time_memberships(time)
    experience_memberships = calculate_experience_memberships(experience)

    return min(
        time_memberships["Short"],
        experience_memberships["Beginner"]
    )


def evaluate_beginner_medium_rule(time, experience):

    time_memberships = calculate_time_memberships(time)
    experience_memberships = calculate_experience_memberships(experience)

    return min(
        time_memberships["Medium"],
        experience_memberships["Beginner"]
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

    time = 25
    experience = 4

    short_strength = evaluate_beginner_short_rule(
        time,
        experience
    )

    medium_strength = evaluate_beginner_medium_rule(
        time,
        experience
    )

    gentle_strength = evaluate_intensity_preference_rule(
        experience,
        "gentle",
        "gentle"
    )

    print(f"Short rule strength: {short_strength:.3f}")
    print(f"Medium rule strength: {medium_strength:.3f}")
    print(f"Gentle preference strength: {gentle_strength:.3f}")