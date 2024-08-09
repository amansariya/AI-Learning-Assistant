from fastapi import FastAPI
from fastapi.responses import RedirectResponse
import gradio as gr
from langflow.load import run_flow_from_json
from fastapi.middleware.cors import CORSMiddleware
import os

def chat(history, message):
    if history is None:
        history = []
    
    print(f'Request for chat received with message={message}')
    result = run_flow_from_json(flow="Vector Store RAG.json",
                                input_value=message,
                                fallback_to_env_vars=True,
                                tweaks=TWEAKS)
    print(f'Result structure: {result}')
    if message:
        print(f'Request for chat received with message={message}')
        
        try:
            answer = result[0].outputs[0].results['message'].data['text']
        except KeyError:
            answer = "Sorry, I couldn't process that request."
        history.append((message, answer))
        return history, history
    else:
        return history, history

# Initialize FastAPI app
app = FastAPI()

# Configure CORS middleware (optional, depending on your needs)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods
    allow_headers=["*"],  # Allow all headers
)

# Initialize Gradio app
with gr.Blocks() as demo:
    chatbot = gr.Chatbot()
    state = gr.State([])
    txt = gr.Textbox(placeholder="Type your message here...")
    send_button = gr.Button("Send")
    clear_button = gr.ClearButton([txt])

    def submit(message, history):
        return chat(history, message)
    
    txt.submit(submit, [txt, state], [chatbot, state])
    send_button.click(submit, inputs=[txt, state], outputs=[chatbot, state])

# Mount the Gradio app to the FastAPI app
app = gr.mount_gradio_app(app, demo, path="/gradio")

@app.get("/")
def root():
    # Redirect to the Gradio interface
    return RedirectResponse(url="/gradio")

# Run the app using Uvicorn
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=7860)
