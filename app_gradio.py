from model import englishteacher
import gradio as gr


# Function to generate a response using the GPT-2 model
def generate_response(text, history):
    response = englishteacher(text)
    return response


# Gradio interface
chatbot_interface = gr.ChatInterface(generate_response, chatbot=gr.Chatbot(height=400),
                                        title="Voice Assistant - English Coach",
                                        theme = 'base')
chatbot_interface.launch()
