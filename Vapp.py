import streamlit as st
from gtts import gTTS

# Title Setup
st.title("🎙️ Tamil Storyteller AI")

# Text Box
story_text = st.text_area("Tamil Ghost Story-ai inge type pannunga:", height=150)

# Button
if st.button("Generate Voice"):
    if story_text:
        with st.spinner('AI Pesudhu...'):
            # gTTS use panni Tamil-la voice create panrom
            tts = gTTS(text=story_text, lang='ta')
            tts.save("story.mp3")
        
        st.success("Semma! Kelunga:")
        st.audio("story.mp3")
    else:
        st.warning("Story text-ah type pannunga bro!")
      
