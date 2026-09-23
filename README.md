
# 🧘 AI-Based Yoga Routine Selection Assistant

An AI-powered yoga routine selection assistant that generates personalized yoga routines based on a user's experience level, available time, and preferred intensity.

The project combines **Artificial Intelligence (AI)** and **Fuzzy Logic** to analyze user preferences, calculate an appropriate yoga intensity, and recommend a suitable yoga routine.

The application provides a Streamlit web interface where users can describe their yoga requirements using natural language.

---

## 📌 Project Overview

The AI-Based Yoga Routine Selection Assistant is designed to help users select a suitable yoga routine based on their individual requirements.

Users can enter a description such as:

> I am a beginner. I have 25 minutes and want a gentle yoga routine.

The application processes the user's input using an AI-based preference extraction system and fuzzy logic.

The fuzzy inference system evaluates factors such as:

- Yoga experience
- Available time
- Preferred intensity

Based on the processed preferences, the application generates a suitable yoga routine with recommended poses, durations, benefits, and an AI-generated explanation.

---

## ✨ Features

### 🤖 AI-Based Processing

- Accepts natural-language yoga requirements.
- Extracts user preferences from input.
- Processes experience level and available time.
- Supports AI-generated yoga routine selection.
- Provides an explanation for the generated routine.
- Handles AI service errors and timeout situations.

### 🧠 Fuzzy Logic System

- Time membership functions.
- Experience membership functions.
- Preference processing.
- Fuzzy rule evaluation.
- Mamdani aggregation.
- Centroid defuzzification.
- Fuzzy intensity calculation.
- Gentle, Balanced, and Active intensity categories.
- Fuzzy membership function visualization.

### 🧘 Yoga Routine Selection

- Automatic yoga routine selection.
- Recommended yoga poses.
- Pose duration.
- Pose benefits.
- Total routine duration.
- Number of recommended poses.
- Personalized routine description.
- AI-generated explanation.

### 🖥️ Streamlit Web Interface

- Simple and user-friendly interface.
- Natural-language input field.
- Generate Yoga Routine button.
- Reset functionality.
- User preference summary.
- Routine summary metrics.
- Fuzzy calculation visibility toggle.
- Fuzzy intensity score display.
- Fuzzy membership function chart.
- Fuzzy reasoning details.
- Recommended pose cards.
- AI explanation section.
- Yoga safety information.
- Testing examples.

### ⚠️ Error Handling

- AI service timeout handling.
- API quota error handling.
- Connection error handling.
- Expandable technical error details.
- User-friendly error messages.

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Streamlit | Web application interface |
| Fuzzy Logic | Intensity calculation and routine selection |
| Google Gemini / AI Service | Natural-language processing and routine generation |
| Git | Version control |
| GitHub | Source code hosting |
| Virtual Environment | Dependency isolation |

> The exact AI provider configuration and dependencies are defined in the project source files and environment configuration.

---

## 📂 Project Structure

```text
yoga-ai-assistant/
│
├── fuzzy_logic/
│   │
│   ├── __pycache__/
│   │
│   ├── experience.py
│   ├── inference.py
│   ├── membership.py
│   ├── output.py
│   ├── preference.py
│   ├── routine.py
│   └── rules.py
│
├── __pycache__/
│
├── .env
├── .gitignore
│
├── ai_explanation.py
├── ai_extractor.py
├── app_logic.py
├── app.py
├── gemini_test.py
├── main.py
├── README.md
└── validator.py
```

### Project Files

| File / Folder | Description |
|---|---|
| `fuzzy_logic/` | Contains the fuzzy logic modules used by the application |
| `experience.py` | Handles experience-related fuzzy calculations |
| `inference.py` | Performs fuzzy inference processing |
| `membership.py` | Defines fuzzy membership functions |
| `output.py` | Defines output membership functions |
| `preference.py` | Supports preference-related processing |
| `routine.py` | Supports yoga routine selection |
| `rules.py` | Contains fuzzy inference rules |
| `ai_explanation.py` | Handles AI-based routine explanations |
| `ai_extractor.py` | Extracts user preferences from natural-language input |
| `app_logic.py` | Contains the main application processing logic |
| `app.py` | Streamlit application interface |
| `gemini_test.py` | Used for testing the Gemini AI integration |
| `main.py` | Main Python entry point or development file |
| `validator.py` | Validates input or extracted preference data |
| `.env` | Stores environment configuration and secret values |
| `.gitignore` | Specifies files excluded from Git tracking |
| `README.md` | Project documentation |

---

## 🔄 Application Workflow

```text
User enters yoga requirements
            │
            ▼
Streamlit user interface
            │
            ▼
Process user input
            │
            ▼
Extract user preferences using AI
            │
            ▼
Validate extracted preferences
            │
            ▼
Process time and experience factors
            │
            ▼
Calculate fuzzy membership values
            │
            ▼
Evaluate fuzzy rules
            │
            ▼
Mamdani aggregation
            │
            ▼
Centroid defuzzification
            │
            ▼
Calculate yoga intensity
            │
            ▼
Select suitable yoga routine
            │
            ▼
Generate routine explanation
            │
            ▼
Display recommended yoga poses
```

---

## 🧠 Fuzzy Logic System

The fuzzy logic system is used to handle uncertain or flexible user preferences.

Instead of depending only on fixed categories, fuzzy logic allows an input to have different degrees of membership in a category.

### Input Factors

- Available time.
- Yoga experience.
- User preference information.

### Output Categories

- Gentle.
- Balanced.
- Active.

### Fuzzy Processing Steps

1. Receive the processed user preferences.
2. Calculate input membership values.
3. Evaluate fuzzy rules.
4. Perform Mamdani aggregation.
5. Apply centroid defuzzification.
6. Calculate the final intensity score.
7. Select a suitable yoga routine.

The Streamlit interface provides an optional fuzzy calculation section where users can inspect the intensity score, membership function chart, membership values, and rule strengths.

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/neeraj01J/yoga-ai-assistant.git
```

### 2. Open the Project Folder

```bash
cd yoga-ai-assistant
```

### 3. Create a Virtual Environment

On Windows:

```powershell
python -m venv .venv
```

### 4. Activate the Virtual Environment

Using PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

Using Git Bash:

```bash
source .venv/Scripts/activate
```

### 5. Install Project Dependencies

If a `requirements.txt` file is available:

```bash
pip install -r requirements.txt
```

Otherwise, install the dependencies required by the project configuration.

### 6. Configure Environment Variables

Create or configure the `.env` file with the required AI service settings.

Example:

```env
GEMINI_API_KEY=your_api_key_here
```

> The environment variable name must match the name used by the project code.

Do not upload API keys or other confidential information to GitHub.

### 7. Run the Streamlit Application

```bash
python -m streamlit run app.py
```

The application will normally be available at:

```text
http://localhost:8501
```

---

## 🧪 Example User Inputs

### Test 1 — Beginner / Gentle

```text
I am a beginner. I have 25 minutes and want a gentle yoga routine.
```

### Test 2 — Intermediate / Active

```text
I am an intermediate user. I have 45 minutes and want an active routine.
```

### Test 3 — Advanced / Active

```text
I am advanced. I have 60 minutes and want an active yoga routine.
```

### Test 4 — Beginner / Short Routine

```text
I am a beginner. I only have 10 minutes and want gentle yoga.
```

---

## 📊 Application Output

The application displays the following information after generating a routine:

- User experience level.
- Available time.
- Preferred intensity.
- Number of recommended poses.
- Total routine duration.
- Selected yoga routine.
- Routine description.
- Recommended yoga poses.
- Pose duration.
- Pose benefits.
- AI-generated explanation.
- Fuzzy intensity score.
- Fuzzy membership function visualization.
- Fuzzy membership values.
- Fuzzy rule strengths.
- Safety information.

---

## 🧩 Error Handling

The application includes error handling for common AI service issues.

### Timeout Error

If the AI service takes too long to respond, the application displays a timeout message and suggests trying again.

### API Quota Error

If the AI service usage limit is reached, the application displays a quota-related message.

### Connection Error

If the application cannot connect to the AI service, the interface displays a connection error message.

### Technical Error Details

Additional error details can be viewed through the expandable error details section.

---

## 🔧 Development Progress

- [x] Python project setup
- [x] Time membership functions
- [x] Experience membership functions
- [x] Fuzzy rule evaluation
- [x] Mamdani aggregation
- [x] Centroid defuzzification
- [x] Yoga routine selection
- [x] AI-based preference extraction
- [x] Preference validation
- [x] AI-generated routine explanation
- [x] Streamlit user interface
- [x] Natural-language user input
- [x] Recommended yoga poses
- [x] Routine summary
- [x] Fuzzy intensity score
- [x] Fuzzy membership function visualization
- [x] Fuzzy reasoning display
- [x] Reset functionality
- [x] API error handling
- [x] Timeout error handling
- [x] GitHub repository setup
- [ ] Automated testing
- [ ] Application deployment
- [ ] Further routine personalization

---

## 🌱 Future Improvements

Potential future improvements include:

- User accounts and saved yoga routines.
- Yoga routine history.
- Additional yoga poses and categories.
- Voice-based user input.
- Progress tracking.
- More advanced routine personalization.
- Improved mobile responsiveness.
- Automated unit testing.
- Cloud deployment.
- AI request optimization.
- Additional wellness and flexibility goals.

---

## ⚠️ Safety Notice

This application provides general yoga suggestions for educational and informational purposes.

Users should:

- Stop exercising if they experience pain or discomfort.
- Practice within their individual abilities.
- Avoid forcing movements or poses.
- Consult a qualified yoga instructor or healthcare professional if they have health concerns or physical limitations.

The application is not a replacement for professional medical advice, diagnosis, or treatment.

---

## 🔐 Security Guidelines

The project uses environment variables for configuration and API credentials.

Make sure sensitive files are excluded from Git tracking.

Recommended `.gitignore` entries:

```gitignore
.env
.venv/
__pycache__/
*.pyc
```

Never commit API keys, passwords, or other private credentials to a public repository.

---

## 🌿 Git Branches

The project uses Git for version control.

Example development branches:

```text
master
   │
   └── ui-improvements
```

The `ui-improvements` branch is used for developing and testing user interface improvements before merging changes into the main branch.

---

## 👨‍💻 Author

**Neeraj Jaiswar**

BSc Information Technology

GitHub:  
https://github.com/neeraj01J

---

## 📄 License

This project is developed for educational and academic purposes.
```