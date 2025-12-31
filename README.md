# EKAI — Engineering Knowledge & Intelligence Agent

EKAI is a decision-first engineering strategist and project critic designed to
evaluate project ideas and critique completed projects with senior-level judgment.

The system separates deterministic logic from optional AI explanations to ensure
reliability, clarity, and graceful failure handling.

## Features

### 🧠 Idea Evaluation
- Build / Pivot / Kill verdict
- Viability, Differentiation, Resume Impact scores
- Clear decision rationale
- Actionable next steps
- Optional AI explanation (fails safely if unavailable)

### 🔍 Project Critique
- Overall project score with confidence level
- Code quality, architecture, ML depth, documentation scoring
- Strengths, weaknesses, and improvement suggestions
- Optional AI explanation layer

## Architecture Principles
- Rule-based core logic (deterministic and testable)
- AI used only for explanation, not decision-making
- Graceful degradation when AI is unavailable
- Modular and production-safe design

## Tech Stack
- Python
- Streamlit
- Modular architecture
- OpenAI-compatible LLM (optional)

## How to Run
```bash
pip install -r requirements.txt
streamlit run app.py
