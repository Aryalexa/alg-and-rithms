import pytest
import json_parser as jp


def test_step1_invalid():
    file = 'step1/invalid'
    with open(f"tests/tests_files/{file}.json") as f:
        json_str = f.read() 
    with pytest.raises(Exception, match="bad start"):
        jp.json_parser(json_str)

def test_step1_valid():
    file = 'step1/valid'
    with open(f"tests/tests_files/{file}.json") as f:
        json_str = f.read() 
    assert jp.json_parser(json_str) == {}