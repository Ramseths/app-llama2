import gradio as gr
from model import getResponse

def greet(name):
    return "Hello " + name + "!"

genres = ['Romance', 'Comedy', 'Horror', 'Fantasy']


with gr.Blocks() as demo:
    with gr.Row():
        title = gr.Label('Story Generation with Llama 2 📝💻')
    with gr.Row():
        story = gr.Textbox(label='Enter the Story Topic:', lines = 2)
    with gr.Row():
        genre = gr.Dropdown(genres, label = 'Story Genre', multiselect=False)
        character = gr.Textbox(placeholder = 'Name',label = 'Main Character')
    with gr.Row():
        output = gr.Textbox(label = 'Story:')
        btn = gr.Button("Generate")
        btn.click(fn = getResponse, inputs = [story, genre, character], outputs = output)
            
demo.launch()
