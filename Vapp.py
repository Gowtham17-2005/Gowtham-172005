import streamlit as st
from gtts import gTTS
import os

# Web page title and style
st.set_page_config(page_title="Tamil Text-to-Voice AI", page_icon="🔊")
st.title("🔊 Tamil Text to Voice Converter")
st.write("Unga Tamil text-ai inge type pannunga:")

# Text input area
user_text = st.text_area("Tamil Text Input", "வணக்கம் நண்பா, எப்படி இருக்கீங்க?", height=150)

# Speed control option
speed = st.radio("Pesura Vegam (Speed):", ("Normal", "Slow"), horizontal=True)
is_slow = True if speed == "Slow" else False

if st.button("Convert to Voice"):
    if user_text.strip() == "":
        st.warning("Please enter some Tamil text!")
    else:
        with st.spinner('Audio generate aaguthu...'):
            try:
                # gTTS use panni Tamil audio create panrathu
                tts = gTTS(text=user_text, lang='ta', slow=is_slow)
                filename = "tamil_audio.mp3"
                tts.save(filename)
                
                # Web-la audio play panna streamlit function
                audio_file = open(filename, 'rb')
                audio_bytes = audio_file.read()
                st.audio(audio_bytes, format='audio/mp3')
                
                # Download button
                st.download_button(
                    label="Download Audio",
                    data=audio_bytes,
                    file_name="tamil_voice.mp3",
                    mime="audio/mp3"
                )
                
                # Cleanup: System-la irunthu temporary file-ai remove panna
                audio_file.close()
                os.remove(filename)
                
            except Exception as e:
                st.error(f"Error: {e}")

st.divider()
st.caption("Made with ❤️ for Tamil Developers")
