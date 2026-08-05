import gradio as gr

from rag import process_pdf, ask_pdf

history = []


# -----------------------------
# Upload & Index PDF
# -----------------------------
def upload_pdf(file):
    global history
    history = []

    if file is None:
        return "Please upload a PDF first."

    try:
        result = process_pdf(file.name)
        return result

    except Exception as e:
        import traceback
        traceback.print_exc()
        return f"❌ Error: {str(e)}"


# -----------------------------
# Chat Function
# -----------------------------
def chatbot(message, chat_history):
    global history

    if chat_history is None:
        chat_history = []

    answer, history = ask_pdf(message, history)

    chat_history.append(
        {
            "role": "user",
            "content": message,
        }
    )

    chat_history.append(
        {
            "role": "assistant",
            "content": answer,
        }
    )

    return "", chat_history


# -----------------------------
# UI
# -----------------------------
with gr.Blocks(
    title="PDF Question Answering Assistant",
    theme=gr.themes.Soft(),
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
            file_types=[".pdf"],
        )

        upload_btn = gr.Button("Index PDF")

    status = gr.Textbox(
        label="Status",
        interactive=False,
    )

    upload_btn.click(
        fn=upload_pdf,
        inputs=pdf,
        outputs=status,
    )

    chatbot_ui = gr.Chatbot(
        type="messages",
        height=450,
    )

    msg = gr.Textbox(
        placeholder="Ask a question about your PDF..."
    )

    msg.submit(
        fn=chatbot,
        inputs=[msg, chatbot_ui],
        outputs=[msg, chatbot_ui],
    )

demo.launch()