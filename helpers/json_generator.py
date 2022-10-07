from flask import jsonify
def json_generator(is_error, predictions = None, error = False):
    response = {}
    if is_error:
        response["error"] = {}
        if (error == 'invalid_filename_provided'):
            response["error"]["code"] = 400
            response["error"]["message"] = "No filename is provided, or file extension is not txt."
        if (error == 'missing_file'):
            response["error"]["code"] = 400
            response["error"]["message"] = "No file is provided."
        elif (error == 'invalid_sentences'):
            response["error"]["code"] = 400
            response["error"]["message"] = "No sentence is provided."
        elif (error == 'invalid_personality'):
            response["error"]["code"] = 404
            response["error"]["message"] = "Invalid personality is provided."
        elif (error == 'invalid_file_type'):
            response["error"]["code"] = 400
            response["error"]["message"] = "File provided is in incorrect file format, please convert into txt, pdf or docx format."
    else:
        response["data"] = {}
        response["data"]["predictions"] = predictions

    return jsonify(response)