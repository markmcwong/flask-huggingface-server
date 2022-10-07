from flask import Flask
from transformers import pipeline
from api.serve_summariser import serve_summariser_bp
from helpers import model_loader
import torch

app = Flask(__name__)
app.register_blueprint(serve_summariser_bp)


def startup_event():
    # has to assign to variables in another file rather than directly exported in app.py
    # to avoid circular import
    model_name = 'pszemraj/led-large-book-summary'
    summarizer = pipeline(
        "summarization",
        model_name,
        device=0 if torch.cuda.is_available() else -1,
    )
    model_loader.model = summarizer
    print('Model loaded')
    # model_loader.tokenizer = AutoTokenizer.from_pretrained(
    #     "pszemraj/led-large-book-summary")
    # print('AutoTokenizer loaded')


def run_server():
    startup_event()
    app.run(debug=True, use_reloader=False)


if __name__ == "__main__":
    run_server()
