from membership import triangular_membership


def calculate_experience_memberships(experience):

    beginner = triangular_membership(
        experience, 0, 5, 10
    )

    intermediate = triangular_membership(
        experience, 2, 5, 8
    )

    advanced = triangular_membership(
        experience, 5, 9.5, 10
    )

    return {
        "Beginner": beginner,
        "Intermediate": intermediate,
        "Advanced": advanced
    }


if __name__ == "__main__":

    experience = 4

    result = calculate_experience_memberships(experience)

    print("Experience:", experience)

    for category, degree in result.items():
        print(f"{category}: {degree:.3f}")