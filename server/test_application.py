import pytest

from application import TestMe

'''Take five unit test'''
def test_server():
    assert TestMe().take_five() == 5

'''Port unit test'''
def test_port():
    assert TestMe().port() == 8000
