import streamlit as st
from TTS.api import TTS
import os

# Page Title
st.set_page_config(page_title="Tamil Ghost Story AI", page_icon="👻")
st.title("🎙️ Tamil Storyteller AI")

# Model-ai load panna (Modhalla konjam time edukkum)
@st.cache_resource
def load_model():
    return TTS("tts_models/multilingual/multi-dataset/xtts_v2").to("cpu")

tts = load_model()

# User Input
st.subheader("Unga Story-ai Type Pannunga:")
story_text = st.text_area("Tamil-la ezhudhavum...", height=150)

# Voice Cloning Sample
st.subheader("Voice Sample Upload Pannunga (WAV format):")
uploaded_file = st.file_uploader("Casual human voice (10-15 sec)", type=["wav"])

if st.button("Generate Audio"):
    if story_text and uploaded_file:
        # Sample-ai temporary-ah save pannuvom
        with open("sample.wav", "wb") as f:
            f.write(uploaded_file.getbuffer())
        
        with st.spinner('AI Pesudhu... Konjam porumaiya irunga...'):
            tts.tts_to_file(text=story_text, 
                            speaker_wav="sample.wav", 
                            language="ta", 
                            file_path="output.wav")
        
        st.success("Success! Kelunga:")
        st.audio("output.wav")
        
        # Download button
        with open("output.wav", "rb") as file:
            st.download_button(label="Download Audio", data=file, file_name="story.wav")
    else:
        st.warning("Story text matrum voice sample renduமே mukkiam!")
