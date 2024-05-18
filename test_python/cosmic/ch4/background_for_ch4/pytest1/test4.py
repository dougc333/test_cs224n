#factor out the MY_SETTINGS from test3 into conftest.py

import json, pytest, test1

@pytest.fixture
def my_settings():
    print(f"\n my_settings fixture in {__file__}")
    return {"name":"foo"}


def test_read_settings(tmp_path,monkeypatch,my_settings):
    monkeypatch.setattr(test1,"MY_PATH", tmp_path / '.my_fake_settings')
    test1.MY_PATH.write_text(json.dumps(my_settings))
    assert test1.read() == my_settings

def test_write_settings(monkeypatch, tmp_path,my_settings):
    monkeypatch.setattr(test1,"MY_PATH", tmp_path / '.my_fake_settings')
    test1.write(my_settings)
    retrieved_settings = eval(test1.MY_PATH.read_text())
    assert retrieved_settings == my_settings


   
