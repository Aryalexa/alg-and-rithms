import pytest
import json_parser as jp


def test_step1_invalid():
    file = 'step1/invalid'
    with open(f"tests/tests_files/{file}.json") as f:
        json_str = f.read() 
    with pytest.raises(Exception, match="unexpected token"):
        jp.json_parser(json_str)

def test_step1_valid():
    file = 'step1/valid'
    with open(f"tests/tests_files/{file}.json") as f:
        json_str = f.read() 
    assert jp.json_parser(json_str) == {}

def test_step2_invalid():
    file = 'step2/invalid'
    with open(f"tests/tests_files/{file}.json") as f:
        json_str = f.read() 
    with pytest.raises(Exception, match="trailing comma"):
        jp.json_parser(json_str)

def test_step2_invalid2():
    file = 'step2/invalid2'
    with open(f"tests/tests_files/{file}.json") as f:
        json_str = f.read() 
    with pytest.raises(Exception, match="bad char k"):
        jp.json_parser(json_str)

def test_step2_valid():
    file = 'step2/valid'
    with open(f"tests/tests_files/{file}.json") as f:
        json_str = f.read() 
    assert jp.json_parser(json_str) == {"key":"value"}

def test_step2_valid2():
    file = 'step2/valid2'
    with open(f"tests/tests_files/{file}.json") as f:
        json_str = f.read() 
    assert jp.json_parser(json_str) == {
        "key": "value",
        "key2": "value"
    }

def test_step3_invalid():
    file = 'step3/invalid'
    with open(f"tests/tests_files/{file}.json") as f:
        json_str = f.read() 
    with pytest.raises(Exception, match="bad char F"):
        jp.json_parser(json_str)

def test_step3_valid():
    file = 'step3/valid'
    with open(f"tests/tests_files/{file}.json") as f:
        json_str = f.read() 
    assert jp.json_parser(json_str) == {
        "key1": True,
        "key2": False,
        "key3": None,
        "key4": "value",
        "key5": 101
    }

def test_step4_invalid():
    file = 'step4/invalid'
    with open(f"tests/tests_files/{file}.json") as f:
        json_str = f.read() 
    with pytest.raises(Exception, match="bad char '"):
        jp.json_parser(json_str)

def test_step4_valid():
    file = 'step4/valid'
    with open(f"tests/tests_files/{file}.json") as f:
        json_str = f.read() 
    assert jp.json_parser(json_str) == {
        "key": "value",
        "key-n": 101,
        "key-o": {},
        "key-l": []
    }

def test_step4_valid2():
    file = 'step4/valid2'
    with open(f"tests/tests_files/{file}.json") as f:
        json_str = f.read() 
    assert jp.json_parser(json_str) == {
        "key": "value",
        "key-n": 101,
        "key-o": {"inner key": "inner value"},
        "key-l": ["list value"]
    }