# app.py
# This is a test commit to check if the CI pipeline is working correctly.
def add(a, b):
    return a + b

def test_add():
    assert add(1, 3) == 4
    assert add(1, -1) == 0
    assert add(0, 0) == 0
    assert add(-1, -1) == -2
    assert add(1.5, 2.5) == 4.0
