
from membership import calculate_time_memberships
from experience import calculate_experience_memberships


def evaluate_beginner_short_rule(time, experience):
    """
    Rule:
    IF experience is Beginner
    AND available time is Short
    THEN Gentle routine.
    """

    time_memberships = calculate_time_memberships(time)

    experience_memberships = calculate_experience_memberships(
        experience
    )

    short_degree = time_memberships["Short"]

    beginner_degree = experience_memberships["Beginner"]

    rule_strength = min(short_degree, beginner_degree)

    return rule_strength


def evaluate_beginner_medium_rule(time, experience):
    """
    Rule:
    IF experience is Beginner
    AND available time is Medium
    THEN Balanced routine.
    """

    time_memberships = calculate_time_memberships(time)

    experience_memberships = calculate_experience_memberships(
        experience
    )

    medium_degree = time_memberships["Medium"]

    beginner_degree = experience_memberships["Beginner"]

    rule_strength = min(medium_degree, beginner_degree)

    return rule_strength


# =====================================
# TESTING THE FUZZY RULES
# =====================================

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

    aggregated_strength = max(
        short_strength,
        medium_strength
    )

    print("\nAvailable time:", time, "minutes")
    print("Experience:", experience)

    print(
        "Short rule strength:",
        round(short_strength, 3)
    )

    print(
        "Medium rule strength:",
        round(medium_strength, 3)
    )

    print(
        "Aggregated strength:",
        round(aggregated_strength, 3)
    )