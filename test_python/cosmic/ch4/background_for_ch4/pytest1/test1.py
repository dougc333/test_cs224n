import json
from pathlib import Path

MY_PATH=Path.home() / '.my_settings'

def write(settings):
    MY_PATH.write_text(json.dumps(settings))

def read():
    return json.loads(MY_PATH.read_text())

