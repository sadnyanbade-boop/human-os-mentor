import streamlit as st
import warnings
warnings.filterwarnings("ignore")

# Import our custom modules (Ensure data.py and brain.py are in your GitHub)
import data
import brain

# --- 1. PAGE SETUP ---
st.set_page_config(
    page_title="Human OS: Maharashtra Mentor",
    page_icon="🧬",
    layout="wide"
)

# --- 2. CSS STYLING (Smart Stealth Mode) ---
st.markdown("""
<style>
    /* 1. HIDE GITHUB ICON & DEPLOY BUTTON ONLY */
    /* This removes the code links but keeps the top bar functional for mobile */
    .stDeployButton {display:none;}
    [data-testid="stHeader"] [data-testid="stToolbar"] {display:none;}
    
    /* 2. HIDE MENU & FOOTER */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}

    /* 3. MOBILE SIDEBAR OPTIMIZATION */
    /* Ensures the sidebar ☰ button is accessible on small screens */
    [data-testid="stSidebarNav"] {margin-top: -50px;}

    /* 4. CHAT BUBBLES STYLING */
    .user-msg {
        background-color: rgba(0, 255, 128, 0.1);
        border: 1px solid rgba(0, 255, 128, 0.4);
        padding: 15px; border-radius: 15px 15px 0px 15px;
        margin: 10px 0; text-align: right;
    }
    .bot-msg {
        background-color: rgba(128, 128, 128, 0.1);
        border: 1px solid rgba(128, 128, 128, 0.2);
        padding: 15px; border-radius: 15px 15px 15px 0px;
        margin: 10px 0; text-align: left;
        border-left: 4px solid #4CAF50;
    }
    
    /* 5. DIAGRAM CARD STYLING */
    div[data-testid="stImage"] {
        background-color: white; padding: 20px; border-radius: 10px;
        margin: 10px 0; box-shadow: 0px 4px 6px rgba(0,0,0,0.1); display: inline-block;
    }
    
    /* 6. BUTTON STYLING */
    .stButton>button {
        border-radius: 8px; min-height: 3em; height: auto;
        white-space: normal;
    }
</style>
""", unsafe_allow_html=True)

# --- 3. SIDEBAR (Navigation & Controls) ---
with st.sidebar:
    st.markdown("<h1 style='text-align: center;'>🧬</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center;'>Human OS</h3>", unsafe_allow_html=True)
    st.divider()
    
    # Language Selection
    language_mode = st.radio("🗣️ Language", ["English", "Semi-English (Hinglish)", "Marathi (पूर्ण मराठी)"])
    
    st.subheader("📚 Syllabus")
    # Dynamic Dropdowns fetching from your data.py
    selected_class = st.selectbox("Class", list(data.MAHARASHTRA_SYLLABUS.keys()))
    selected_subject = st.selectbox("Subject", list(data.MAHARASHTRA_SYLLABUS[selected_class].keys()))
    selected_chapter = st.selectbox("Chapter", data.MAHARASHTRA_SYLLABUS[selected_class][selected_subject])
    
    st.divider()
    enable_audio = st.toggle("🔊 Audio Mode", value=True)

# --- 4. MAIN INTERFACE ---
subject_icon = "🧪" if "Science" in selected_subject else "📐"
st.title(f"{subject_icon} {selected_subject}")
st.caption(f"**Chapter:** `{selected_chapter}`")

# Initialize Session States
if "messages" not in st.session_state: st.session_state.messages = []
if "current_chapter" not in st.session_state: st.session_state.current_chapter = selected_chapter

# Clear chat if user switches chapters
if st.session_state.current_chapter != selected_chapter:
    st.session_state.messages = []
    st.session_state.current_chapter = selected_chapter

# Display History
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.markdown(f'<div class="user-msg"><b>You:</b><br>{msg["content"]}</div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="bot-msg"><b>Mentor:</b><br>{msg["content"]}</div>', unsafe_allow_html=True)
        if msg.get("image"): st.image(msg["image"], width=400)
        if msg.get("audio"): st.audio(msg["audio"], format='audio/mp3')

# Quick Concept Buttons (Appears only on empty chat)
if len(st.session_state.messages) == 0:
    st.markdown("### 🔥 Key Concepts / महत्त्वाचे मुद्दे")
    q_lang_key = "English" 
    class_concepts = data.IMPORTANT_CONCEPTS.get(q_lang_key, {})
