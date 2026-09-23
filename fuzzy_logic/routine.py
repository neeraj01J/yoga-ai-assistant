
# Selects a yoga routine and adjusts it to available time.


def _allocate_durations(total_time, pose_count):
    """Distributes available time across the selected poses."""

    total_time = max(int(total_time), pose_count)

    base_duration = total_time // pose_count
    remainder = total_time % pose_count

    durations = [
        base_duration
        for _ in range(pose_count)
    ]

    for index in range(remainder):
        durations[index] += 1

    return durations


def _create_poses(pose_templates, total_time):
    """Creates poses with durations that match available time."""

    pose_count = min(
        len(pose_templates),
        max(3, total_time // 6)
    )

    selected_templates = pose_templates[:pose_count]

    durations = _allocate_durations(
        total_time,
        pose_count
    )

    poses = []

    for template, duration in zip(
        selected_templates,
        durations
    ):

        poses.append({
            "name": template["name"],
            "duration": duration,
            "benefit": template["benefit"]
        })

    return poses


def _get_routine_category(
    intensity,
    requested_intensity
):

    if requested_intensity == "gentle":

        return "gentle"

    if requested_intensity == "active":

        return "active"

    if requested_intensity == "balanced":

        return "balanced"

    if intensity < 3.5:

        return "gentle"

    if intensity < 6.5:

        return "balanced"

    return "active"


def select_routine(
    intensity,
    requested_intensity="unknown",
    available_time=25
):

    category = _get_routine_category(
        intensity,
        requested_intensity
    )

    available_time = max(
        int(available_time),
        3
    )

    gentle_templates = [

        {
            "name": "Child's Pose",
            "benefit": (
                "Encourages relaxation and gentle stretching."
            )
        },

        {
            "name": "Cat-Cow",
            "benefit": (
                "Improves spinal mobility and body awareness."
            )
        },

        {
            "name": "Easy Seated Pose",
            "benefit": (
                "Supports calm breathing and relaxation."
            )
        },

        {
            "name": "Standing Forward Fold",
            "benefit": (
                "Encourages gentle stretching of the back and legs."
            )
        },

        {
            "name": "Cobra Pose",
            "benefit": (
                "Supports gentle chest opening and spinal movement."
            )
        },

        {
            "name": "Supine Twist",
            "benefit": (
                "Encourages gentle spinal rotation and relaxation."
            )
        },

        {
            "name": "Legs-Up-the-Wall",
            "benefit": (
                "Supports relaxation and calm breathing."
            )
        },

        {
            "name": "Resting Pose",
            "benefit": (
                "Provides time for relaxation and mindful breathing."
            )
        }

    ]

    balanced_templates = [

        {
            "name": "Cat-Cow",
            "benefit": (
                "Improves spinal mobility and body awareness."
            )
        },

        {
            "name": "Downward-Facing Dog",
            "benefit": (
                "Encourages full-body stretching and mobility."
            )
        },

        {
            "name": "Warrior II",
            "benefit": (
                "Develops balance and lower-body strength."
            )
        },

        {
            "name": "Tree Pose",
            "benefit": (
                "Practices balance and concentration."
            )
        },

        {
            "name": "Bridge Pose",
            "benefit": (
                "Engages the lower body and supports mobility."
            )
        },

        {
            "name": "Low Lunge",
            "benefit": (
                "Supports hip mobility and leg stretching."
            )
        },

        {
            "name": "Seated Forward Fold",
            "benefit": (
                "Encourages gentle stretching of the back and legs."
            )
        },

        {
            "name": "Relaxation Pose",
            "benefit": (
                "Allows the body to relax after movement."
            )
        }

    ]

    active_templates = [

        {
            "name": "Cat-Cow",
            "benefit": (
                "Warms up the spine and improves mobility."
            )
        },

        {
            "name": "Warrior II",
            "benefit": (
                "Develops balance and lower-body strength."
            )
        },

        {
            "name": "Chair Pose",
            "benefit": (
                "Builds leg and core strength."
            )
        },

        {
            "name": "Plank",
            "benefit": (
                "Activates the core and upper body."
            )
        },

        {
            "name": "Downward-Facing Dog",
            "benefit": (
                "Encourages full-body stretching and stability."
            )
        },

        {
            "name": "High Lunge",
            "benefit": (
                "Develops balance and lower-body engagement."
            )
        },

        {
            "name": "Boat Pose",
            "benefit": (
                "Engages the core and supports body control."
            )
        },

        {
            "name": "Standing Forward Fold",
            "benefit": (
                "Encourages recovery and gentle stretching."
            )
        },

        {
            "name": "Relaxation Pose",
            "benefit": (
                "Allows the body to cool down and relax."
            )
        }

    ]

    if category == "gentle":

        templates = gentle_templates
        name = "Gentle Yoga"
        description = (
            "A light and relaxing yoga routine "
            "adjusted to your available time."
        )

    elif category == "balanced":

        templates = balanced_templates
        name = "Balanced Yoga"
        description = (
            "A balanced yoga routine combining "
            "mobility, strength, and relaxation."
        )

    else:

        templates = active_templates
        name = "Active Yoga"
        description = (
            "A more energetic yoga routine "
            "adjusted to your available time."
        )

    poses = _create_poses(
        templates,
        available_time
    )

    return {
        "name": name,
        "description": description,
        "poses": poses
    }


if __name__ == "__main__":

    sample_routine = select_routine(
        intensity=7.6,
        requested_intensity="active",
        available_time=45
    )

    print(sample_routine["name"])
    print(sample_routine["description"])

    print("\nRecommended Poses:")

    total_duration = 0

    for index, pose in enumerate(
        sample_routine["poses"],
        start=1
    ):

        print(
            f"{index}. {pose['name']} - "
            f"{pose['duration']} minutes"
        )

        total_duration += pose["duration"]

    print(
        f"\nTotal Duration: {total_duration} minutes"
    )