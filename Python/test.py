import pytest
import newer

def test_add():
    assert newer.add(10, 5) == 15
def test_subtract():
    assert newer.subtract(10, 5) == 5
def test_multiply():
    assert newer.multiply(10, 5) == 50
def test_divide():
    try:
        assert newer.divide(10, 0) == 2
    except:
        AssertionError('cannot divide by zerooooo')        