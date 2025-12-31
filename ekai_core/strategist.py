def evaluate_idea(text):
    text = text.lower()

    viability = 50
    differentiation = 50
    resume_impact = 50
    verdict = "PIVOT ⚠️"

    do_next = []
    avoid = []

    if "chatbot" in text or "todo" in text:
        viability = 30
        differentiation = 20
        resume_impact = 25
        verdict = "KILL ❌"
        avoid.append("Do not build a generic chatbot or todo app.")
        do_next.append("Identify a niche, real-world problem instead.")

    if "ai" in text:
        viability += 20
        resume_impact += 15
        do_next.append("Clearly define the AI component and evaluation metrics.")

    if "agent" in text:
        differentiation += 25
        resume_impact += 20
        verdict = "BUILD ✅"
        do_next.append("Design the agent workflow and decision logic.")
        do_next.append("Show autonomy, not just responses.")

    if verdict == "PIVOT ⚠️":
        do_next.append("Refine the idea with a unique angle or target user.")
        avoid.append("Avoid adding features without a clear impact.")

    return verdict, viability, differentiation, resume_impact, do_next, avoid
