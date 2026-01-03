import streamlit as st
import warnings
warnings.filterwarnings("ignore")

# Import our custom modules
import data
import brain

# --- 1. PAGE SETUP ---
st.set_page_config(
    page_title="Human OS: Maharashtra Mentor",
    page_icon="🧬",
    layout="wide",
    # 'auto' is the most stable for phones; it shows on desktop and hides on mobile 
    # until the user needs it.
    initial_sidebar_state="auto" 
)

# --- 2. CLEAN UI STYLING ---
st.markdown("""
<style>
    /* HIDE ONLY THE FOOTER (Safe & Stable) */
    footer {visibility: hidden;}

    /* Professional Chat Bubble Styling */
    .user-msg {
        background-color: #f0f2f6;
        border-radius: 10px;
        padding: 15px;
        margin: 10px 0;
        border-right: 5px solid #4CAF50;
    }
    .bot-msg {
        background-color: #ffffff;
        border: 1px solid #e6e9ef;
        border-radius: 10px;
        padding: 15px;
        margin: 10px 0;
        border-left: 5px solid #2e7bcf;
    }
    
    /* Make the image container look like a card */
    div[data-testid="stImage"] {
        background-color: white; 
        padding: 10px; 
        border-radius: 10px;
        box-shadow: 0px 4px 6px rgba(0,0,0,0.1);
    }
</style>
""", unsafe_allow_html=True)

# --- 3. SIDEBAR (The Navigation Hub) ---
with st.sidebar:
    st.markdown("<h1 style='text-align: center;'>🧬 Human OS</h1>", unsafe_allow_html=True)
    st.divider()
    
    language_mode = st.radio("🗣️ Language", ["English", "Semi-English (Hinglish)", "Marathi (पूर्ण मराठी)"])
    
    st.subheader("📚 Syllabus Selection")
    selected_class = st.selectbox("Class", list(data.MAHARASHTRA_SYLLABUS.keys()))
    selected_subject = st.selectbox("Subject", list(data.MAHARASHTRA_SYLLABUS[selected_class].keys()))
    selected_chapter = st.selectbox("Chapter", data.MAHARASHTRA_SYLLABUS[selected_class][selected_subject])
    
    st.divider()
    enable_audio = st.toggle("🔊 Audio Mode", value=True)
    
    if st.button("🗑️ Reset Conversation", use_container_width=True):
        st.session_state.messages = []
        st.rerun()

# --- 4. MAIN INTERFACE ---
st.title(f"📖 {selected_subject}")
st.caption(f"**Chapter:** {selected_chapter}")

# Initialize Chat
if "messages" not in st.session_state: st.session_state.messages = []
if "current_chapter" not in st.session_state: st.session_state.current_chapter = selected_chapter

# Auto-reset if user changes chapter
if st.session_state.current_chapter != selected_chapter:
    st.session_state.messages = []
    st.session_state.current_chapter = selected_chapter

# Display History
for msg in st.session_state.messages:
    css_class = "user-msg" if msg["role"] == "user" else "bot-msg"
    label = "You" if msg["role"] == "user" else "Mentor"
    
    st.markdown(f'<div class="{css_class}"><b>{label}:</b><br>{msg["content"]}</div>', unsafe_allow_html=True)
    
    if msg.get("image"): st.image(msg["image"], width=400)
    if msg.get("audio"): st.audio(msg["audio"], format='audio/mp3')

# --- 5. INPUT & AI BRAIN ---
st.divider()
user_input = st.chat_input("Ask a doubt...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    with st.spinner("🧠 Thinking..."):
        ai_text = brain.get_ai_response(user_input, st.session_state.messages[:-1], selected_class, selected_subject, selected_chapter, language_mode)
        
        audio_data = None
        if enable_audio and "⚠️" not in ai_text:
            audio_data = brain.get_audio_bytes(ai_text, language_mode)
            
        diagram_url = brain.get_relevant_diagram(user_input)
        
        st.session_state.messages.append({
            "role": "assistant", 
            "content": ai_text, 
            "audio": audio_data, 
            "image": diagram_url
        })
    st.rerun()
