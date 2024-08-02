import os

from flask import (Flask, redirect, render_template, request,
                   send_from_directory, url_for)
from langflow.load import run_flow_from_json


TWEAKS = {
  "ChatInput-PIbxE": {},
  "AstraVectorStoreComponent-3wF9y": {},
  "ParseData-b1pCb": {},
  "Prompt-mY768": {},
  "ChatOutput-tNmf1": {},
  "SplitText-b4YP5": {},
  "File-hzYXz": {},
  "AstraVectorStoreComponent-6yQOg": {},
  "OpenAIEmbeddings-ptVaH": {},
  "OpenAIEmbeddings-y9dEH": {},
  "OpenAIModel-Qe5KX": {},
  "ConversationChain-sOivX": {}
}

app = Flask(__name__)


@app.route('/')
def index():
   print('Request for index page received')
   return render_template('index.html')

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/chat', methods=['POST'])
def chat():
    question = request.form.get('question')
    print('Request for chat page received with name=%s' % question)
    result = run_flow_from_json(flow="Vector Store RAG.json",
                        input_value=question,
                        fallback_to_env_vars=True, # False by default
                        tweaks=TWEAKS)
    print(result)
    if question:
        print('Request for chat page received with question=%s' % question)
        answer = result[0].outputs[0].results
        return render_template('chat.html', question=question, answer=answer)
    else:
        print('Request for chat page received with no question or blank question -- redirecting')
        return redirect(url_for('index'))

# @app.route('/hello', methods=['POST'])
# def hello():
#    name = request.form.get('name')

#    if name:
#        print('Request for hello page received with name=%s' % name)
#        return render_template('hello.html', name = name)
#    else:
#        print('Request for hello page received with no name or blank name -- redirecting')
#        return redirect(url_for('index'))


if __name__ == '__main__':
   app.run()
