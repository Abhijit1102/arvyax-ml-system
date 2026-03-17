# 🌿 ArvyaX ML System — From Understanding Humans → To Guiding Them

## 🧠 Overview

This project builds an intelligent system that goes beyond prediction.
It **understands emotional signals, reasons under uncertainty, and guides users toward better mental states.**

The system processes:

- Short, noisy user reflections
- Contextual signals (sleep, stress, energy, time, etc.)

And produces:

- Emotional understanding
- Actionable decisions (what to do + when)
- Confidence + uncertainty awareness

---

## 🎯 Objectives

### 1. Emotional Understanding

- Predict:
  - `emotional_state` (classification)
  - `intensity` (regression / ordinal classification)

---

### 2. Decision Engine (Core)

The system decides:

- **What to do** (e.g., breathing, journaling, rest, deep work)
- **When to do it**:
  - `now`
  - `within_15_min`
  - `later_today`
  - `tonight`
  - `tomorrow_morning`

---

### 3. Uncertainty Awareness

Each prediction includes:

- `confidence` score (0–1)
- `uncertain_flag` (0 or 1)

---

### 4. (Optional) Supportive Guidance

Human-like message to guide users toward a better state.

---

## 📂 Project Structure

```
arvyax-ml-system/
│
├── data/                  # raw + processed datasets
├── notebooks/             # EDA & experiments
├── src/                   # core ML pipeline
│   ├── data/              # preprocessing
│   ├── features/          # feature engineering
│   ├── models/            # ML models
│   ├── decision/          # WHAT + WHEN logic
│   ├── uncertainty/       # confidence handling
│   ├── evaluation/        # ablation + error analysis
│   ├── inference/         # end-to-end pipeline
│
├── models/                # saved models
├── outputs/               # predictions.csv
├── docs/                  # reports (error, edge plan)
├── api/                   # (optional FastAPI)
├── run_pipeline.py        # main entry point
└── requirements.txt
```

---

## ⚙️ Setup Instructions

### 1. Clone Repository

```bash
git clone https://github.com/Abhijit1102/arvyax-ml-system.git
cd arvyax-ml-system
```

### 2. Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🚀 How to Run

### Run Full Pipeline

```bash
python run_pipeline.py
```

This will:

- Load data
- Preprocess inputs
- Train models
- Generate predictions
- Save output to:

```
outputs/predictions.csv
```

---

## 🧪 Approach

### 🔹 Feature Engineering

**Text Features**

- TF-IDF vectorization
- Handles short and noisy reflections

**Metadata Features**

- sleep_hours
- stress_level
- energy_level
- time_of_day
- previous_day_mood

---

### 🔹 Model Design

| Task            | Approach                            |
| --------------- | ----------------------------------- |
| Emotional State | Classification (Logistic / XGBoost) |
| Intensity       | Regression / Ordinal Classification |

---

### 🔹 Decision Engine (Key Differentiator)

Rule-based + contextual logic using:

- predicted state
- intensity
- stress
- energy
- time of day

Example:

```python
if stress > 7 and intensity >= 4:
    action = "box_breathing"
    when = "now"
elif energy < 3:
    action = "rest"
    when = "within_15_min"
```

---

### 🔹 Uncertainty Modeling

- Confidence = max class probability
- Threshold-based uncertainty flag

```python
uncertain_flag = 1 if confidence < 0.6 else 0
```

---

## 📊 Ablation Study

We compare:

- Text-only model
- Metadata-only model
- Combined model

👉 Result: **Text + metadata performs best** due to contextual grounding.

---

## ❌ Error Analysis

Detailed in:

```
docs/ERROR_ANALYSIS.md
```

Focus areas:

- Ambiguous text
- Conflicting signals
- Very short inputs
- Noisy labels

---

## 📱 Edge / Mobile Deployment

Explained in:

```
docs/EDGE_PLAN.md
```

Key considerations:

- Lightweight models (TF-IDF + Logistic Regression)
- Low latency inference
- On-device execution

---

## 🛡️ Robustness

Handles:

- Short text (“ok”, “fine”) → fallback logic
- Missing values → imputation
- Contradictions → uncertainty flag

---

## 📤 Output Format

```
id | predicted_state | predicted_intensity | confidence | uncertain_flag | what_to_do | when_to_do
```

---

## 🧩 Tech Stack

- Python
- scikit-learn
- XGBoost
- Pandas / NumPy
- (Optional) FastAPI

---

## 💡 Key Strengths

- Handles **real-world messy data**
- Combines **ML + reasoning**
- Includes **decision-making layer**
- Explicit **uncertainty awareness**
- Strong focus on **error analysis**

---

## 🚀 Future Improvements

- Replace TF-IDF with lightweight embeddings
- Learn decision engine via reinforcement learning
- Add conversational agent (SLM)
- Personalization over time

---

## 🌱 Philosophy

AI should not just understand humans.
It should **help them move toward a better state.**

---

## 👨‍💻 Author

Abhijit Rajkumar
AI/ML & Full-Stack Developer

---
