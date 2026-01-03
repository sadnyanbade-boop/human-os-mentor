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
    initial_sidebar_state="auto"
)

# --- 2. STABLE UI STYLING ---
st.markdown("""
<style>
    /* 1. HIDE ONLY THE FOOTER (Stable) */
    footer {visibility: hidden;}

    /* 2. CHAT BUBBLES (Stable) */
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
</style>
""", unsafe_allow_html=True)

# --- 3. SIDEBAR ---
with st.sidebar:
    st.markdown("<h1 style='text-align: center;'>🧬</h1>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: center;'>Human OS</h2>", unsafe_allow_html=True)
    st.divider()
    
    language_mode = st.radio("🗣️ Language", ["English", "Semi-English (Hinglish)", "Marathi (पूर्ण मराठी)"])
    
    st.subheader("📚 Syllabus")
    selected_class = st.selectbox("Class", list(data.MAHARASHTRA_SYLLABUS.keys()))
    selected_subject = st.selectbox("Subject", list(data.MAHARASHTRA_SYLLABUS[selected_class].keys()))
    selected_chapter = st.selectbox("Chapter", data.MAHARASHTRA_SYLLABUS[selected_class][selected_subject])
    
    st.divider()
    enable_audio = st.toggle("🔊 Audio Mode", value=True)
    
    if st.button("🗑️ Clear Chat", use_container_width=True):
        st.session_state.messages = []
        st.rerun()

# --- 4. MAIN INTERFACE ---
subject_icon = "🧪" if "Science" in selected_subject else "📐"
st.title(f"{subject_icon} {selected_subject}")
st.caption(f"**Chapter:** `{selected_chapter}`")

if "messages" not in st.session_state: st.session_state.messages = []
if "current_chapter" not in st.session_state: st.session_state.current_chapter = selected_chapter

if st.session_state.current_chapter != selected_chapter:
    st.session_state.messages = []
    st.session_state.current_chapter = selected_chapter

for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.markdown(f'<div class="user-msg"><b>You:</b><br>{msg["content"]}</div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="bot-msg"><b>Mentor:</b><br>{msg["content"]}</div>', unsafe_allow_html=True)
        if msg.get("image"): st.image(msg["image"], width=400)
        if msg.get("audio"): st.audio(msg["audio"], format='audio/mp3')

if len(st.session_state.messages) == 0:
    st.markdown("### 🔥 Key Concepts")
    class_concepts = data.IMPORTANT_CONCEPTS.get("English", {})
    concepts = class_concepts.get(selected_chapter, class_concepts.get("default", ["Overview"]))
    
    cols = st.columns(3)
    for i, concept in enumerate(concepts):
        if cols[i % 3].button(f"📌 {concept}", use_container_width=True, key=f"btn_{i}"):
            st.session_state.clicked_prompt = f"Explain {concept}"

# --- 5. INPUT & AI LOGIC ---
st.divider()
user_input = st.chat_input("Ask a doubt here...")

if "clicked_prompt" in st.session_state and st.session_state.clicked_prompt:
    user_input = st.session_state.clicked_prompt
    st.session_state.clicked_prompt = None

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input.replace("Explain ", "")})
    st.rerun()

if st.session_state.messages and st.session_state.messages[-1]["role"] == "user":
    last_user_msg = st.session_state.messages[-1]["content"]
    with st.spinner("🧠 Thinking..."):
        ai_text = brain.get_ai_response(last_user_msg, st.session_state.messages[:-1], selected_class, selected_subject, selected_chapter, language_mode)
        audio_data = None
        if enable_audio and "⚠️" not in ai_text:
            audio_data = brain.get_audio_bytes(ai_text, language_mode)
        diagram_url = brain.get_relevant_diagram(last_user_msg)
        st.session_state.messages.append({"role": "assistant", "content": ai_text, "audio": audio_data, "image": diagram_url})
        st.rerun()
