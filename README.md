# SkillBridge AI 🚀
*Empowering underserved workers with instant, AI-verified hands-on skill portfolios.*

---

## 📌 Problem Statement & Solution
* **Problem:** Millions of individuals gain valuable vocational, technical, and hands-on skills through informal work or non-traditional routes. However, standard resume builders and job platforms rely heavily on written proficiency and formal degrees, leaving skilled blue-collar workers, craftspeople, and non-native speakers overlooked by hiring algorithms.
* **Solution:** **SkillBridge AI** allows users to record or upload a short video/audio demonstration of a practical task. Our multimodal AI engine analyzes the visual technique and spoken explanation, evaluates procedural safety and correctness, and instantly generates a professional, shareable micro-portfolio badge for employers.

---

## ⚙️ Technology Stack
* **Frontend / UI:** Python, Streamlit
* **AI Core:** Google Gemini 1.5 Pro (Multimodal Video & Task Rubric Analysis) / OpenAI API
* **Utilities:** Python `dotenv`, Pillow, MoviePy (for video frame handling)
* **Deployment:** Streamlit Community Cloud

---

## 🏗️ AI Methodology and Implementation
1. **Multimodal Ingestion:** Users upload a video clip or audio recording explaining/demonstrating their hands-on task.
2. **Vision & Speech Evaluation:** 
   * **Gemini 1.5 Pro** processes the visual frames to verify tool usage, safety protocol adherence, and sequential step completion.
   * Structured system prompts enforce a strict grading rubric to ensure objective evaluation.
3. **Structured Portfolio Generation:** The AI extracts the core competency, difficulty level, and recommended job roles, outputting a clean professional JSON payload rendered as a digital credential badge.

---

## 🛠️ Setup and Installation Instructions

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/your-username/skillbridge-ai.git](https://github.com/your-username/skillbridge-ai.git)
   cd skillbridge-ai