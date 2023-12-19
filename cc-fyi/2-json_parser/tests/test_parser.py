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