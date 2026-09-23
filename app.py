import streamlit as st

from app_logic import process_yoga_request
from fuzzy_logic.output import calculate_output_memberships


st.set_page_config(
    page_title="Yoga AI Assistant",
    page_icon="🧘",
    layout="centered"
)


# Stores the generated result.
if "result" not in st.session_state:
    st.session_state.result = None


# Controls fuzzy calculation visibility.
if "show_fuzzy" not in st.session_state:
    st.session_state.show_fuzzy = False


# Page header.
st.title("🧘 AI-Based Yoga Routine Assistant")

st.write(
    "Describe your yoga requirements and get a personalized routine "
    "using AI and fuzzy logic."
)


user_input = st.text_area(
    "Describe your yoga requirements",
    placeholder=(
        "I am a beginner. I have 25 minutes "
        "and want a gentle yoga routine."
    ),
    height=120,
    key="yoga_input"
)


col1, col2 = st.columns(2)

with col1:

    generate = st.button(
        "✨ Generate Yoga Routine",
        use_container_width=True
    )

with col2:

    reset = st.button(
        "🔄 Reset",
        use_container_width=True
    )


# Reset the generated result.
if reset:

    st.session_state.result = None
    st.session_state.show_fuzzy = False

    st.rerun()


# Generate a new routine.
if generate:

    if user_input.strip() == "":

        st.warning(
            "Please describe your yoga requirements."
        )

    else:

        try:

            with st.spinner(
                "Creating your personalized yoga routine..."
            ):

                st.session_state.result = process_yoga_request(
                    user_input
                )

                # Hide fuzzy calculation for every new result.
                st.session_state.show_fuzzy = False

        except Exception as error:

            error_message = str(error)

            if (
                "429" in error_message
                or "RESOURCE_EXHAUSTED" in error_message
                or "quota" in error_message.lower()
            ):

                st.error(
                    "Gemini API quota exceeded."
                )

                st.info(
                    "The AI service has reached its current usage limit. "
                    "Please wait and check your Gemini API quota."
                )

            else:

                st.error(
                    "Something went wrong while generating your routine."
                )

            with st.expander("View Error Details"):

                st.exception(error)


# Display the generated result.
if st.session_state.result:

    result = st.session_state.result

    preferences = result["preferences"]
    routine = result["routine"]
    fuzzy_reasoning = result["fuzzy_reasoning"]
    intensity = result["intensity"]


    st.success(
        "Yoga routine generated successfully!"
    )


    # User preferences section.
    st.subheader("👤 Your Preferences")

    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(
            "Experience",
            preferences["experience"].title()
        )

    with col2:

        st.metric(
            "Available Time",
            f'{preferences["time_minutes"]} min'
        )

    with col3:

        st.metric(
            "Intensity",
            preferences["intensity"].title()
        )


    # Routine summary.
    st.subheader("📊 Routine Summary")

    total_duration = sum(
        pose["duration"]
        for pose in routine["poses"]
    )

    pose_count = len(routine["poses"])

    col1, col2 = st.columns(2)

    with col1:

        st.metric(
            "Number of Poses",
            pose_count
        )

    with col2:

        st.metric(
            "Total Duration",
            f"{total_duration} min"
        )


    # Selected routine.
    st.subheader(
        f'🧘 {routine["name"]}'
    )

    st.write(
        routine["description"]
    )


    # Fuzzy calculation button at the top-right.
    fuzzy_col1, fuzzy_col2 = st.columns([3, 1])

    with fuzzy_col2:

        fuzzy_button_label = (
            "🔽 Hide"
            if st.session_state.show_fuzzy
            else "🧠 Fuzzy"
        )

        if st.button(
            fuzzy_button_label,
            use_container_width=True
        ):

            st.session_state.show_fuzzy = (
                not st.session_state.show_fuzzy
            )

            st.rerun()


    # Display fuzzy calculation only when requested.
    if st.session_state.show_fuzzy:

        st.divider()

        with st.container(border=True):

            st.header("🧠 Fuzzy Calculation")

            st.caption(
                "Technical explanation of how the fuzzy inference "
                "system calculates the yoga routine intensity."
            )


            # Fuzzy intensity score.
            st.subheader("🎯 Fuzzy Intensity Score")

            st.metric(
                "Calculated Intensity",
                f"{intensity:.3f} / 10"
            )

            st.progress(
                min(max(intensity / 10, 0.0), 1.0)
            )

            st.caption(
                "The intensity score is calculated using fuzzy rules "
                "and centroid defuzzification."
            )


            st.divider()


            # Fuzzy membership function visualization.
            st.subheader("📈 Fuzzy Membership Functions")

            x_values = [
                round(i / 10, 1)
                for i in range(0, 101)
            ]

            chart_data = {
                "Gentle": [],
                "Balanced": [],
                "Active": []
            }

            for x in x_values:

                memberships = calculate_output_memberships(x)

                chart_data["Gentle"].append(
                    memberships["Gentle"]
                )

                chart_data["Balanced"].append(
                    memberships["Balanced"]
                )

                chart_data["Active"].append(
                    memberships["Active"]
                )

            st.line_chart(
                chart_data
            )

            st.caption(
                "The graph represents the membership functions "
                "for Gentle, Balanced, and Active intensity."
            )


            st.divider()


            # Fuzzy logic reasoning.
            st.subheader("⚙️ Fuzzy Logic Reasoning")

            with st.expander("View Membership Values"):

                st.write("Time Memberships")

                st.json(
                    fuzzy_reasoning["time_memberships"]
                )

                st.write("Experience Memberships")

                st.json(
                    fuzzy_reasoning["experience_memberships"]
                )


            with st.expander("View Rule Strengths"):

                st.json(
                    fuzzy_reasoning["rule_strengths"]
                )

            st.info(
                "Membership values represent the degree to which "
                "an input belongs to a fuzzy category. Rule strengths "
                "are used to calculate the final intensity."
            )


    # Recommended poses.
    st.subheader("📋 Recommended Poses")

    for index, pose in enumerate(
        routine["poses"],
        start=1
    ):

        with st.container(border=True):

            st.markdown(
                f"### {index}. {pose['name']}"
            )

            st.write(
                f"⏱️ **Duration:** "
                f"{pose['duration']} minutes"
            )

            st.write(
                f"🌿 **Benefit:** "
                f"{pose['benefit']}"
            )


    # AI explanation.
    st.subheader("🤖 AI Explanation")

    st.write(
        result["explanation"]
    )


    # Safety note.
    st.warning(
        "Safety Note: These are general yoga suggestions. "
        "Stop if you experience pain or discomfort. "
        "Consult a qualified instructor or healthcare professional "
        "if you have health concerns or physical limitations."
    )


# Testing section.
st.divider()

st.subheader("🧪 Test the Assistant")

st.markdown(
    """
    **Test 1 — Beginner / Gentle**

    `I am a beginner. I have 25 minutes and want a gentle yoga routine.`

    **Test 2 — Intermediate / Active**

    `I am an intermediate user. I have 45 minutes and want an active routine.`

    **Test 3 — Advanced / Active**

    `I am advanced. I have 60 minutes and want an active yoga routine.`

    **Test 4 — Beginner / Short**

    `I am a beginner. I only have 10 minutes and want gentle yoga.`
    """
)