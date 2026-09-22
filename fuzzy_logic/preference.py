
# Calculates fuzzy membership values for intensity preference.

def calculate_preference_memberships(preference):

    preference = preference.lower().strip()

    if preference == "gentle":

        return {
            "Gentle": 1.0,
            "Balanced": 0.0,
            "Active": 0.0
        }

    elif preference == "balanced":

        return {
            "Gentle": 0.0,
            "Balanced": 1.0,
            "Active": 0.0
        }

    elif preference == "active":

        return {
            "Gentle": 0.0,
            "Balanced": 0.0,
            "Active": 1.0
        }

    else:

        return {
            "Gentle": 0.0,
            "Balanced": 0.0,
            "Active": 0.0
        }


if __name__ == "__main__":

    preference = "gentle"

    result = calculate_preference_memberships(
        preference
    )

    print("Preference:", preference)

    for category, degree in result.items():

        print(f"{category}: {degree:.3f}")