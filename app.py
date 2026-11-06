import streamlit as st
from google import genai
from pypdf import PdfReader
from io import BytesIO
from datetime import datetime
import time


# =======================
# 1. PAGE CONFIGURATION
# =======================

st.set_page_config(
    page_title="StudyMate AI",
    page_icon="✌",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =======================
# 2. SESSION STATE
# =======================

default_values = {
    "study_goal": 5,
    "completed_tasks": 0,
    "completed_questions": 0,
    "notes": [],
    "tasks": [],
    "user_name": "",
    "chat_history": [],
    "pdf_text": "",
    "pdf_name": "",
    "daily_goal": "",
    "practice_answer": None
}

for key, value in default_values.items():
    if key not in st.session_state:
        st.session_state[key] = value

# =======================
# 3. GEMINI CONFIGURATION
# =======================

def get_gemini_client():

    try:
        api_key = st.secrets["GEMINI_API_KEY"]

        client = genai.Client(api_key=api_key)

        return client
    except Exception:
        return None

# =======================
# 4.GLOBAL CSS
# =======================

st.markdown(
    """
    <style>
    /* Global background */

    .stApp {
        background-color: #F7F9FC;
        color: #344054;
    }

    /* Main content */

    .block-container {
        max-width: 1400px;
        padding-top: 2.5rem;
        padding-bottom: 4rem;
    }

    /* Sidebar */

    [data-testid="stSidebar"] {
        background: #FFFFFF;
        border-right: 1px solid #E9EEF5;
    }

    [data-testid="stSidebar"] * {
        color: #344054;
    }

    [data-testid="stSidebar"] {
        min-width: 290px !important;
    }
    

   
       

    /* Titles */

    .main-title {
        font-size: 38px;
        font-weight: 800;
        color: #26364B
        letter-spacing: -1px;
        margin-bottom: 8px;
    }

    .subtitle {
        font-size: 15px;
        color: #8A96A8
        margin-bottom: 28px;
    }

    /* Gradient text */

    .gradient-text {
        background: linear-gradient(90deg, #72A9E8, #82CDB7);
        -webkit-background-clip: text;
        webkit-text-fill-color: transparent;
    }

    /* Hero card */

    .hero-card {
        background: linear-gradient(
            115deg,
            #DCEBFA 0%,
            #E7F1FA 50%,
            #DDF2EA 100%
        );
        border-radius: 24px;
        padding: 38px 40px;
        margin-bottom: 30px;
        boeder: 1px solid #E3EDF5;
    }

    .hero-label {
        color: #6687A5
        font-size: 12px;
        font-weight: 700;
        letter-spacing: 2px;
        margin-bottom: 12px;
    }

    .hero-heading {
        font-size: 36px;
        font-weight: 800;
        color: #304B68;
        line-height: 1.25;
        margin-bottom: 12px;
    }

    .hero-description {
        font-size: 15px;
        color: #607D98;
        line-height: 1.7;
    }

    /* Section heading */

    .section-heading {
        color: #344054;
        font-size: 21px;
        font-weight: 750;
        margin-top: 28px;
        margin-bottom: 16px;
    }

    /* Metric cards */

    .metric-card {
    background: #FFFFFF;
    border: 1px solid #EDF0F5;
    border-radius: 18px;
    padding: 22px;
    min-height: 130px;
    box-shadow: 0 5px 18px rgba(50, 70, 100, 0.04);
    }

    .metric-label {
        color: #8A96A8;
        font-size: 12px;
        font-weight: 800;
    }

    .metric-value{
        color: #344054;
        font-size: 30px;
        font-weight: 800;
    }

    .metric-caption {
        color: #A0AABA;
        font-size: 12px;
        margin-top: 5px;
    }

    /* Feature cards */

    .feature-card {
        background: #FFFFFF;
        border: 1px solid #EDF0F5;
        border-radius: 18px;
        padding: 24px;
        min-height: 180px;
        box-shadow: 0 5px 18px rgba(50, 70, 100, 0.04);
    }

    .feature-icon {
        font-size: 30px;
        margin-bottom: 14px;
    }

    .feature-title {
        color: #344054
        font-size: 17px;
        font-weight: 750;
        margin-bottom: 9px;
    }

    .feature-description {
        color: #8A96A8;
        font-size: 13px;
        line-height: 1.7;
    }

    /* Inputs */

    .stTextInput input,
    .stTextArea textarea {
        background-color: #FFFFFF !important;
        color: #344054 !important;
        border: 1px solid #DFE7F0 !important;
        border-radius: 10px !important;
    }

    /* Buttons*/

    .stButton button {
        background: linear-gradient(90deg, #82AFE5, #8BCDB7);
        color: #FFFFFF;
        border: none;
        border-radius: 10px;
        padding: 8px 20px;
        font-weight: 700;
        transition: 0.2s;
    }

    /* Progress bar */

    .stProgress > div > div > div {
        background: linear-gradient(90deg, #8BBCEB, #A8DCC5);
    }

    /* File uploader */

    [data-testid="stFileUploader"] {
        background: #FFFFFF;
        border: 1px dashed #B8D3E8;
        border-radius: 15px;
        padding: 15px;
    }

    /* Footer */

    .footer{
        color: #A3ADBC;
        text-align: center;
        font-size: 12px;
        margin-top: 55px;
    }

    </style>
    """,
    unsafe_allow_html=True
)

# ============================
# 5. SIDEBAR NAVIGATION
# ============================

with st.sidebar:

    st.markdown("# ✌ StudyMate")

    st.caption("AI Learning Workspace")

    st.divider()

    st.markdown("### WORKSPACE")
        
    page = st.radio(
        "Navigation",
        [
            "㊣ Dashboard",
            "✍ Knowledge Hub",
            "☃ AI Learning",
            "♬ Practice Lab",
            "▦ Learning Analytics",
            "㉿ My Library"
        ],
        label_visibility="collapsed"
    )
    
        

    st.divider()

    subject = st.selectbox(
        "✌ Current Subject",
        [
           "VWL",
           "Mathematik",
           "Deutsch",
           "English"
       ]   
    )

    st.divider()

    st.caption("YOUR PERSONAL LEARNING SPACE")
    st.caption("Learn at your own space.")
    st.caption("StudyMate AI © 2026")

#==================================
# 6. Dashboard
#==================================
if page == "㊣ Dashboard":
    st.markdown(
        """
    <div class="main-title">
           Good to see you! 
           <span class="gradient-text"> ☁ </span>
       </div>

       <div class="subtitle">
           A little progress each day adds up to big results.
       </div>
       """, 
       unsafe_allow_html=True
    )

    st.markdown(
        """
<div class="hero-card">
<div class="hero-label">YOUR PERSONAL SPACE</div>
<div class="hero-heading">Learn at your own pace.<br>Grow every day.</div>
<div class="hero-description">Organize your knowledge, practice new skills,and keep track of your learning journey.</div>
</div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-heading">Your Overview</div>',
        unsafe_allow_html=True
    )

    col1, col2,col3, col4 = st.columns(4)

    with col1:

        st.metric(
            "★ SAVED NOTES",
            len(st.session_state.notes)
        )

    with col2:

        st.metric(
            "♣ QUESTIONS DONE",
            st.session_state.completed_questions
        )

    with col3:

        st.metric(
           "❁ DAILY GOAL",
           f"{st.session_state.completed_tasks}/{st.session_state.study_goal}" 
        )

    with col4:

        st.metric(
            "✌ CURRENT SUBJECT",
            subject
        )

    st.markdown("---")
    st.markdown("### Explore Your Workplace")

    f1, f2, f3 = st.columns(3)

    with f1:
        st.markdown(
            """
            <div class="feature-card">
                <div class="feature-icon">✍</div>
                <div class="feature-title">Knowledge Hub</div>
                <div class="feature-description">
                    Save your notes and organize everything you learn.
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with f2:
        st.markdown(
            """
            <div class="feature-card">
                <div class="feature-icon">☃</div>
                <div class="feature-title">AI Learning</div>
                <div class="feature-description">
                    Ask questions and understand difficult concepts.
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with f3:
        st.markdown(
            """
            <div class="feature-card">
                <div class="feature-icon">▦</div>
                <div class="feature-title">Learning Analytics</div>
                <div class="feature-description">
                    Track your progress and celebrate every achievement.
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown("---")

    st.markdown("### ۞ Set Your DAILY GOAL")

    new_goal = st.number_input(
        "How much study tasks would you like to complete?",
        min_value=1,
        max_value=20,
        value=st.session_state.study_goal
    )

    if st.button("Update Goal"):

      st.session_state.study_goal = new_goal
      st.success("Your daily goal has been updated")
      st.rerun()

#============================
# 7. KNOWLEDGE HUB
#============================

elif page == "✍ Knowledge Hub":

    st.markdown(
        """
        <div class="main-title">
            Knowledge <span class="gradient-text">Hub.</span>
        </div>

        <div class="subtitle">
            Collect ideas. Build your knowledge.
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("### ★ Create a New Note")

    note_subject = st.selectbox(
        "Choose a subject",
        [
            "VWL",
            "Mathematik",
            "Deutsch",
            "English"
        ]
    )

    note_title = st.text_input(
        "Note title",
        placeholder="e.g. Introduction to Elasticity",
    )

    note_content = st.text_area(
        "Your notes",
        placeholder="Write down the key concepts here...",
        height=200
    )

    if st.button("+ Save Note"):

         if note_title.strip() and note_content.strip():

             st.session_state.notes.append(
                 {
                     "subject": note_subject,
                     "title": note_title,
                     "content": note_content,
                     "date": datetime.now().strftime("%Y-%m-%d %H:%M")
                 }
             )

             st.success("Note saved successfully!")
             st.rerun()

         else:
             st.warning("Please enter both a title and note content.")
             
    st.markdown("---")

    st.markdown("### ✉ Your Knowledge Collection")

    if st.session_state.notes:
        for note in reversed(st.session_state.notes):

            with st.expander(
                f"✌ {note['title']} · {note['subject']}"
            ):

               st.write(note["content"])
               st.caption(f"Created: {note['date']}")
    else:
        st.info("Your knowledge collection is empty. Create your first note!")
 #===============================
 # 8. AI Learning
 # ===============================
           
elif page == "☃ AI Learning":

     st.markdown(
         """
<div class="main-title">
    AI <span class="gradient-text">Learning.</span>
</div>
<div class="subtitle">
    Your Personal AI learning assistant.
</div>
<div class="hero-card">
    <div class="hero-label">POWERED BY GEMINI AI</div>
    <div class="hero-heading">
        Ask. Understand.<br>
        Learn smarter.
    </div>
    <div class="hero-description">
        Ask questions about your subjects
        and get explanations from AI.
    </div>
</div>
         """,
         unsafe_allow_html=True
     )

     client = get_gemini_client()

     if client is None:

         st.error(
             "Gemini API connection unavailable."
             "Please check your Streamlit Secrets configuration."
         )

     else:

         st.success("Gemini AI is connected.")

         st.markdown(f"### Current Subject: {subject}")

         use_pdf = st.checkbox(
             "Use my uploaded PDF as learning context",
             value=bool(st.session_state.pdf_text)
         )

         user_question = st.text_area(
             "What would you like to ask?",
             placeholder="For example: Explain price elasticity of demand...",
             height=130
         )

         if st.button("Ask StudyMate AI"):
             
             if not user_question.strip():
                 
                 st.warning("Please enter your question.")

             else:

                 with st.spinner("StudyMate AI is thinking..."):

                    models =[
                        "gemini-3.8-flash",
                        "gemini-3.5-flash-lire"
                    ]

                    response = None

                    for model_name in models:
                        for attempt in range(2):
                            try:
                                response = client.models.generate_content(
                                    model=model_name,
                                    contents=user_question
                                )
                                break

                            except Exception as e:
                                error_message = str(e)

                                if "503" in error_message or "UNAVAILABLE" in error_message:
                                    time.sleep(2 * (attempt + 1))
                                    continue

                                break
                 if response is None:
                        st.error("AI is temporarily unavailable. Please try again later.")
                 else:
                      st.write(response.text)
                        
    
         if st.session_state.chat_history:

            st.markdown("---")

            st.markdown("### Conversation History")

            for chat in reversed(st.session_state.chat_history):

                with st.expander(chat["question"]):

                    st.markdown(chat["answer"])

            if st.button("Clear Concersation:"):

                st.session_state.chat_history = []

                st.rerun()

# =========================
# 9. PRACTICE LAB
# =========================

elif page == "♬ Practice Lab":

    st.markdown(
        """
        <div class="main-title">
            Practice <span class="gradient-text">Lab.</span>
        </div>

        <div class="subject">
            Challenge yourself. Turn knowledge into skills.
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="hero-card">
            
            <div class="hero-label">
                YOUR PERSONAL PRACTICE SPACE
            </div>

            <div class="hero-heading">
                Practice makes progress.
            </div>

            <div class="hero-description">
                Test your knowledge and learn from your mistakes.
            </div>

        <div>
        """,
        unsafe_allow_html=True
    )

    practice_subject = st.selectbox(
        "Select a subject",
        [
            "VWL",
            "Mathematik",
            "Deutsch",
            "English"
        ]
    )

    if practice_subject == "VWL":

        st.markdown("### Sample Question")

        st.write(
            "**What does price elasticity of demand measure?**"
        )

        answer = st.radio(
            "Choose your answer:",
            [
                "The change in supply caused by income",
                "The responsiveness of quantity demanded to a price change",
                "The total revenue of a company",
                "The production cost of a product"
            ],
            index=None,
            key="vwl_sample_answer"
        )

        if st.button("Check answer"):

            if answer is None:

                st.warning("Please select an answer.")

            elif answer == "The responsiveness of quantity demanded to a price change":

                st.success("Correct! Well done!")

                st.session_state.completed_questions += 1

            else:

                st.error(
                    "Not quite! Price elasticity measures"
                    "how strongly quantity demanded reacts to a price change."
                )

        else:

            st.info(
                "More practice questions for this subject will be added soon."
            )

        st.markdown("---")

        st.markdown("### AI Question Generator")

        st.write(
            "Generate practice questions based on your uploaded learning material."
        )

        if st.button("Generate Questions with AI"):

            client = get_gemini_client()

            if not st.session_state.pdf_text:

                st.warning("Please upload a PDF in My Library first.")
            elif client is None:

                st.error("Gemini connection unavailable")

            else:

                with st.spinner("Generating questions..."):

                    try:

                        prompt = f"""
                        Based on the following study material,
                        create 5 practice questions.

                        Subject: {practice_subject}

                        Include:
                        1. Multiple choice questions
                        2. Correct answers
                        3. Short explanations

                        Study material:

                        {st.session_state.pdf_text[:25000]}  
                        """

                        response = client.models.generate_content(
                            model="gemini-3.8-flash",
                            contents=prompt
                        )

                        st.sessin_state.generated_questions = response.text

                    except Exception as e:

                        st.error(f"Generation failed: {e}")

        if "generated_questions" in st.session_state:

            st.markdown("### Generated Practice Questions")

            st.markdown(st.session_state.generated_questions)

                
# =============================
# 10. LEARNING ANALYTICS
# =============================

elif page == "▦ Learning Analytics":

    st.markdown(
        """
        <div class="main-title">
            Learning <span class="gradient-text">Analytics.</span>
            </div>
            <div class="subtitle">
                Every small step takes you closer to your goals.
        </div>
        """,
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)

    with col1:

        st.metric(
            "COMPLETED QUESTIONS",
            st.session_state.completed_questions
        )
        
    with col2:

        st.metric(
            "SAVED NOTES",
            len(st.session_state.notes)
        )
            
    st.markdown("---")

    st.markdown("### ۞ Daily Progress")

    progress = min(
        st.session_state.completed_tasks / st.session_state.study_goal,
        1.0
    )

    st.progress(progress)

    st.write(
        f"{st.session_state.completed_tasks} of "
        f"{st.session_state.study_goal} tasks completed."
    )

    if st.button("+ Complete One Study Task"):

        if st.session_state.completed_tasks < st.session_state.study_goal:

            st.session_state.completed_tasks += 1
            st.rerun()

        else:
            st.success("Daily goal achieved! Great work!")

        st.markdown("---")

        st.markdown("### Your Learning Summary")

        st.write(f"✌ Total notes: {len(st.session_state.notes)}")

        st.write(
            f"★ Questions completed:"
            f"{st.session_state.completed_questions}"
        )

        st.write(
            f"❁ Study tasks completed:"
            f"{st.session_state.completed_tasks}"
        )

# ====================================
# 11. My Library
# ====================================

elif page == "㉿ My Library":

    st.markdown(
        """
        <div class="main-title">
            My <span class="gradient-text">Library.</span>
        </div>

        <div class="subtitle">
            All your learning materials, in one place.
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="metric-card">
  
            <div class="hero-label">
                YOUR PERSONAL RESOURCE CENTER
            </div>

            <div class="hero-heading">
                Your materials.<br>
                Your Knowledge.
            </div>

            <div class="hero-description">
                Upload your learning materials and prepare them
                for future AI-powered analysis.
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("### ☂ Upload Learning Materials")

    uploaded_file = st.file_uploader(
        "Choose a PDF file",
        type=["pdf"]
    )

    if uploaded_file is not None:

        try:

            pdf = PdfReader(
                BytesIO(uploaded_file.getvalue())
            )

            text_content = ""

            for page in pdf.pages:

                page_text = page.extract_text() or ""

                text_content += page_text + "/n"

            st.session_state.pdf_text = text_content

            st.session_state.pdf_name = uploaded_file.name

            st.success(
                f"Successfully uploaded: {uploaded_file.name}"
            )

            col1, col2 = st.columns(2)

            with col1:

                st.metric(
                    "Total Pages",
                    len(pdf.pages)
                )

            with col2:

                st.metric(
                    "Characters",
                    len(text_content)
                )

            st.markdown("---")

            st.markdown("### Extracted PDF Content")

            if text_content.strip():

                st.text_area(
                    "PDF Text",
                    value=text_content,
                    height=350
                )

            else:

                st.warning(
                    "Your PDF is ready for AI analysis!"
                )

        except Exception as e:

            st.error(f"Could not PDF: {e}")

    elif st.session_state.pdf_name:

        st.info(
            f"Previously uploaded PDF:{st.session_state.pdf_name}"
        )

        st.write(
            "The extracted text is available during this session."
        )

        if st.button("Remove Uploaded Material"):

            st.session_state.pdf_text = ""

            st.session_state.pdf_name = ""

            st.rerun()

# =======================
# 12. Footer
# =======================

st.markdown(
    """
    <div class="footer">
        STUDYMATE AI · MADE FOR CURIOUS MINDS
    </dic>
    """,
    unsafe_allow_html=True
)



    

