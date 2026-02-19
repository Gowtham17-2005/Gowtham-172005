# ============================================
# Tamil Voice Clone TTS (MP3/WAV support)
# Casual emotional speech - FIXED FOR TORCH 2.4+
# ============================================

import os
import librosa
import soundfile as sf
import torch  # <--- இதைக் கண்டிப்பாகச் சேர்க்க வேண்டும்
from TTS.api import TTS

# --------------------------------------------
# SECURITY FIX: Allow Coqui TTS globals in Torch
# --------------------------------------------
# புதிய Torch வெர்ஷனில் வரும் 'UnpicklingError' ஐத் தடுக்க இந்த வரிகள் உதவும்
torch.serialization.add_safe_globals(['TTS.tts.configs.vits_config.VitsConfig'])
torch.serialization.add_safe_globals(['TTS.tts.configs.xtts_config.XttsConfig'])
torch.serialization.add_safe_globals(['TTS.config.shared_configs.BaseDatasetConfig'])

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
    # உங்கள் வாய்ஸ் ஃபைல் இருக்கிறதா என்று சரிபார்க்கிறது
    if not os.path.exists(input_path):
        raise FileNotFoundError(f"❌ '{input_path}' என்ற கோப்பு உங்கள் ஃபோல்டரில் இல்லை!")

    ext = os.path.splitext(input_path)[1].lower()

    if ext == ".wav":
        print("✅ WAV file detected")
        return input_path

    elif ext == ".mp3":
        print("🔄 Converting MP3 to WAV...")
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

    # ஒருவேளை மேலே உள்ள globals வேலை செய்யவில்லை என்றால், 
    # மாடலை லோட் செய்யும் போது weights_only=False என்பதைப் பயன்படுத்த வேண்டும்.
    # Coqui TTS API இதை உள்ளுக்குள் (internally) கையாளும்.
    
    try:
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

        print(f"✅ Done! Check {OUTPUT_FILE}")

    except Exception as e:
        print(f"❌ Error occurred: {e}")
        print("\n💡 Tip: ஒருவேளை இன்னும் Error வந்தால் 'pip install torch==2.3.1' என்று கொடுத்துப் பாருங்கள்.")

if __name__ == "__main__":
    main()
    
