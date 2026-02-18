import gradio as gr
from TTS.api import TTS
import os

# 1. Model Setup - Unga 12th Gen Intel CPU-ku optimize panrom
device = "cpu"
model_name = "tts_models/multilingual/multi-dataset/xtts_v2"
tts = TTS(model_name).to(device)

def clone_voice(story_text, audio_file):
    if audio_file is None:
        return "Error: Please upload a voice sample!"
    
    output_path = "ghost_story_web_output.wav"
    
    # AI Processing
    tts.tts_to_file(
        text=story_text,
        speaker_wav=audio_file.name,
        language="ta",
        file_path=output_path
    )
    return output_path

# 2. Web Interface Design
with gr.Blocks(title="Ghost Story AI Generator") as demo:
    gr.Markdown("# 👻 Ghost Story AI Voice Cloner")
    gr.Markdown("Unga kural-la ghost stories pesa vaikka inga script-ah type pannunga.")
    
    with gr.Row():
        with gr.Column():
            input_text = gr.Textbox(label="Unga Ghost Story Script-ah inga type pannunga", placeholder="e.g., Antha iruttu kaatukulla...", lines=5)
            input_audio = gr.File(label="Unga 8-second Voice Sample-ah Upload Pannunga (MP3 or WAV)")
            generate_btn = gr.Button("Generate Ghost Story 🎙️")
        
        with gr.Column():
            output_audio = gr.Audio(label="AI Generated Ghost Voice")

    generate_btn.click(fn=clone_voice, inputs=[input_text, input_audio], outputs=output_audio)

# 3. App-ah Launch panrom
demo.launch(inbrowser=True)
