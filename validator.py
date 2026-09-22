
# Validates and normalizes AI-extracted yoga preferences.

def validate_preferences(preferences):

    # Allowed experience levels
    valid_experiences = [
        "beginner",
        "intermediate",
        "advanced"
    ]

    # Allowed intensity levels
    valid_intensities = [
        "gentle",
        "balanced",
        "active",
        "unknown"
    ]

    # Extract values from the AI response
    experience = str(
        preferences.get("experience", "")
    ).lower().strip()

    time_minutes = preferences.get("time_minutes")

    intensity = str(
        preferences.get("intensity", "unknown")
    ).lower().strip()

    # Validate experience
    if experience not in valid_experiences:
        raise ValueError(
            "Invalid experience level."
        )

    # Validate available time
    if not isinstance(time_minutes, (int, float)):
        raise ValueError(
            "Time must be a number."
        )

    if time_minutes <= 0:
        raise ValueError(
            "Time must be greater than zero."
        )

    # Validate intensity
    if intensity not in valid_intensities:
        intensity = "unknown"

    # Return cleaned and validated preferences
    return {
        "experience": experience,
        "time_minutes": int(time_minutes),
        "intensity": intensity
    }


if __name__ == "__main__":

    # Sample AI response for testing
    sample_preferences = {
        "experience": "beginner",
        "time_minutes": 25,
        "intensity": "gentle"
    }

    validated_data = validate_preferences(
        sample_preferences
    )

    print("Validated Preferences:")
    print(validated_data)