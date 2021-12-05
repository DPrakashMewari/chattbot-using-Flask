import flask
from flask import Flask,render_template,request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

app = Flask(__name__)

chatbot = ChatBot('Ron Obvious',storage_adapter="chatterbot.storage.SQLStorageAdapter")
# Create a new trainer for the chatbot
trainer = ChatterBotCorpusTrainer(chatbot)
# Train the chatbot based on the english corpus
trainer.train("chatterbot.corpus.english")

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/get")
def chatbotcall():
    msg = request.args.get('msg')
    response = chatbot.get_response(msg)
    return render_template('index.html',ourresponse=str(msg),botresponse=response)

if __name__ == "__main__":
    app.run(debug=True)