
# 🧘 AI-Based Yoga Routine Selection Assistant

An AI-powered yoga routine selection assistant that generates personalized yoga routines based on a user's **experience level, available time, and preferred intensity**.

The project combines **Artificial Intelligence and Fuzzy Logic** to select suitable yoga routines and provide recommended yoga poses.

The application features a Streamlit web interface where users can describe their yoga requirements in natural language and receive a personalized routine.

---

## 📌 Project Overview

The AI-Based Yoga Routine Selection Assistant is designed to provide personalized yoga routine recommendations.

Users can describe their requirements using natural language, for example:

> I am a beginner. I have 25 minutes and want a gentle yoga routine.

The system processes the user's requirements, identifies relevant preferences, and uses fuzzy logic to determine an appropriate routine intensity.

The application then generates a yoga routine containing recommended poses, durations, benefits, and an AI-generated explanation.

---

## ✨ Features

### 🤖 AI-Powered Routine Generation

- Accepts natural-language yoga requirements.
- Processes user preferences using an AI service.
- Generates personalized yoga routines.
- Provides an explanation for the generated routine.

### 🧠 Fuzzy Logic System

- Time membership functions.
- Experience membership functions.
- Fuzzy rule evaluation.
- Mamdani aggregation.
- Centroid defuzzification.
- Fuzzy intensity calculation.
- Gentle, Balanced, and Active intensity membership functions.

### 🧘 Yoga Routine Recommendations

- Automatic routine selection.
- Recommended yoga poses.
- Pose duration.
- Benefits of each pose.
- Total routine duration.
- Number of recommended poses.

### 🖥️ Streamlit Web Interface

- User-friendly web interface.
- Natural-language input using a text area.
- Generate Yoga Routine button.
- Reset functionality.
- User preference summary.
- Routine summary metrics.
- Fuzzy calculation visibility toggle.
- Fuzzy membership function visualization.
- AI-generated explanation.
- Safety information for users.
- Testing examples.

### ⚠️ Error Handling

- AI service timeout handling.
- API quota error handling.
- Connection error handling.
- Expandable technical error details.

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Streamlit | Web application interface |
| Fuzzy Logic | Intensity calculation and routine selection |
| Google Gemini / AI Service | Natural-language processing and routine generation |
| HTTPX / HTTP Core | AI service communication through the application dependencies |
| Git | Version control |
| GitHub | Source code hosting |

> The exact AI integration and dependency configuration are defined in the project's application and dependency files.

---

## 📂 Project Structure

```text
yoga-ai-assistant/
│
├── fuzzy_logic/
│   ├── membership.py
│   ├── experience.py
│   ├── rules.py
│   ├── output.py
│   ├── inference.py
│   └── routine.py
│
├── app.py
├── app_logic.py
├── .gitignore
├── README.md
└── .venv/
```

### Main Files

| File | Description |
|---|---|
| `app.py` | Streamlit user interface and application flow |
| `app_logic.py` | Processes user requirements and generates the yoga routine |
| `membership.py` | Defines fuzzy membership functions |
| `experience.py` | Handles experience-related fuzzy calculations |
| `rules.py` | Contains fuzzy inference rules |
| `output.py` | Defines output membership functions |
| `inference.py` | Performs fuzzy inference calculations |
| `routine.py` | Supports yoga routine selection |

---

## 🔄 Application Workflow

```text
User enters yoga requirements
            │
            ▼
Streamlit user interface
            │
            ▼
Process user input using AI
            │
            ▼
Extract user preferences
            │
            ▼
Fuzzy logic processing
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
Calculate routine intensity
            │
            ▼
Select suitable yoga routine
            │
            ▼
Display recommended poses
            │
            ▼
Display AI explanation
```

---

## 🧠 Fuzzy Logic Process

The fuzzy inference system uses user-related inputs to calculate an appropriate yoga intensity.

### Input Factors

- Available time.
- Yoga experience.

### Output Categories

- Gentle.
- Balanced.
- Active.

### Fuzzy Processing Steps

1. Calculate input membership values.
2. Evaluate fuzzy rules.
3. Perform Mamdani aggregation.
4. Apply centroid defuzzification.
5. Calculate the final intensity score.
6. Select an appropriate yoga routine.

The application also provides a fuzzy membership function chart for technical inspection.

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

### 5. Install Dependencies

If the project contains a `requirements.txt` file:

```bash
pip install -r requirements.txt
```

Otherwise, install the dependencies specified by the project configuration.

### 6. Configure the AI Service

Configure the required AI service credentials according to the implementation used in `app_logic.py`.

Do not commit API keys or other confidential credentials to GitHub.

### 7. Run the Streamlit Application

```bash
python -m streamlit run app.py
```

The application will open in your browser at a local Streamlit address, normally:

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

The application provides:

- Detected user experience.
- Available time.
- Preferred intensity.
- Number of recommended poses.
- Total routine duration.
- Selected yoga routine.
- Recommended yoga poses.
- Pose durations.
- Pose benefits.
- AI-generated explanation.
- Fuzzy intensity score.
- Fuzzy membership function chart.
- Fuzzy reasoning details.

---

## ⚠️ Safety Notice

The application provides general yoga suggestions and is not a replacement for professional medical advice or instruction.

Users should:

- Stop if they experience pain or discomfort.
- Practice within their individual limits.
- Consult a qualified yoga instructor or healthcare professional if they have health concerns or physical limitations.

---

## 🔧 Development Progress

- [x] Python project setup
- [x] Time membership functions
- [x] Experience membership functions
- [x] Fuzzy rule evaluation
- [x] Mamdani aggregation
- [x] Centroid defuzzification
- [x] Yoga routine selection
- [x] AI-based preference processing
- [x] AI-generated yoga routine
- [x] Streamlit user interface
- [x] Recommended yoga poses
- [x] Routine summary
- [x] Fuzzy intensity visualization
- [x] Fuzzy reasoning display
- [x] Reset functionality
- [x] API error handling
- [x] Timeout error handling
- [x] GitHub repository setup
- [ ] Additional testing
- [ ] Deployment
- [ ] Further UI improvements

---

## 🌱 Future Improvements

Potential future improvements include:

- User accounts and saved yoga routines.
- Routine history.
- More yoga poses and categories.
- Voice-based user input.
- Progress tracking.
- Improved routine personalization.
- Mobile-friendly enhancements.
- Automated testing.
- Cloud deployment.
- Additional AI service optimization.

---

## 👨‍💻 Author

**Neeraj Jaiswar**

BSc Information Technology

GitHub: [neeraj01J](https://github.com/neeraj01J)

---

## 📄 License

This project is developed for educational and academic purposes.