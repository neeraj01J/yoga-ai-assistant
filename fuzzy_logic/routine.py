
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
                {
                    "name": "Child's Pose",
                    "duration": 3,
                    "benefit": "Encourages relaxation and gentle stretching."
                },
                {
                    "name": "Cat-Cow",
                    "duration": 4,
                    "benefit": "Improves spinal mobility and body awareness."
                },
                {
                    "name": "Easy Seated Pose",
                    "duration": 3,
                    "benefit": "Supports calm breathing and relaxation."
                }
            ]
        }

    elif requested_intensity == "active":

        return {
            "name": "Active Yoga",
            "description": "A more energetic yoga routine.",
            "poses": [
                {
                    "name": "Cat-Cow",
                    "duration": 4,
                    "benefit": "Warms up the spine and improves mobility."
                },
                {
                    "name": "Warrior II",
                    "duration": 5,
                    "benefit": "Develops balance and lower-body strength."
                },
                {
                    "name": "Chair Pose",
                    "duration": 4,
                    "benefit": "Builds leg and core strength."
                },
                {
                    "name": "Plank",
                    "duration": 3,
                    "benefit": "Activates the core and upper body."
                }
            ]
        }

    elif intensity < 3.5:

        return {
            "name": "Gentle Yoga",
            "description": "A light and relaxing yoga routine.",
            "poses": [
                {
                    "name": "Child's Pose",
                    "duration": 3,
                    "benefit": "Encourages relaxation and gentle stretching."
                },
                {
                    "name": "Cat-Cow",
                    "duration": 4,
                    "benefit": "Improves spinal mobility and body awareness."
                },
                {
                    "name": "Easy Seated Pose",
                    "duration": 3,
                    "benefit": "Supports calm breathing and relaxation."
                }
            ]
        }

    elif intensity < 6.5:

        return {
            "name": "Balanced Yoga",
            "description": "A moderate yoga routine for balance and flexibility.",
            "poses": [
                {
                    "name": "Cat-Cow",
                    "duration": 4,
                    "benefit": "Warms up the spine and improves mobility."
                },
                {
                    "name": "Downward-Facing Dog",
                    "duration": 5,
                    "benefit": "Stretches the back and legs."
                },
                {
                    "name": "Warrior II",
                    "duration": 5,
                    "benefit": "Develops balance and lower-body strength."
                },
                {
                    "name": "Tree Pose",
                    "duration": 3,
                    "benefit": "Practices balance and concentration."
                }
            ]
        }

    else:

        return {
            "name": "Active Yoga",
            "description": "A more energetic yoga routine.",
            "poses": [
                {
                    "name": "Cat-Cow",
                    "duration": 4,
                    "benefit": "Warms up the spine and improves mobility."
                },
                {
                    "name": "Warrior II",
                    "duration": 5,
                    "benefit": "Develops balance and lower-body strength."
                },
                {
                    "name": "Chair Pose",
                    "duration": 4,
                    "benefit": "Builds leg and core strength."
                },
                {
                    "name": "Plank",
                    "duration": 3,
                    "benefit": "Activates the core and upper body."
                }
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

        print(
            f"- {pose['name']} "
            f"({pose['duration']} minutes)"
        )

        print(
            f"  Benefit: {pose['benefit']}"
        )