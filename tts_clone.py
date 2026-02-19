# ============================================
# Tamil Voice Clone TTS (MP3/WAV support)
# Casual emotional speech
# ============================================

import os
import librosa
import soundfile as sf
from TTS.api import TTS

# --------------------------------------------
# SETTINGS (CHANGE ONLY IF NEEDED)
# --------------------------------------------

VOICE_FILE = "myvoice.wav"  # can be .wav or .mp3
OUTPUT_FILE = "output.wav"

TEXT = """
ஹாய் நண்பர்களே…
இது என் குரலில் உருவாக்கப்பட்ட ஒரு AI voice.
இது ரொம்ப natural ஆக இருக்கும்னு நம்புறேன்.
"""

# --------------------------------------------
# FUNCTION: convert mp3 → wav if needed
# --------------------------------------------

def prepare_voice(input_path):
    ext = os.path.splitext(input_path)[1].lower()

    if ext == ".wav":
        print("✅ WAV file detected")
        return input_path

    elif ext == ".mp3":
        print("🔄 Converting MP3 to WAV...")

        # load mp3
        audio, sr = librosa.load(input_path, sr=22050)

        temp_wav = "temp_voice.wav"
        sf.write(temp_wav, audio, sr)

        print("✅ MP3 converted to WAV")
        return temp_wav

    else:
        raise ValueError("❌ Only MP3 or WAV supported!")

# --------------------------------------------
# MAIN
# --------------------------------------------

def main():
    print("🚀 Loading model (first time slow)...")

    tts = TTS(
        model_name="tts_models/multilingual/multi-dataset/xtts_v2",
        progress_bar=True,
        gpu=False,
    )

    speaker_wav = prepare_voice(VOICE_FILE)

    print("🎙️ Generating emotional speech...")

    tts.tts_to_file(
        text=TEXT,
        speaker_wav=speaker_wav,
        language="ta",
        file_path=OUTPUT_FILE,
    )

    print("✅ Done! Check output.wav")

if __name__ == "__main__":
    main()
