
import streamlit as st

from app_logic import process_yoga_request
from fuzzy_logic.output import calculate_output_memberships


# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="Yoga AI Assistant",
    page_icon="🧘",
    layout="centered"
)


# =========================================================
# CUSTOM CSS STYLING
# =========================================================

st.markdown(
    """
    <style>

    /* =========================================
       APPLICATION
    ========================================= */

    .stApp {
        background-color: var(--background-color);
    }

    .block-container {
        max-width: 1050px;
        padding-top: 2.2rem;
        padding-bottom: 3rem;
    }

    header[data-testid="stHeader"] {
        background-color: var(--background-color);
    }

    footer {
        visibility: hidden;
    }


    /* =========================================
       TYPOGRAPHY
    ========================================= */

    h1 {
        font-size: 2.35rem !important;
        font-weight: 750 !important;
        letter-spacing: -1.4px;
        line-height: 1.2 !important;
        margin-bottom: 0.7rem !important;
    }

    h2 {
        font-size: 1.4rem !important;
        font-weight: 750 !important;
        letter-spacing: -0.4px;
        margin-top: 1.7rem !important;
        margin-bottom: 0.7rem !important;
    }

    h3 {
        font-size: 1.1rem !important;
        font-weight: 700 !important;
    }

    p {
        line-height: 1.65;
    }


    /* =========================================
       BRAND AND INTRODUCTION
    ========================================= */

    .brand-label {
        font-size: 0.72rem;
        font-weight: 750;
        letter-spacing: 0.13rem;
        text-transform: uppercase;
        opacity: 0.6;
        margin-bottom: 0.75rem;
    }

    .hero-description {
        font-size: 0.95rem;
        line-height: 1.7;
        opacity: 0.72;
        margin-bottom: 1.1rem;
    }


    /* =========================================
       TEXT AREA
    ========================================= */

    .stTextArea label {
        font-size: 0.88rem !important;
        font-weight: 650 !important;
    }

    .stTextArea textarea {
        border-radius: 14px !important;
        border: 1px solid var(--border-color, #d9dee7) !important;
        padding: 15px !important;
        font-size: 0.95rem !important;
        line-height: 1.6 !important;
        box-shadow: none !important;
        transition:
            border-color 0.2s ease,
            box-shadow 0.2s ease !important;
    }

    .stTextArea textarea:focus {
        border-color: var(--primary-color) !important;
        box-shadow: 0 0 0 1px var(--primary-color) !important;
    }


    /* =========================================
       BUTTONS
    ========================================= */

    .stButton > button {
        min-height: 45px;
        border-radius: 12px !important;
        border: 1px solid var(--border-color, #d9dee7) !important;
        font-size: 0.88rem !important;
        font-weight: 650 !important;
        transition:
            transform 0.2s ease,
            border-color 0.2s ease,
            background-color 0.2s ease !important;
    }

    .stButton > button:hover {
        border-color: var(--primary-color) !important;
        transform: translateY(-1px);
    }

    .stButton > button:focus {
        box-shadow: none !important;
    }


    /* =========================================
       METRIC CARDS
    ========================================= */

    [data-testid="stMetric"] {
        background: var(--secondary-background-color);
        border: 1px solid var(--border-color, #d9dee7);
        border-radius: 14px;
        padding: 15px 17px;
        transition:
            transform 0.2s ease,
            border-color 0.2s ease;
    }

    [data-testid="stMetric"]:hover {
        border-color: var(--primary-color);
        transform: translateY(-2px);
    }

    [data-testid="stMetricLabel"] {
        font-size: 0.78rem !important;
        font-weight: 550 !important;
    }

    [data-testid="stMetricValue"] {
        font-size: 1.3rem !important;
        font-weight: 750 !important;
    }


    /* =========================================
       BORDERED CONTAINERS
    ========================================= */

    [data-testid="stVerticalBlockBorderWrapper"] {
        border-radius: 15px !important;
        border: 1px solid var(--border-color, #d9dee7) !important;
        background: var(--secondary-background-color);
        padding: 5px;
        transition: border-color 0.2s ease;
    }

    [data-testid="stVerticalBlockBorderWrapper"]:hover {
        border-color: var(--primary-color) !important;
    }


    /* =========================================
       EXPANDERS
    ========================================= */

    [data-testid="stExpander"] {
        border-radius: 12px !important;
        border: 1px solid var(--border-color, #d9dee7) !important;
        background: var(--secondary-background-color);
    }


    /* =========================================
       ALERTS
    ========================================= */

    [data-testid="stAlert"] {
        border-radius: 12px !important;
    }


    /* =========================================
       DIVIDERS
    ========================================= */

    hr {
        margin-top: 1.4rem !important;
        margin-bottom: 1.4rem !important;
        border-color: var(--border-color, #d9dee7) !important;
    }


    /* =========================================
       PROGRESS BAR
    ========================================= */

    [data-testid="stProgressBar"] > div > div {
        border-radius: 20px;
    }


    /* =========================================
       RESPONSIVE DESIGN
    ========================================= */

    @media (max-width: 700px) {

        .block-container {
            padding-top: 1.4rem;
            padding-left: 1rem;
            padding-right: 1rem;
            padding-bottom: 2rem;
        }

        h1 {
            font-size: 2rem !important;
        }

        h2 {
            font-size: 1.25rem !important;
        }

        [data-testid="stMetricValue"] {
            font-size: 1.05rem !important;
        }

    }

    </style>
    """,
    unsafe_allow_html=True
)


# =========================================================
# SESSION STATE
# =========================================================

if "result" not in st.session_state:
    st.session_state.result = None

if "show_fuzzy" not in st.session_state:
    st.session_state.show_fuzzy = False


# =========================================================
# PAGE HEADER
# =========================================================

st.markdown(
    """
    <div class="brand-label">
        YOGAFLOW AI / PERSONAL PRACTICE
    </div>
    """,
    unsafe_allow_html=True
)

st.title("🧘 AI-Based Yoga Routine Assistant")

st.markdown(
    """
    <div class="hero-description">
        Describe your yoga requirements and get a personalized
        routine using AI and fuzzy logic.
    </div>
    """,
    unsafe_allow_html=True
)


# =========================================================
# USER INPUT
# =========================================================

user_input = st.text_area(
    "Describe your yoga requirements",
    placeholder=(
        "I am a beginner. I have 25 minutes "
        "and want a gentle yoga routine."
    ),
    height=120,
    key="yoga_input"
)


# =========================================================
# ACTION BUTTONS
# =========================================================

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


# =========================================================
# RESET
# =========================================================

if reset:

    st.session_state.result = None
    st.session_state.show_fuzzy = False

    st.rerun()


# =========================================================
# GENERATE ROUTINE
# =========================================================

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

                st.session_state.show_fuzzy = False

        except Exception as error:

            error_message = str(error).lower()


            # ---------------------------------------------
            # TIMEOUT ERROR
            # ---------------------------------------------

            if (
                "readtimeout" in error_message
                or "timed out" in error_message
                or "timeout" in error_message
            ):

                st.error(
                    "⏳ The AI service took too long to respond."
                )

                st.info(
                    "Please try again in a few seconds. "
                    "The request may have been delayed by the "
                    "AI service or your internet connection."
                )


            # ---------------------------------------------
            # API QUOTA ERROR
            # ---------------------------------------------

            elif (
                "429" in error_message
                or "resource_exhausted" in error_message
                or "quota" in error_message
            ):

                st.error(
                    "⚠️ Gemini API quota exceeded."
                )

                st.info(
                    "The AI service has reached its current "
                    "usage limit. Please wait and check "
                    "your Gemini API quota."
                )


            # ---------------------------------------------
            # CONNECTION ERROR
            # ---------------------------------------------

            elif (
                "connecterror" in error_message
                or "connection" in error_message
                or "network" in error_message
            ):

                st.error(
                    "🌐 Unable to connect to the AI service."
                )

                st.info(
                    "Check your internet connection and try again."
                )


            # ---------------------------------------------
            # OTHER ERRORS
            # ---------------------------------------------

            else:

                st.error(
                    "Something went wrong while generating "
                    "your routine."
                )

                st.info(
                    "Please try again. If the issue continues, "
                    "check the technical details below."
                )


            # ---------------------------------------------
            # ERROR DETAILS
            # ---------------------------------------------

            with st.expander("View Error Details"):

                st.exception(error)


# =========================================================
# DISPLAY GENERATED RESULT
# =========================================================

if st.session_state.result:

    result = st.session_state.result

    preferences = result["preferences"]
    routine = result["routine"]
    fuzzy_reasoning = result["fuzzy_reasoning"]
    intensity = result["intensity"]


    # =====================================================
    # SUCCESS MESSAGE
    # =====================================================

    st.success(
        "Yoga routine generated successfully!"
    )


    # =====================================================
    # USER PREFERENCES
    # =====================================================

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


    # =====================================================
    # ROUTINE SUMMARY
    # =====================================================

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


    # =====================================================
    # SELECTED ROUTINE
    # =====================================================

    st.subheader(
        f'🧘 {routine["name"]}'
    )

    st.write(
        routine["description"]
    )


    # =====================================================
    # FUZZY BUTTON
    # =====================================================

    fuzzy_col1, fuzzy_col2 = st.columns([3, 1])

    with fuzzy_col1:

        st.caption(
            "View the technical fuzzy inference details "
            "used to calculate the routine intensity."
        )

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


    # =====================================================
    # FUZZY CALCULATION
    # =====================================================

    if st.session_state.show_fuzzy:

        st.divider()

        with st.container(border=True):

            st.header("🧠 Fuzzy Calculation")

            st.caption(
                "Technical explanation of how the fuzzy inference "
                "system calculates the yoga routine intensity."
            )


            # ---------------------------------------------
            # INTENSITY SCORE
            # ---------------------------------------------

            st.subheader("🎯 Fuzzy Intensity Score")

            st.metric(
                "Calculated Intensity",
                f"{intensity:.3f} / 10"
            )

            st.progress(
                min(max(intensity / 10, 0.0), 1.0)
            )

            st.caption(
                "The intensity score is calculated using fuzzy "
                "rules and centroid defuzzification."
            )


            st.divider()


            # ---------------------------------------------
            # MEMBERSHIP FUNCTIONS
            # ---------------------------------------------

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

            st.line_chart(chart_data)

            st.caption(
                "The graph represents the membership functions "
                "for Gentle, Balanced, and Active intensity."
            )


            st.divider()


            # ---------------------------------------------
            # FUZZY REASONING
            # ---------------------------------------------

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
                "an input belongs to a fuzzy category. Rule "
                "strengths are used to calculate the final intensity."
            )


    # =====================================================
    # RECOMMENDED POSES
    # =====================================================

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


    # =====================================================
    # AI EXPLANATION
    # =====================================================

    st.subheader("🤖 AI Explanation")

    st.write(
        result["explanation"]
    )


    # =====================================================
    # SAFETY NOTE
    # =====================================================

    st.warning(
        "Safety Note: These are general yoga suggestions. "
        "Stop if you experience pain or discomfort. "
        "Consult a qualified instructor or healthcare "
        "professional if you have health concerns or "
        "physical limitations."
    )


# =========================================================
# TESTING SECTION
# =========================================================

st.divider()

st.subheader("🧪 Test the Assistant")

with st.expander("View testing examples"):

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