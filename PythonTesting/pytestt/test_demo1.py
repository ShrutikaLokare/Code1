import pytest


@pytest.mark.smoke
def test_firstpro(setup):
    print("Hello  Pytest")


@pytest.mark.xfail
def test_firstpro1CreditCard():
    print('Good Morning')


def test_crossBrowser(crossBrowser):
    print(crossBrowser)
