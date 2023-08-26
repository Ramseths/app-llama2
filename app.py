import gradio as gr

def greet(name):
    return "Hello " + name + "!"

# demo = gr.Interface(
#     fn=greet,
#     inputs=gr.Textbox(lines=2, placeholder="Name Here..."),
#     outputs="text",
# )

languages = ['JavaScript', 'Python', 'C++']
functions = ['Rosenbrock', 'Rastrigin']
algorithm = ['Particle Swarm Optimization', 'Artificial Bee Colony', 'Differential Evolution']

with gr.Blocks() as demo:
    with gr.Row():
        name = gr.Label('Code Generation 💻')
    with gr.Row():
        textArea = gr.Textbox(label='Enter the code topic:', lines = 4)
    with gr.Row():
        language = gr.Dropdown(languages, label = '', multiselect=False)
        function = gr.Dropdown(languages, multiselect=False)
    with gr.Row():
        with gr.Column(scale=1, min_width=600):
            text1 = gr.Textbox(label="prompt 1")
            text2 = gr.Textbox(label="prompt 2")
            inbtw = gr.Button("Between")
            text4 = gr.Textbox(label="prompt 1")
            text5 = gr.Textbox(label="prompt 2")
        with gr.Column(scale=2, min_width=600):
            btn = gr.Button("Go")

demo.launch()
