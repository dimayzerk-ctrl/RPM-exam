import pytest
from sim import contains_wake_word, extract_command

def test_wake_word():
    assert contains_wake_word("сим открой браузер") == True

def test_extract_command():
    assert extract_command("сим открой хром") == "открой хром"

def test_empty_command():
    assert extract_command("сим") == ""

def test_invalid_wake_word():
    assert contains_wake_word("привет") == False