import streamlit as st
from TTS.api import TTS
import os
from pydub import AudioSegment

# Model-ai load pannuvathu (Muthal thadava matum late aagum)
@st.cache_resource
def load_model():
    # GPU iruntha gpu=True kudunga, illana False
    return TTS("tts_models/multilingual/multi-dataset/xtts_v2", gpu=False)

tts = load_model()

st.title("🎙️ Personal Tamil Voice Cloner")
st.write("Unga 8-second voice-ai upload panni, unga voice-laye pesa vainga!")

# 1. Voice File Upload
uploaded_file = st.file_uploader("Upload your 8-sec voice (MP3/WAV)", type=["mp3", "wav"])

# 2. Text Input
user_text = st.text_area("Tamil Text:", "வணக்கம், இது என் சொந்த குரலில் பேசும் ஏஐ.")

if st.button("Clone My Voice"):
    if uploaded_file is not None and user_text:
        with st.spinner("AI unga voice-ai padikithu..."):
            # Temporary-ah file-ai save panna
            with open("sample_voice.wav", "wb") as f:
                f.write(uploaded_file.getbuffer())
            
            # XTTS v2 cloning process
            output_path = "cloned_output.wav"
            tts.tts_to_file(
                text=user_text,
                file_path=output_path,
                speaker_wav="sample_voice.wav",
                language="ta"
            )
            
            # Play the result
            st.audio(output_path)
            st.success("Unga voice clone aayiduchi!")
    else:
        st.error("File matrum text renduமே mukkiyam!")
        
