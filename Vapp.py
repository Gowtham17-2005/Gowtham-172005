import streamlit as st
from gtts import gTTS
import os
from io import BytesIO

# --- Page Config ---
st.set_page_config(page_title="Tamil Text to Voice Converter", page_icon="🎙️")

def main():
    # 1.1 & 3: Application Name & UI
    st.title("🎙️ Tamil Text to Voice Converter")
    st.markdown("### YouTube Storytellers-க்கான க்யூட்டான டூல்")

    # 2.1 & 3: Text input field for Tamil content
    tamil_text = st.text_area("Tamil Text-ஐ இங்கே உள்ளிடவும்:", height=250, 
                              placeholder="ஒரு ஊர்ல ஒரு ராஜா இருந்தாராம்...")

    # 2.2 & 3: Voice age range selector
    st.subheader("Voice Settings")
    age_group = st.selectbox(
        "வயது வரம்பு (Age Range):",
        ["Young Adult Male (இளைஞர்)", "Middle-Aged Male (நடுத்தர வயது)", "Senior Male (பெரியவர்)"]
    )

    # Logic to adjust speed based on age range
    # 'slow=True' for Senior to simulate a slower, natural pace
    is_slow = True if "Senior" in age_group else False

    # 3: Generate button
    if st.button("Generate Audio (குரலை உருவாக்கு)"):
        if tamil_text.strip() == "":
            st.error("Please enter some Tamil text first!")
        else:
            with st.spinner('Converting to voice...'):
                try:
                    # 2.2: Natural, casual style using gTTS
                    tts = gTTS(text=tamil_text, lang='ta', slow=is_slow)
                    
                    # 2.3: Audio output in MP3 format
                    mp3_fp = BytesIO()
                    tts.write_to_fp(mp3_fp)
                    
                    # 3: Audio player for preview
                    st.success("Audio Generated!")
                    st.audio(mp3_fp, format='audio/mp3')
                    
                    # 2.3 & 3: Download button for MP3 file
                    st.download_button(
                        label="Download MP3 (பதிவிறக்கம் செய்)",
                        data=mp3_fp.getvalue(),
                        file_name="tamil_story_audio.mp3",
                        mime="audio/mp3"
                    )
                except Exception as e:
                    st.error(f"Error: {e}")

if __name__ == "__main__":
    main()
    
