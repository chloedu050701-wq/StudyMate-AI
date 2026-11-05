import streamlit as st
if "study_goal" not in st.session_state:
    st.session_state.study_goal = 5
# Initialize session state variables
if "completed_tasks" not in st.session_state:
    st.session_state.completed_tasks = 0

if "total_tasks" not in st.session_state:
    st.session_state.total_tasks = 0

if "tasks" not in st.session_state:
    st.session_state.tasks = []

if "user_name" not in st.session_state:
    st.session_state.user_name = ""


# Intitialize session state variables
if "completed_quesstions" not in st.session_state:
    st.session_state.completed_questions = 0

if "total_questions" not in st.session_state:
    st.session_state.total_questions = 0

if "score" not in st.session_state:
    st.session_state.score = 0

if "current_question" not in st.session_state:
    st.session_state.current_question = 0

from datetime import datetime



practice_subject = st.session_state.get("practice_subject", "Economics")

# =======================
# 1. 页面设置
# =======================

st.set_page_config(
    page_title="StudyMate AI",
    page_icon="✌",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =======================
# 2. 初始化数据
# =======================

st.set_page_config(
    page_title="StudyMate AI",
    page_icon="✌",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =======================
# 3. 全局样式
# =======================

st.markdown(
    """
    <style>
    /* 整体背景 */
    .stApp {
        background-color: #F7F9FC;
        color: #344054;
    }

    /* 主内容区域 */
    .block-container {
        max-width: 1400px;
        padding-top: 2.5rem;
        padding-bottom: 4rem;
    }

    /* 隐藏顶部装饰 */
    [data-testid="stHeader"] {
        background: transparent;
    }

    /* 侧边栏 */
    [data-testid="stSidebar"] {
        background: #FFFFFF;
        border-right: 1px solid #E9EEF5;
    }

    [data-testid="stSidebar"] * {
        color: #344054;
    }

    /* 标题 */
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

    /* 渐变字体 */
    .gradient-text {
        background: linear-gradient(90deg, #72A9E8, #82CDB7);
        -webkit-background-clip: text;
        webkit-text-fill-color: transparent;
    }

    /* 首页欢迎卡片 */
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

    /* 区域标题 */
    .section-heading {
        color: #344054;
        font-size: 21px;
        font-weight: 750;
        margin-top: 28px;
        margin-bottom: 16px;
    }

    /* 数据卡片 */
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

    /* 功能卡片 */
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

    /* 输入框 */
    .stTextInput input,
    .stTextArea textarea {
        background-color: #FFFFFF !important;
        color: #344054 !important;
        border: 1px solid #DFE7F0 !important;
        border-radius: 10px !important;
    }

    .stTextInput input:focus,
    .stTextArea textarea:focus {
        border-color: #8BBCEB !important;
        box-shadow: 0 0 0 2px rgba(139, 188, 235, 0.15) !important;
    }

    /* 下拉框 */
    .stSelectbox div[data-baseweb="select"] {
        background-color: #FFFFFF !important;
        border-radius: 10px !important;
    }

    /* 按钮 */
    .stButton button {
        background: linear-gradient(90deg, #82AFE5, #8BCDB7);
        color: #FFFFFF;
        border: none;
        border-radius: 10px;
        padding: 8px 20px;
        font-weight: 700;
        transition: 0.2s;
    }

    /* 进度条 */
    .stProgress > div > div > div {
        background: linear-gradient(90deg, #8BBCEB, #A8DCC5);
    }

    /* 文件上传 */
    [data-testid="stFileUploader"] {
        background: #FFFFFF;
        border: 1px dashed #B8D3E8;
        border-radius: 15px;
        padding: 15px;
    }

    /* 分隔线 */
    hr{
       border-color: #E9EEF5;
    }

    /* 页脚 */
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
# 4.侧边栏
# ============================

with st.sidebar:

    st.markdown(
        """
       <div style="padding: 15px 5px 25px 5px;">
           <div style="font-size: 25px; font-weight: 850; color: #344054;">
                ✌ Study<span style="color:#80B9E8;">Mate</span>
           </div>
           <div style="font-size: 10px; letter-spacing: 2px; color:#9AA8B9;">
               YOUR PERSONAL LEARNING SPACE
    <div>
    """, 
    unsafe_allow_html=True
)

st.markdown("---")

st.markdown("##### WORKSPACE")

page = st.radio(
    "Navigation",
    [
        "㊣ Dashboard",
        "✍ Knowledge Hub",
        "☃ AI Practice Lab",
        "▦ Learning Analytics"
        "㉿ My Library"
    ],
    label_visibility="collapsed"
)

st.markdown("---")

st.markdown("##### ۞ DAILY GOAL")

st.write(
    f"{st.session_state.completed_tasks} / "
    f"{st.session_state.get('study_goal', 5)} tasks"
)

progressc= min(
    st.session_state.completed_tasks / st.session_state.study_goal,
    1.0
)

st.progress(progressc)

st.markdown("---")

st.caption("STUDYMATE AI · VERSION 0.1")

#==================================
# 5. Dashboard
#==================================
if page == "㊣ Dashboard":

    st.markdown(
        """
       <div class="main-title">
           Good to see you! <span class="gradient-text"> ☁ </span>
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
       <div class="hero-heading">
           Learn at your own pace.<br>
           Grow every day.
       </div>
       <div class="hero-description">
           Organize your knowledge, practice new skills,
           and keep track of your learning journey.
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
    st.markdown(
        """
       <div class="metric-card">
           <div class="metric-label">✍ SAVED NOTES</div>
           <div class="metric-value">{len(st.session_state.notes)}</div>
           <div class="metric-caption">Your Knowledge collection</div>
    </div>
    """,
    unsafe_allow_html=True
)

with col2:
    st.markdown(
        """
       <div class="metric-card">
            <div class="metric-label">☃ QUESTIONS DONE</div>
            <div class="metric-value">{len(st.session_state.completed_questions)}</div>
            <div class="metric-caption">Keep practicing!</div>
    </div>
    """,
    unsafe_allow_html=True
) 

with col3:
    st.markdown(
        """
       <div class="metric-card">
            <div class="metric-label">㉿ DAILY GOAL</div>
            <div class="metric-value">
                {st.session_state.completed_tasks}/{st.session_state.study_goal}
            </div>
            <div class="metric-caption">Tasks completed today</div>
    </div>
    """,
    unsafe_allow_html=True
) 

with col4:
    st.markdown(
        """
       <div class="metric-card">
            <div class="metric-label">books YOUR STATUS</div>
            <div class="metric-value" style="font-size:24px;">READY</div>
            <div class="metric-caption">Let's start learning</div>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    '<div class="section-heading">Explore Your Workspace</div>',
    unsafe_allow_html=True
)

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
                  <div class="feature-title">Practice Lab</div>
                  <div class="feature-description">
                      Test your knowledge and learn from your mistakes.
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
# 6. Knowledge Hub
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

    st.markdown("### ✪ Create a New Note")

    subject = st.selectbox(
        "Choose a subject",
        [
            "Economics",
            "Mathematics",
            "English",
            "German"
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

             st.session_state.notes.append({
                 "subject": subject,
                 "title": note_title,
                 "content": note_content,
                 "date": datetime.now().strftime("%Y-%m-%d %H:%M")
             })

             st.success("Note saved successfully!")
             st.rerun()

         else:
             st.warning("Please enter both a title and note content.")
             
    st.markdown("---")

    st.markdown("### ✉ Your Knowledge Collection")

    if st.session_state.notes:
        for note in reversed(st.session_state.notes):

            with st.expander(
                f"♟ {note['title']} · {note['subject']}"
            ):

               st.write(note["content"])
               st.caption(f"Created: {note['date']}")
    else:
        st.info("Your knowledge collection is empty. Create your first note!")
 #===============================
 # 7. AI Practice Lab
 # ===============================
           
elif page == "☃ AI Practice Lab":

     st.markdown(
         """
         <div class="main-title">
             Practice <span class="gradient-text">Lab.</span>
             </div>
             <div class="subtitle">
                 Challenge yourself. Turn knowledge into skills.
         </div>
         """,
         unsafe_allow_html=True
     )

     st.markdown(
         """
         <div class="hero-card">
             <div class="hero-label">YOUR PERSONAL SPACE</div>
             <div class="hero-heading">Practice makes progress.</div>   
             <div class="hero-description">
                 Start with sample questions. AI-powered exercises
                 will be introduced in a future version.
             </div>
         </div>
         """,
         unsafe_allow_html=True
     )

     practice_subject = st.selectbox(
         "Select a subject",
         ["Economics", "Accounting", "Business Studies"]
     )

if practice_subject == "Economics":

    st.markdown("### 〠 Sample Question")

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
        index=None
    )

    if st.button("Check answer"):

        if answer is None:
            st.warning("Please select an answer.")

        elif answer == "The responsiveness of quantity demanded to a price change":

            st.success("Correct! Well done! ☺")

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
# =============================
# 8. Learning Analytics
# =============================

elif page == "▦ Learning Analytics":

    st.markdown(
        """
        <div class="main-title">
            Practice <span class="gradient-text">Analytics.</span>
            </div>
            <div class="subtitle">
                Every small step takes you closer to your goals.
        </div>
        """,
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)

    with col1:
        st.markdown(
            """
            <div class="metric-card">
                <div class="metric-label">COMPLETED QUSTIONS</div>
                <div class="metric-value">{st.session_state.completed_questions}</div>
                <div class="metric-caption">Questions answered in this session</div>
        </div>
        """,
        unsafe_allow_html=True
    )

    with col1:
        st.markdown(
            """
            <div class="metric-card">
                <div class="metric-label">SAVED NOTES</div>
                <div class="metric-value">{len(st.session_state.notes)}</div>
                <div class="metric-caption">Questions answered in this session</div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("---")

    st.markdown("### ۞ Daily Progress")

    progress = min(
        st.session_state.completed_tasks / st.session_state.study_goal,
        1.0
    )

    st.progress(progressc)

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

# ====================================
# 9. My Library
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
            <div class="hero-label">YOUR PERSONAL RESOURCE CENTER</div>
            <div class="hero-heading">Your materials.<br>Your Knowledge.</div>   
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
        "Choose a PDF or TXT file",
        type=["pdf", "text"]
    )

    if uploaded_file is not None:

        st.success(f"File received: {uploaded_file.name}")

        st.info(
            "File upload is working. Automatic document reading "
            "and AI analysis will be added in a future update."
        )

# =======================
# 10. Footer
# =======================

st.markdown(
    """
    <div class="footer">
        STUDYMATE AI · MADE FOR CURIOUS MINDS
    </dic>
    """,
    unsafe_allow_html=True
)

# ==========================
# 11. PDF Upload & Reader
# ==========================

import streamlit as st
from pypdf import PdfReader
from io import BytesIO

st.markdown("---")

st.markdown(
    """
    <h2 style="color:#477C9B;">
        ㉿ My PDF Library
    </h2>
    <p style="color:#8296A8;">
        Upload your study materials and let StudyMate AI read them.
    </p>
    """,
    unsafe_allow_html=True
)

uploaded_pdf = st.file_uploader(
    "Upload your PDF study material",
    type=["pdf"],
    help="Choose a PDF file from your computer."
)

if uploaded_pdf is not None:

    try:
        pdf = PdfReader(BytesIO(uploaded_pdf.getvalue()))

        text_content = ""

        for page in pdf.pages:
            page_text = page.extract_text() or ""
            text_content += page_text + "/n"

        st.success("PDF uploaded successfully!")

        col1, col2 = st.columns(2)

        with col1:
           st.metric("Total Pages", len(pdf.pages0)) 

        with col2:
            st.metric("Characters", len(text_content))

        st.markdown("### ✉ Extracted Content")

        if text_content.strip():
            st.text_area(
                "PDF Text",
                value=text_content,
                height=400
            )
        else:
            st.warning(
                "No readable text found."
                "This PDF may contain scanned images."
            )
    except Exception as e:
        st.error(f"Could not rea PDF: {e}")




    

