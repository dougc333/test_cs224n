import json


import json
import tempfile
from pathlib import Path

import test1
#no fixtures

def test_read_no_fixtures():
    old_path = test1.MY_PATH
    try:
        with tempfile.TemporaryDirectory() as tmpdir:
            test1.MY_PATH = Path(tmpdir) / '.my_fake_settings'
            fake_settings= {'name' : 'bob' }
            test1.MY_PATH.write_text(json.dumps(fake_settings))
            assert test1.read() == fake_settings
    finally:
        test1.MY_PATH == old_path

def test_write_no_Fixtures():
    old_path = test1.MY_PATH
    try:
        with tempfile.TemporaryDirectory() as tmpdir:
            test1.MY_PATH = Path(tmpdir) / '.my_fake_settings'
            fake_settings= {'name' : 'sam' }
            test1.MY_PATH.write_text(json.dumps(fake_settings))
            retrieved_settings = test1.MY_PATH.read_text()
            assert eval(retrieved_settings) == fake_settings
    finally:
        test1.MY_PATH == old_path
#use yield when you want to return and undo things after test


