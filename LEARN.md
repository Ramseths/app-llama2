## 🚀 Project Introduction
This project is a web application built with Gradio, LLaMA 2 and LangChain to generate stories.

## 📝 Instructions for Use
Enter a story topic, select the genre and finally the main character. Click on the generate button and wait a while (quite a while) to get a story.

## 💻 Technologies Used
- LLaMA 7B Chat ⚛️
- Gradio 🎨
- LangChain 🤖

## 🏗️ Building the Project
Follow these steps to build and run the project locally using Anaconda:

Prerequisites: Ensure you have the following software installed on your system:

- Anaconda
- Model LLaMA 2

Clone the repository: Clone the project to your local machine.

1. Create virtual env with conda:
    ```conda create -n llama python=3.8```

2. Activate virtual env:
    ```conda activate llama```

3. Install gradio:
    ``conda install -c conda-forge gradio```

4. Install requirements.txt:
    ```pip install -r requirements.txt```

5. Finally, run:
    ```python app.py```