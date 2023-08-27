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
algorithms = ['Particle Swarm Optimization', 'Artificial Bee Colony', 'Differential Evolution']

with gr.Blocks() as demo:
    with gr.Row():
        title = gr.Label('Evolutionary Computation - Code Generation 🧬💻')
    with gr.Row():
        textArea = gr.Textbox(label='Enter the code topic:', lines = 4)
    with gr.Row():
        language = gr.Dropdown(languages, label = 'Programming Languages', multiselect=False)
        function = gr.Dropdown(functions, label = 'Function', multiselect=False)
        algorithm = gr.Dropdown(algorithms, label = 'Algorithms', multiselect=False)
    with gr.Row():
        btn_generate = gr.Button("Generate")
        with gr.Column(scale=1, min_width=600):
            text1 = gr.Textbox(label="prompt 1")
            text2 = gr.Textbox(label="prompt 2")
            inbtw = gr.Button("Between")
            text4 = gr.Textbox(label="prompt 1")
            text5 = gr.Textbox(label="prompt 2")
        with gr.Column(scale=2, min_width=600):
            btn = gr.Button("Go")

demo.launch()
