import gradio as gr

from rag import process_pdf, ask_pdf

history = []


def upload_pdf(file):
    global history
    history = []

    if file is None:
        return "Please upload a PDF first."

    return process_pdf(file.name)


def chatbot(message, chat_history):
    global history

    answer, history = ask_pdf(message, history)

    chat_history.append((message, answer))

    return "", chat_history


with gr.Blocks(
    title="PDF Question Answering Assistant",
    theme=gr.themes.Soft()
) as demo:

    gr.Markdown(
        """
# 📄 PDF Question Answering Assistant

Upload a PDF and ask anything about its contents.

Powered by **Google Gemini + LangChain + ChromaDB**
"""
    )

    with gr.Row():

        pdf = gr.File(
            label="Upload PDF",
            file_types=[".pdf"]
        )

        upload_btn = gr.Button("Index PDF")

    status = gr.Textbox(
        label="Status",
        interactive=False
    )

    upload_btn.click(
        upload_pdf,
        inputs=pdf,
        outputs=status
    )

    chatbot_ui = gr.Chatbot(height=450)

    msg = gr.Textbox(
        placeholder="Ask a question about your PDF..."
    )

    msg.submit(
        chatbot,
        inputs=[msg, chatbot_ui],
        outputs=[msg, chatbot_ui]
    )

demo.launch()