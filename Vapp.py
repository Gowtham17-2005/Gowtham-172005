import streamlit as st
from TTS.api import TTS
import os
import torch

# Page Config
st.set_page_config(page_title="Ghost Story AI Voice", page_icon="👻")

st.title("👻 Ghost Story - Voice Cloner")
st.write("Unga voice-laye bayangaramaana kathaigalai uruvaakkunga!")

# AI Model Load (Unga 16GB RAM ithai nalla handle pannum)
@st.cache_resource
def load_model():
    device = "cuda" if torch.cuda.is_available() else "cpu"
    return TTS("tts_models/multilingual/multi-dataset/xtts_v2").to(device)

tts = load_model()

# 1. Voice Upload Section
uploaded_file = st.file_uploader("Unga 8-second audio file-ah upload pannunga (WAV/MP3)", type=['wav', 'mp3'])

# 2. Story Text Section
story_text = st.text_area("Ghost Story Script-ah inga type pannunga:", 
                          height=200, 
                          placeholder="Antha iruttu araiyil...")

# 3. Generation Button
if st.button("Generate Ghost Voice 🎙️"):
    if uploaded_file is not None and story_text:
        with st.spinner("AI unga voice-la pesittu irukku... konjam poruunga..."):
            # Temporary-ah file-ah save panrom
            with open("temp_voice.wav", "wb") as f:
                f.write(uploaded_file.getbuffer())
            
            # Voice Generation
            output_path = "final_ghost_story.wav"
            tts.tts_to_file(
                text=story_text,
                speaker_wav="temp_voice.wav",
                language="ta",
                file_path=output_path
            )
            
            # Output Display
            st.success("Ghost Story ready bro!")
            audio_file = open(output_path, 'rb')
            st.audio(audio_file.read(), format='audio/wav')
            
            # Download Button
            st.download_button(label="Download Audio", data=audio_file, file_name="ghost_story.wav")
    else:
        st.error("Dhayavu senju audio file matrum story script-ah kudunga!")
