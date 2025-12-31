import streamlit as st
from ekai_core.strategist import evaluate_idea
from ekai_core.critic import critique_project
from ekai_core.ai_explainer import explain_decision

# ================= SESSION STATE =================
if "history" not in st.session_state:
    st.session_state.history = []

# ================= HELPERS =================
def score_label(score):
    if score >= 80:
        return "Strong"
    elif score >= 60:
        return "Adequate"
    else:
        return "Weak"

# ================= GLOBAL CSS =================
st.markdown("""
<style>
html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

.ekai-card {
    background: #020617;
    padding: 1.3rem;
    border-radius: 14px;
    margin-bottom: 1.2rem;
    border: 1px solid #1e293b;
}

.badge-build { color: #22c55e; font-weight: 700; }
.badge-pivot { color: #facc15; font-weight: 700; }
.badge-kill  { color: #ef4444; font-weight: 700; }

section[data-testid="stSidebar"] {
    background: #020617;
    border-right: 1px solid #1e293b;
}
</style>
""", unsafe_allow_html=True)

# ================= HEADER =================
st.markdown("""
<h1 style="text-align:center;">
EKAI <span style="color:#2563eb;">| Engineering Knowledge & Intelligence Agent</span>
</h1>
<p style="text-align:center; color:#94a3b8;">
Autonomous engineering strategist & project critic
</p>
""", unsafe_allow_html=True)

st.divider()

# ================= SIDEBAR =================
with st.sidebar:
    st.markdown("## 🧠 EKAI Control Panel")

    mode = st.radio(
        "Mode",
        ["Idea Evaluation", "Project Critique"]
    )

    st.divider()
    st.caption("Session History")

    if st.session_state.history:
        for item in reversed(st.session_state.history[-3:]):
            st.write(f"• {item['type']} → {item['verdict']} | Score: {item['score']}")
    else:
        st.caption("No evaluations yet.")

# ================= IDEA EVALUATION =================
if mode == "Idea Evaluation":
    st.subheader("🧠 Idea Evaluation")
    st.caption("Evaluate an idea before investing time building it.")

    idea = st.text_area("Describe your project idea:")

    if st.button("Evaluate Idea"):
        if idea.strip() == "":
            st.warning("Please enter an idea first.")
        else:
            verdict, v, d, r, do_next, avoid = evaluate_idea(idea)
            avg_score = int((v + d + r) / 3)

            st.session_state.history.append({
                "type": "Idea",
                "verdict": verdict,
                "score": avg_score
            })

            st.markdown('<div class="ekai-card">', unsafe_allow_html=True)
            st.subheader("EKAI Strategic Evaluation")

            if "BUILD" in verdict:
                st.markdown(f"<p class='badge-build'>Verdict: {verdict}</p>", unsafe_allow_html=True)
            elif "PIVOT" in verdict:
                st.markdown(f"<p class='badge-pivot'>Verdict: {verdict}</p>", unsafe_allow_html=True)
            else:
                st.markdown(f"<p class='badge-kill'>Verdict: {verdict}</p>", unsafe_allow_html=True)

            st.divider()

            col1, col2, col3 = st.columns(3)
            col1.metric("Viability", f"{v} ({score_label(v)})")
            col2.metric("Differentiation", f"{d} ({score_label(d)})")
            col3.metric("Resume Impact", f"{r} ({score_label(r)})")

            st.divider()
            st.write("### 🧠 Decision Rationale")
            st.write(
                "EKAI assigned this verdict based on differentiation, "
                "practical viability, and resume impact."
            )

            # 🤖 AI EXPLANATION (CORRECTLY PLACED)
            st.write("### 🤖 AI Explanation")
            context = f"""
Idea Evaluation Summary:
Verdict: {verdict}
Viability Score: {v}
Differentiation Score: {d}
Resume Impact Score: {r}
"""
            with st.spinner("EKAI is generating an explanation..."):
                ai_text = explain_decision(context)
            st.info(ai_text)

            st.markdown('</div>', unsafe_allow_html=True)

            st.markdown('<div class="ekai-card">', unsafe_allow_html=True)
            st.write("### ✅ What to do next")
            for item in do_next:
                st.markdown(f"• {item}")

            if avoid:
                st.write("### ❌ What to avoid")
                for item in avoid:
                    st.markdown(f"• {item}")
            st.markdown('</div>', unsafe_allow_html=True)

# ================= PROJECT CRITIQUE =================
else:
    st.subheader("🔍 Project Critique")
    st.caption("Objective review of a completed project.")

    project_desc = st.text_area("Describe your project:")

    if st.button("Critique Project"):
        if project_desc.strip() == "":
            st.warning("Please describe the project first.")
        else:
            (
                overall,
                code_q,
                arch,
                ml,
                doc,
                confidence,
                strengths,
                weaknesses,
                suggestions,
            ) = critique_project(project_desc)

            st.session_state.history.append({
                "type": "Project",
                "verdict": confidence,
                "score": overall
            })

            st.markdown('<div class="ekai-card">', unsafe_allow_html=True)
            st.subheader("EKAI Project Review")

            st.metric("Overall Score", f"{overall} ({score_label(overall)})")
            st.write("**Confidence Level:**", confidence)

            st.divider()

            col1, col2, col3, col4 = st.columns(4)
            col1.metric("Code Quality", f"{code_q} ({score_label(code_q)})")
            col2.metric("Architecture", f"{arch} ({score_label(arch)})")
            col3.metric("ML Depth", f"{ml} ({score_label(ml)})")
            col4.metric("Documentation", f"{doc} ({score_label(doc)})")

            st.divider()
            st.write("### 🧠 Decision Rationale")
            st.write(
                "EKAI evaluated engineering structure, ML clarity, and documentation quality."
            )

            # 🤖 AI EXPLANATION (CORRECTLY PLACED)
            st.write("### 🤖 AI Explanation")
            context = f"""
Project Critique Summary:
Overall Score: {overall}
Confidence Level: {confidence}
Code Quality: {code_q}
Architecture: {arch}
ML Depth: {ml}
Documentation: {doc}
"""
            with st.spinner("EKAI is generating an explanation..."):
                ai_text = explain_decision(context)
            st.info(ai_text)

            st.markdown('</div>', unsafe_allow_html=True)

            st.markdown('<div class="ekai-card">', unsafe_allow_html=True)
            st.write("### ✅ Strengths")
            for s in strengths:
                st.markdown(f"• {s}")

            st.write("### ⚠️ Weaknesses")
            for w in weaknesses:
                st.markdown(f"• {w}")

            st.write("### 🎯 Strategic Improvements")
            for sug in suggestions:
                st.markdown(f"• {sug}")
            st.markdown('</div>', unsafe_allow_html=True)

# ================= ABOUT =================
st.divider()
with st.expander("About EKAI"):
    st.markdown("""
**EKAI (Engineering Knowledge & Intelligence Agent)** is a decision-first system
designed to evaluate engineering ideas and critique projects with senior-level judgment.

**Core Principles**
- Strategy before execution  
- Signal over noise  
- Honest, calm evaluation  
- Real-world engineering impact  

EKAI does not aim to impress — it aims to be correct.
""")
