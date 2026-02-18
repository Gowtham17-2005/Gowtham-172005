import torch
from TTS.api import TTS

# GPU irukka nu check pannuvom (Fast processing-ku)
device = "cuda" if torch.cuda.is_available() else "cpu"

# Multilingual model-ai load pannuvom (XTTS v2 - idhu ElevenLabs level quality tharum)
tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2").to(device)

# Script input
story_text = "Oru oorula oru periya payangaramaana ghost irundhuchi. Adhu yaarum ninaikaadha nerathula veliya varum."

# Voice Generation
# 'speaker_wav' la oru 10 seconds casual-ah pesuna Tamil audio file path kudunga
# ElevenLabs madhiriye andha kural-la pesum
tts.tts_to_file(text=story_text, 
                speaker_wav="your_sample_voice.wav", 
                language="ta", 
                file_path="ghost_story_output.wav")

print("AI Voice Ready! ghost_story_output.wav file-ah check pannunga.")
