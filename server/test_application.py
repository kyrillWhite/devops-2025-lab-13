import pytest

from application import TestMe

def test_server():
    """Take five unit test"""
    assert TestMe().take_five() == 5

def test_port():
    """Port unit test"""
    assert TestMe().port() == 8000
