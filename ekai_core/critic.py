def critique_project(description):
    text = description.lower()

    code_quality = 50
    architecture = 50
    ml_depth = 40
    documentation = 45

    strengths = []
    weaknesses = []
    suggestions = []

    if "clean" in text or "modular" in text:
        code_quality += 20
        strengths.append("Clean and modular code structure.")

    if "architecture" in text or "design" in text:
        architecture += 20
        strengths.append("Thoughtful architecture design.")

    if "machine learning" in text or "ml" in text or "model" in text:
        ml_depth += 30
        strengths.append("Uses machine learning effectively.")
    else:
        weaknesses.append("ML usage is unclear or shallow.")
        suggestions.append("Clearly explain ML models and evaluation.")

    if "readme" in text or "documentation" in text:
        documentation += 25
        strengths.append("Good documentation provided.")
    else:
        weaknesses.append("Documentation is weak or missing.")
        suggestions.append("Add a clear README with setup and results.")

    overall = int((code_quality + architecture + ml_depth + documentation) / 4)

    if overall >= 75:
        confidence = "High"
    elif overall >= 55:
        confidence = "Medium"
    else:
        confidence = "Low"

    return (
        overall,
        code_quality,
        architecture,
        ml_depth,
        documentation,
        confidence,
        strengths,
        weaknesses,
        suggestions,
    )
