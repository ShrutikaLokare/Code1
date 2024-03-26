# fixture = used to create pre requisite stuff and post execution stuff

import pytest


@pytest.mark.usefixtures("setup")     #to use fixture "setup" in all the methods declared in the class
class TestExample:                  #declared a class
    def test_fixtureDemo1(self):
        print("I will execute1")

    def test_fixtureDemo2(self):
        print("I will execute2")

    def test_fixtureDemo4(self):
        print("I will execute4")
