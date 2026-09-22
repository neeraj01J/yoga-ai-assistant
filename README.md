
# AI-Based Yoga Routine Selection Assistant

## Project Overview

The AI-Based Yoga Routine Selection Assistant is a mini project that recommends a suitable yoga routine based on the user's available time and yoga experience.

The project uses fuzzy logic to handle uncertain inputs and select an appropriate routine intensity.

## Features

- Fuzzy membership functions
- Experience and available-time analysis
- Fuzzy rule evaluation
- Mamdani aggregation
- Centroid defuzzification
- Automatic yoga routine selection
- Recommended yoga poses

## Technologies Used

- Python
- Fuzzy Logic
- LangChain (planned)
- Google Gemini (planned)
- Streamlit (planned)
- Git and GitHub

## Project Structure

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
├── main.py
├── .gitignore
└── README.md
```

## Current Progress

- [x] Python project setup
- [x] Time membership functions
- [x] Experience membership functions
- [x] Fuzzy rule evaluation
- [x] Mamdani aggregation
- [x] Centroid defuzzification
- [x] Yoga routine selection
- [ ] LangChain and Google Gemini integration
- [ ] Streamlit user interface
- [ ] Project deployment

## How to Run

### 1. Clone the Repository

```bash
git clone https://github.com/neeraj01J/yoga-ai-assistant.git
```

### 2. Open the Project Folder

```bash
cd yoga-ai-assistant
```

### 3. Activate the Virtual Environment

On Windows:

```powershell
.venv\Scripts\Activate.ps1
```

### 4. Run the Fuzzy Inference System

```bash
python fuzzy_logic/inference.py
```

## Current Output

The system calculates a defuzzified intensity score and selects a yoga routine based on the result.

## Author

Neeraj Jaiswar

BSc Information Technology