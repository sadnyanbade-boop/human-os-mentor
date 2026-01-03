import streamlit as st
import warnings
import urllib.parse
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

# --- 2. PROFESSIONAL UI STYLING ---
st.markdown("""
<style>
    footer {visibility: hidden;}
    .stChatFloatingInputContainer {padding-bottom: 20px;}
    
    .video-card {
        background-color: #f9f9f9;
        border-radius: 10px;
        padding: 15px;
        border-left: 5px solid #ff0000;
        margin: 10px 0;
    }
</style>
""", unsafe_allow_html=True)

# --- 3. SIDEBAR ---
with st.sidebar:
    st.markdown("<h1 style='text-align: center;'>🧬 Human OS</h1>", unsafe_allow_html=True)
    st.divider()
    
    language_mode = st.radio("🗣️ Language", ["English", "Semi-English (Hinglish)", "Marathi (पूर्ण मराठी)"])
    
    st.subheader("📚 Syllabus")
    selected_class = st.selectbox("Class", list(data.MAHARASHTRA_SYLLABUS.keys()))
    selected_subject = st.selectbox("Subject", list(data.MAHARASHTRA_SYLLABUS[selected_class].keys()))
    selected_chapter = st.selectbox("Chapter", data.MAHARASHTRA_SYLLABUS[selected_class][selected_subject])
    
    st.divider()
    # VIDEO FEATURE TOGGLE
    enable_video = st.toggle("🎥 Show Video Recommendations", value=True)
    enable_audio = st.toggle("🔊 Audio Mode", value=True)
    
    if st.button("🗑️ Reset Chat", use_container_width=True):
        st.session_state.messages = []
        st.rerun()

# --- 4. MAIN INTERFACE ---
st.title(f"📖 {selected_subject}")
st.caption(f"**Chapter:** {selected_chapter}")

# Initialize Session
if "messages" not in st.session_state: st.session_state.messages = []

# --- 5. AUTOMATIC VIDEO LESSON ---
if enable_video:
    # We create a smart search link for educational videos
    search_query = f"Maharashtra Board {selected_class} {selected_subject} {selected_chapter} explanation"
    encoded_query = urllib.parse.quote(search_query)
    yt_url = f"https://www.youtube.com/results?search_query={encoded_query}"
    
    with st.expander("📺 Watch Video Lessons for this Chapter", expanded=False):
        st.markdown(f"""
        <div class="video-card">
            <h4>Recommended Visual Learning</h4>
            <p>I have found the best video explanations for <b>{selected_chapter}</b>.</p>
            <a href="{yt_url}" target="_blank">
                <button style="background-color: #ff0000; color: white; border: none; padding: 10px 20px; border-radius: 5px; cursor: pointer;">
                    ▶️ Open YouTube Lessons
                </button>
            </a>
        </div>
        """, unsafe_allow_html=True)

# Display Chat History
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])
        if msg.get("image"): st.image(msg["image"], width=400)
        if msg.get("audio"): st.audio(msg["audio"])

# --- 6. CHAT INPUT & BRAIN ---
user_input = st.chat_input("Ask a question...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.write(user_input)
    
    with st.chat_message("assistant"):
        with st.spinner("🧠 Thinking..."):
            ai_text = brain.get_ai_response(user_input, st.session_state.messages[:-1], selected_class, selected_subject, selected_chapter, language_mode)
            st.write(ai_text)
            
            # Optional Audio
            audio_data = None
            if enable_audio and "⚠️" not in ai_text:
                audio_data = brain.get_audio_bytes(ai_text, language_mode)
                st.audio(audio_data)
                
            # Optional Diagram
            diagram_url = brain.get_relevant_diagram(user_input)
            if diagram_url:
                st.image(diagram_url, width=400)
            
            st.session_state.messages.append({
                "role": "assistant", 
                "content": ai_text, 
                "audio": audio_data, 
                "image": diagram_url
            })
