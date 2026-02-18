import os
import streamlit as st
from TTS.api import TTS
import soundfile as sf
import numpy as np

# ---------------- PAGE ----------------
st.set_page_config(page_title="Tamil Emotion Story AI", page_icon="🎭")

st.title("🎭🔥 Tamil Emotion Story Generator")
st.write("Long Tamil story paste pannunga — emotion narration ready 😎")

# ---------------- LOAD MODEL ----------------
@st.cache_resource
def load_tts():
    return TTS(model_name="tts_models/multilingual/multi-dataset/xtts_v2")

tts = load_tts()

# ---------------- EMOTION PRESETS ----------------
emotion_styles = {
    "😐 Normal": {"speed": 1.0, "prefix": ""},
    "😊 Happy": {"speed": 1.08, "prefix": "மகிழ்ச்சியாக சொல்லு: "},
    "😢 Sad": {"speed": 0.92, "prefix": "சோகமாக சொல்லு: "},
    "😡 Angry": {"speed": 1.12, "prefix": "கோபமாக சொல்லு: "},
    "📖 Story Narrator": {"speed": 0.98, "prefix": "ஒரு கதை சொல்லும் பாணியில்: "},
    "🧒 Kids Story": {"speed": 1.05, "prefix": "குழந்தைகளுக்காக இனிமையாக சொல்லு: "}
}

# ---------------- TEXT SPLITTER ----------------
def split_text(text, max_chars=500):
    sentences = text.replace("\n", " ").split(".")
    chunks = []
    current = ""

    for sentence in sentences:
        if len(current) + len(sentence) < max_chars:
            current += sentence + ". "
        else:
            chunks.append(current.strip())
            current = sentence + ". "

    if current:
        chunks.append(current.strip())

    return chunks

# ---------------- UI ----------------
text = st.text_area("✍️ Paste your Tamil story")

emotion_choice = st.selectbox(
    "🎭 Choose Emotion Style",
    list(emotion_styles.keys())
)

uploaded_voice = st.file_uploader(
    "🎙️ Optional: Upload your voice (WAV for cloning)",
    type=["wav"]
)

# ---------------- GENERATE ----------------
if st.button("🚀 Generate Emotion Voice"):

    if not text.strip():
        st.warning("Story paste pannunga bro 😅")

    else:
        with st.spinner("Emotion narration running... ⏳"):

            try:
                style = emotion_styles[emotion_choice]
                styled_text = style["prefix"] + text
                speed = style["speed"]

                chunks = split_text(styled_text, max_chars=500)

                audio_list = []
                sample_rate = 24000

                # Save uploaded voice
                voice_path = None
                if uploaded_voice is not None:
                    voice_path = "temp_voice.wav"
                    with open(voice_path, "wb") as f:
                        f.write(uploaded_voice.read())

                # Generate each chunk
                for i, chunk in enumerate(chunks):
                    temp_out = f"chunk_{i}.wav"

                    if voice_path:
                        tts.tts_to_file(
                            text=chunk,
                            speaker_wav=voice_path,
                            language="ta",
                            file_path=temp_out,
                            speed=speed
                        )
                    else:
                        tts.tts_to_file(
                            text=chunk,
                            language="ta",
                            file_path=temp_out,
                            speed=speed
                        )

                    data, sr = sf.read(temp_out)
                    sample_rate = sr
                    audio_list.append(data)

                # Merge audio
                final_audio = np.concatenate(audio_list)
                sf.write("final_story.wav", final_audio, sample_rate)

                st.success("✅ Emotion story ready bro!")
                st.audio("final_story.wav")

            except Exception as e:
                st.error(f"Error: {e}")

# ---------------- FOOTER ----------------
st.markdown("---")
st.caption("Unlimited Emotion Story Mode 😈🔥")
