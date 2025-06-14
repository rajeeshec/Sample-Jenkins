import pytest
from app import add, subtract

def test_add():
    assert add(2, 4) == 6

def test_subtract():
    assert subtract(5, 3) == 2
