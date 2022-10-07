from flask import Blueprint
from flask import request
from helpers import model_loader
from helpers.json_generator import json_generator

serve_summariser_bp = Blueprint('serve_summariser', __name__)


@serve_summariser_bp.route('/summarise/')
def serve_summariser():
    params = request.json

    if(params is not None and params['sentences'] is not None):
        result = model_loader.model(
            params['sentences'],
            min_length=16,
            max_length=256,
            no_repeat_ngram_size=3,
            encoder_no_repeat_ngram_size=3,
            repetition_penalty=3.5,
            num_beams=4,
            early_stopping=True,
        )
        return json_generator(False, result)
    else:
        return json_generator(True, error='invalid_sentences')
