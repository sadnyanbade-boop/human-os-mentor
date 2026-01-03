# brain.py
import google.generativeai as genai
import edge_tts
import asyncio
import re
import io
import streamlit as st
from google.api_core import exceptions
from data import DIAGRAM_DB # Import diagram DB from data.py

# --- 1. CONFIGURE AI ---
def configure_genai():
    try:
        if "GOOGLE_API_KEY" in st.secrets:
            genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
            return True
        else:
            st.error("🚨 Missing API Key! Check .streamlit/secrets.toml")
            return False
    except Exception as e:
        st.error(f"⚠️ Connection Error: {e}")
        return False

# Initialize Model
model = None
if configure_genai():
    # Helper to pick best model
    available = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
    chosen = next((m for m in ["models/gemini-1.5-flash", "models/gemini-1.5-flash-8b"] if m in available), available[0] if available else None)
    if chosen:
        model = genai.GenerativeModel(chosen)

# --- 2. AI RESPONSE LOGIC ---
def get_ai_response(student_input, chat_history, class_level, subject, chapter, lang_mode):
    if not model: return "⚠️ AI Model not loaded."

    history_context = ""
    for msg in chat_history:
        role = "Student" if msg["role"] == "user" else "Mentor"
        history_context += f"{role}: {msg['content']}\n"
    
    # Language Instructions
    if lang_mode == "English":
        lang_instruction = "Respond in simple English."
    elif "Marathi" in lang_mode and "Semi" not in lang_mode:
        lang_instruction = "Respond in PURE MARATHI. Use English only for brackets."
    else:
        lang_instruction = "Respond in MARATHI mixed with ENGLISH technical words (Hinglish)."

    # Sandwich Method Prompt
    system_prompt = f"""
    You are a friendly Tutor for {class_level} {subject} (SSC Board).
    CHAPTER: "{chapter}"
    LANGUAGE: {lang_instruction}
    
    GOAL: Teach '{student_input}' using the 'Sandwich Method'.
    
    STRUCTURE:
    1. DIRECT ANSWER: Start with a clear definition, formula, or fact (Max 2 sentences).
    2. ANALOGY: Explain it using a local Indian context (Cricket, Festival, Kitchen, Traffic).
    3. CHECK: End with one simple question to check understanding.
    
    NOTE: If asking for Formula/Definition, give it IMMEDIATELY in step 1.
    """
    
    full_prompt = f"{system_prompt}\n\nHISTORY:\n{history_context}\n\nStudent: {student_input}"
    
    try:
        response = model.generate_content(full_prompt)
        return response.text
    except Exception as e:
        return f"⚠️ Technical Error: {str(e)}"

# --- 3. AUDIO LOGIC ---
async def _generate_audio_async(text, voice, rate):
    try:
        communicate = edge_tts.Communicate(text, voice, rate=rate)
        audio_data = b""
        async for chunk in communicate.stream():
            if chunk["type"] == "audio":
                audio_data += chunk["data"]
        return io.BytesIO(audio_data) if audio_data else None
    except Exception:
        return None

def get_audio_bytes(text, lang_mode):
    try:
        # Clean text
        clean_text = re.sub(r'[^\w\s,.?]', '', re.sub(r'\s*\(.*?\)', '', text))
        if not clean_text or len(clean_text.strip()) < 2: return None 
        
        # Select Voice & Speed
        if "Marathi" in lang_mode and "Semi" not in lang_mode:
            voice = "mr-IN-ManoharNeural"
            speed = "-15%"
        elif "Semi-English" in lang_mode:
            voice = "hi-IN-MadhurNeural"
            speed = "-15%"
        else:
            voice = "en-IN-PrabhatNeural"
            speed = "-10%"
        
        return asyncio.run(_generate_audio_async(clean_text, voice, speed))
    except Exception:
        return None

# --- 4. DIAGRAM LOGIC ---
def get_relevant_diagram(user_text):
    text_lower = user_text.lower()
    for keywords, url in DIAGRAM_DB.items():
        for key in keywords:
            if key in text_lower:
                return url
    return None