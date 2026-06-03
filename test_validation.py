import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from sim import ask_ai

def test_ai_json():
    result = ask_ai("открой chrome")

    assert isinstance(result, dict)
    assert "action" in result