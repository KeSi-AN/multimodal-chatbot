import os
import gradio as gr
import google.generativeai as genai
from dotenv import load_dotenv
import joblib
from utils.model_utils import classify_text

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-pro-vision")
classifier, label_encoder = joblib.load("saved_model/classifier_model.pkl")

def multimodal_chat(text, image=None, mode="Gemini AI"):
    if mode == "Gemini AI":
        if not text and not image:
            return "Please provide text and/or an image."
        inputs = []
        if text:
            inputs.append(text)
        if image:
            inputs.append(image)
        try:
            response = model.generate_content(inputs)
            return response.text
        except Exception as e:
            return f"Error: {e}"
    elif mode == "Local Classifier":
        if not text:
            return "Please provide text for classification."
        return classify_text(text, classifier, label_encoder)
    return "Invalid mode."

with gr.Blocks() as demo:
    gr.Markdown("# 🧠 Multimodal Chatbot")
    mode = gr.Radio(choices=["Gemini AI", "Local Classifier"], value="Gemini AI", label="Mode")
    text_input = gr.Textbox(lines=2, placeholder="Type your message...")
    image_input = gr.Image(type="filepath", label="Upload Image")
    submit_btn = gr.Button("Chat")
    output = gr.Textbox(label="Response")
    submit_btn.click(fn=multimodal_chat, inputs=[text_input, image_input, mode], outputs=output)
demo.launch()
