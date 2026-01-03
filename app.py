# app.py
import streamlit as st
import warnings
warnings.filterwarnings("ignore")

# Import our custom modules
import data
import brain

# --- 1. PAGE SETUP ---
st.set_page_config(page_title="Human OS: Maharashtra Mentor", page_icon="🧬", layout="wide")

# --- 2. CSS STYLING ---
st.markdown("""
<style>
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
    div[data-testid="stImage"] {
        background-color: white; padding: 20px; border-radius: 10px;
        margin: 10px 0; box-shadow: 0px 4px 6px rgba(0,0,0,0.1); display: inline-block;
    }
    .stButton>button {
        border-radius: 8px; min-height: 3em; height: auto;
        white-space: normal;
    }
</style>
""", unsafe_allow_html=True)

# --- 3. SIDEBAR ---
with st.sidebar:
    st.markdown("<h1 style='text-align: center;'>🧬</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center;'>Human OS</h3>", unsafe_allow_html=True)
    st.divider()
    
    language_mode = st.radio("🗣️ Language", ["English", "Semi-English (Hinglish)", "Marathi (पूर्ण मराठी)"])
    
    st.subheader("📚 Syllabus")
    # Dynamic Dropdowns from data.py
    selected_class = st.selectbox("Class", list(data.MAHARASHTRA_SYLLABUS.keys()))
    selected_subject = st.selectbox("Subject", list(data.MAHARASHTRA_SYLLABUS[selected_class].keys()))
    selected_chapter = st.selectbox("Chapter", data.MAHARASHTRA_SYLLABUS[selected_class][selected_subject])
    
    st.divider()
    enable_audio = st.toggle("🔊 Audio Mode", value=True)

# --- 4. MAIN CHAT INTERFACE ---
subject_icon = "🧪" if "Science" in selected_subject else "📐"
st.title(f"{subject_icon} {selected_subject}")
st.caption(f"**Chapter:** `{selected_chapter}`")

# Initialize Chat
if "messages" not in st.session_state: st.session_state.messages = []
if "current_chapter" not in st.session_state: st.session_state.current_chapter = selected_chapter

# Clear chat if chapter changes
if st.session_state.current_chapter != selected_chapter:
    st.session_state.messages = []
    st.session_state.current_chapter = selected_chapter

# Display Chat History
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.markdown(f'<div class="user-msg"><b>You:</b><br>{msg["content"]}</div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="bot-msg"><b>Mentor:</b><br>{msg["content"]}</div>', unsafe_allow_html=True)
        if msg.get("image"): st.image(msg["image"], width=300)
        if msg.get("audio"): st.audio(msg["audio"], format='audio/mp3')

# Quick Topic Buttons
if len(st.session_state.messages) == 0:
    st.markdown("### 🔥 Key Concepts / महत्त्वाचे मुद्दे")
    q_lang_key = "English" # Default to English keys for button logic
    concepts = data.IMPORTANT_CONCEPTS.get(q_lang_key, {}).get(selected_chapter, data.IMPORTANT_CONCEPTS[q_lang_key]["default"])
    
    cols = st.columns(3)
    for i, concept in enumerate(concepts):
        if cols[i % 3].button(f"📌 {concept}", use_container_width=True, key=f"btn_{i}"):
            st.session_state.clicked_prompt = f"Explain {concept}"

# Input Area
st.divider()
user_input = None
if "clicked_prompt" in st.session_state and st.session_state.clicked_prompt:
    user_input = st.session_state.clicked_prompt
    st.session_state.clicked_prompt = None
else:
    user_input = st.chat_input("Ask a doubt here...")

# Process Input
if user_input:
    display_text = user_input.replace("Explain ", "")
    st.session_state.messages.append({"role": "user", "content": display_text})
    st.rerun()

# Generate AI Response
if st.session_state.messages and st.session_state.messages[-1]["role"] == "user":
    last_user_msg = st.session_state.messages[-1]["content"]
    
    with st.spinner("🧠 Thinking... Fetching Visuals... Recording Audio..."):
        # 1. Text Response
        ai_text = brain.get_ai_response(last_user_msg, st.session_state.messages[:-1], selected_class, selected_subject, selected_chapter, language_mode)
        
        # 2. Audio Generation
        audio_data = None
        if enable_audio and "⚠️" not in ai_text:
            audio_data = brain.get_audio_bytes(ai_text, language_mode)
        
        # 3. Diagram Fetching
        diagram_url = brain.get_relevant_diagram(last_user_msg)
        
        st.session_state.messages.append({
            "role": "assistant",
            "content": ai_text,
            "audio": audio_data,
            "image": diagram_url
        })
        st.rerun()