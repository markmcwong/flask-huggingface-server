import helpers.scripts.file_type_converters as ftc
import os
from datetime import datetime

ALLOWED_EXTENSIONS = {'txt', '.pdf', '.docx'}


def convert_file(file, filename, file_extension):
    return None


def extract_file_info(file):
    filename = file.filename
    file_extension = os.path.splitext(filename)[1]
    return (file_extension in ALLOWED_EXTENSIONS), file, filename, file_extension


def get_file_extension(filename):
    return os.path.splitext(filename)[1]
