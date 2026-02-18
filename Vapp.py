import streamlit as st
from gtts import gTTS
import os

# Page Title Setup
st.set_page_config(page_title="Tamil Ghost Story AI", page_icon="👻")
st.title("🎙️ Tamil Storyteller AI")

# User Input Section
st.subheader("Unga Story-ai Type Pannunga:")
story_text = st.text_area("Tamil-la ezhudhavum...", height=150)

# Generate Button
if st.button("Generate Voice"):
    if story_text:
        with st.spinner('AI Pesudhu...'):
            # Tamil voice generate panrom
            tts = gTTS(text=story_text, lang='ta')
            tts.save("story.mp3")
        
        st.success("Semma! Kelunga:")
        st.audio("story.mp3")
        
        # Download option
        with open("story.mp3", "rb") as file:
            st.download_button(label="Download Audio", data=file, file_name="ghost_story.mp3")
    else:
        st.warning("Story text-ah type pannunga bro!")
        
