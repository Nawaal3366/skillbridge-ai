import streamlit as st
import google.generativeai as genai
from PIL import Image

# Page Configuration
st.set_page_config(
    page_title="SkillBridge AI - Micro-Skill Credentialing",
    page_icon="🛠️",
    layout="centered"
)

# Initialize Gemini API
api_key = "AIzaSyD8bEvphQJIf0hMrXLONzQNbAAfreMqn_s"

if api_key:
    genai.configure(api_key=api_key)

st.title("🛠️ SkillBridge AI")
st.subheader("Transforming hands-on practical experience into verified digital credentials.")

st.markdown("""
Welcome! Record or describe a practical task you know how to do (e.g., *electrical wiring repair, kitchen food safety protocol, bicycle brake replacement*), and our AI will evaluate your workflow, certify your skill, and generate a professional profile badge.
""")

st.divider()

with st.form("skill_form"):
    st.markdown("### 📝 Enter Your Task Details")
    user_name = st.text_input("Your Full Name", placeholder="e.g., Alex Johnson")
    skill_category = st.selectbox(
        "Select Domain",
        ["Electrical & Hardware", "Culinary & Food Safety", "Automotive / Mechanical", "General Construction & Craft", "Other"]
    )
    task_description = st.text_area(
        "Describe step-by-step how you perform this task:",
        placeholder="e.g., First, I shut off the main circuit breaker. Next, I test the wires with a multimeter to ensure zero voltage..."
    )
    
    uploaded_image = st.file_uploader("Upload Evidence Photo (Optional: tool setup, finished work, or certification)", type=["jpg", "jpeg", "png"])
    
    submitted = st.form_submit_button("Generate Verified Skill Badge 🚀", use_container_width=True)

if submitted:
    if not user_name or not task_description:
        st.warning("Please provide your name and task description to proceed.")
    elif not api_key:
        st.error("Gemini API Key is missing.")
    else:
        with st.spinner("Analyzing task safety, tool usage, and procedural correctness..."):
            try:
                model = genai.GenerativeModel('gemini-3.8-flash')
                
                prompt = f"""
                You are an expert vocational skills assessor and industry certification board.
                Evaluate the following task submission from a worker named {user_name} in the category '{skill_category}':
                
                Task Procedure described:
                "{task_description}"
                
                Please provide:
                1. Verified Skill Title (Professional naming)
                2. Competency Level (Beginner / Intermediate / Expert)
                3. Safety & Technique Score (Out of 100)
                4. Key Technical Strengths Identified
                5. A concise, professional micro-credential summary paragraph suitable for a resume or employer portfolio.
                """
                
                if uploaded_image:
                    image = Image.open(uploaded_image)
                    response = model.generate_content([prompt, image])
                else:
                    response = model.generate_content(prompt)
                
                st.success("🎉 Skill Verification Complete!")
                
                # Visual Results Section
                st.divider()
                st.markdown(f"## 🏆 Verified Credential: {user_name}")
                
                # Highlight Metrics in Columns
                col1, col2 = st.columns(2)
                with col1:
                    st.metric(label="Domain Category", value=skill_category)
                with col2:
                    st.metric(label="Verification Status", value="Verified ✅")
                
                # AI Report Output
                st.markdown(response.text)
                st.divider()
                st.info("💡 You can copy this badge report or share your portfolio link directly with prospective employers!")
                
            except Exception as e:
                st.error(f"An error occurred during AI evaluation: {e}")