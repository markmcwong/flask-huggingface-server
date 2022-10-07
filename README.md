## Installing
1. `python3 -m venv .venv` to create virtual environment
2. `source .venv/bin/activate` to activate the virtual environment
3. `pip install -r requirements.txt` to install requirements for the project

## Running / Starting the backend API

Run `python3 app.py` in the project root folder

## Testing different pretrained model

Find your favourite pretrained model name through [huggingface.co](https://huggingface.co) and Edit `app.py`'s `startup_event > model_name` accordingly
