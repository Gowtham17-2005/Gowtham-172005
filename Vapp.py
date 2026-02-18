import streamlit as st
from TTS.api import TTS
import os

# --- PAGE SETUP ---
st.set_page_config(page_title="Tamil Ghost Storyteller", page_icon="🎙️")
st.title("🎙️ Tamil Custom Voice AI")

# --- LOAD AI MODEL ---
@st.cache_resource
def load_model():
    # XTTS v2 dhaan ElevenLabs level-ku voice clone pannum
    return TTS("tts_models/multilingual/multi-dataset/xtts_v2").to("cpu")

with st.spinner("AI Model ready aagudhu... Konjam porumaiya irunga..."):
    tts = load_model()

# --- USER INTERFACE ---
st.subheader("1. Unga Ghost Story-ai Type Pannunga:")
story_text = st.text_area("Tamil ghost story-ai inge type pannunga:", height=150)

st.subheader("2. Unga 8-Second Voice Sample-ai Upload Pannunga:")
uploaded_voice = st.file_uploader("Upload 8-sec Sample (WAV/MP3 format):", type=["wav", "mp3"])

# --- GENERATE VOICE ---
if st.button("Generate My Voice"):
    if story_text and uploaded_voice:
        # Temporary-ah unga audio-vai save panrom reference-kaaga
        with open("temp_sample.wav", "wb") as f:
            f.write(uploaded_voice.getbuffer())
        
        with st.spinner('AI unga kural-la pesudhu...'):
            # Voice Cloning process aarambam
            tts.tts_to_file(text=story_text, 
                            speaker_wav="temp_sample.wav", 
                            language="ta", 
                            file_path="cloned_output.wav")
            
        st.success("Semma! Unga kural-la ghost story ready:")
        st.audio("cloned_output.wav")
        
        with open("cloned_output.wav", "rb") as file:
            st.download_button(label="Download Audio", data=file, file_name="my_ghost_story.wav")
    else:
        st.warning("Story text matrum voice sample renduமே kudunga bro!")
        
