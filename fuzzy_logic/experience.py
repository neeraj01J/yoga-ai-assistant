
# Calculates fuzzy membership values for experience levels.

from fuzzy_logic.membership import triangular_membership


def calculate_experience_memberships(experience):

    beginner = triangular_membership(
        experience, 0, 2, 5
    )

    intermediate = triangular_membership(
        experience, 2, 5, 8
    )

    advanced = triangular_membership(
        experience, 5, 8, 10
    )

    return {
        "Beginner": beginner,
        "Intermediate": intermediate,
        "Advanced": advanced
    }


if __name__ == "__main__":

    experience_values = [2, 5, 8]

    for experience in experience_values:

        result = calculate_experience_memberships(
            experience
        )

        print("\nExperience:", experience)

        for category, degree in result.items():

            print(
                f"{category}: {degree:.3f}"
            )