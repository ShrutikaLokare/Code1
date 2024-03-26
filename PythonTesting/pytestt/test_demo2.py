import pytest


#@pytest.mark.smoke
#@pytest.mark.skip
def test_firstpro2():
    msg = "Hello"
    assert msg == "Hi", "strings do not match"


def test_secondproCreditCard():
    a = 4
    b = 5
    assert a + 4 == 8, "addition do not match"
