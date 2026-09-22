
def select_routine(intensity, requested_intensity="unknown"):
    """
    Select a yoga routine using fuzzy intensity
    and the user's requested intensity.
    """

    if requested_intensity == "gentle":

        return {
            "name": "Gentle Yoga",
            "description": "A light and relaxing yoga routine.",
            "poses": [
                "Child's Pose",
                "Cat-Cow",
                "Easy Seated Pose"
            ]
        }

    elif requested_intensity == "active":

        return {
            "name": "Active Yoga",
            "description": "A more energetic yoga routine.",
            "poses": [
                "Cat-Cow",
                "Warrior II",
                "Chair Pose",
                "Plank"
            ]
        }

    elif intensity < 3.5:

        return {
            "name": "Gentle Yoga",
            "description": "A light and relaxing yoga routine.",
            "poses": [
                "Child's Pose",
                "Cat-Cow",
                "Easy Seated Pose"
            ]
        }

    elif intensity < 6.5:

        return {
            "name": "Balanced Yoga",
            "description": "A moderate yoga routine for balance and flexibility.",
            "poses": [
                "Cat-Cow",
                "Downward-Facing Dog",
                "Warrior II",
                "Tree Pose"
            ]
        }

    else:

        return {
            "name": "Active Yoga",
            "description": "A more energetic yoga routine.",
            "poses": [
                "Cat-Cow",
                "Warrior II",
                "Chair Pose",
                "Plank"
            ]
        }


# Test the routine selection

if __name__ == "__main__":

    intensity = 3.927
    requested_intensity = "gentle"

    routine = select_routine(
        intensity,
        requested_intensity
    )

    print("Selected Routine:", routine["name"])
    print("Description:", routine["description"])

    print("\nRecommended Poses:")

    for pose in routine["poses"]:

        print("-", pose)