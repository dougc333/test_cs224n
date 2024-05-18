#monkeypatch fixture and we factor out MY_SETTINGS from 2 fns. 

import json
import test1


MY_SETTINGS = {"name":"bill"}


def test_read_settings(tmp_path,monkeypatch):
    monkeypatch.setattr(test1,"MY_PATH", tmp_path / '.my_fake_settings')
    test1.MY_PATH.write_text(json.dumps(MY_SETTINGS))
    assert test1.read() == MY_SETTINGS

def test_write_settings(monkeypatch, tmp_path):
    monkeypatch.setattr(test1,"MY_PATH", tmp_path / '.my_fake_settings')
    test1.write(MY_SETTINGS)
    retrieved_settings = eval(test1.MY_PATH.read_text())
    assert retrieved_settings == MY_SETTINGS


   
