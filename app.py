
import streamlit as st

from app_logic import process_yoga_request


st.set_page_config(
    page_title="Yoga AI Assistant",
    page_icon="🧘",
    layout="centered"
)


st.title("🧘 AI-Based Yoga Routine Assistant")

st.write(
    "Describe your yoga requirements and get a personalized routine using "
    "AI and fuzzy logic."
)


user_input = st.text_area(
    "Describe your yoga requirements",
    placeholder=(
        "I am a beginner. I have 25 minutes "
        "and want a gentle yoga routine."
    ),
    height=120
)


if st.button("✨ Generate Yoga Routine", use_container_width=True):

    if user_input.strip() == "":
        st.warning("Please describe your yoga requirements.")

    else:

        try:

            with st.spinner("Creating your personalized yoga routine..."):

                result = process_yoga_request(user_input)

            st.success("Yoga routine generated successfully!")

            preferences = result["preferences"]
            routine = result["routine"]
            fuzzy_reasoning = result["fuzzy_reasoning"]

            # Display user preferences
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

            # Display fuzzy intensity score
            st.subheader("🧠 Fuzzy Intensity Score")

            st.metric(
                "Calculated Intensity",
                f'{result["intensity"]:.3f}'
            )

            st.progress(
                min(max(result["intensity"] / 10, 0.0), 1.0)
            )

            # Display routine information
            st.subheader(f'🧘 {routine["name"]}')

            st.write(routine["description"])

            total_duration = sum(
                pose["duration"]
                for pose in routine["poses"]
            )

            st.info(
                f"⏱️ Total Routine Duration: "
                f"approximately {total_duration} minutes"
            )

            # Display recommended poses
            st.subheader("📋 Recommended Poses")

            for index, pose in enumerate(routine["poses"], start=1):

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

            # Display fuzzy reasoning
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

            # Display AI explanation
            st.subheader("🤖 AI Explanation")

            st.write(
                result["explanation"]
            )

            # Safety note
            st.warning(
                "Safety Note: These are general yoga suggestions. "
                "Stop if you experience pain or discomfort. "
                "Consult a qualified instructor or healthcare professional "
                "if you have health concerns or physical limitations."
            )

        except Exception as error:

            st.error(
                "Something went wrong while generating your routine."
            )

            with st.expander("View Error Details"):

                st.exception(error)