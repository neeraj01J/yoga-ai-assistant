
# Calculates membership values for yoga intensity outputs.

from fuzzy_logic.membership import triangular_membership


GENTLE = (0, 3, 6)
BALANCED = (3, 5, 7)
ACTIVE = (5, 8, 10)


def calculate_output_memberships(intensity):
    """
    Calculate membership degrees for
    Gentle, Balanced, and Active intensity.
    """

    if not isinstance(intensity, (int, float)):
        raise ValueError("Intensity must be a number.")

    if intensity < 0 or intensity > 10:
        raise ValueError("Intensity must be between 0 and 10.")

    gentle_degree = triangular_membership(
        intensity, *GENTLE
    )

    balanced_degree = triangular_membership(
        intensity, *BALANCED
    )

    active_degree = triangular_membership(
        intensity, *ACTIVE
    )

    return {
        "Gentle": gentle_degree,
        "Balanced": balanced_degree,
        "Active": active_degree
    }


# Test the output membership function

if __name__ == "__main__":

    intensity = 5

    results = calculate_output_memberships(
        intensity
    )

    print("Intensity:", intensity)

    for category, degree in results.items():

        print(
            f"{category}: {degree:.3f}"
        )