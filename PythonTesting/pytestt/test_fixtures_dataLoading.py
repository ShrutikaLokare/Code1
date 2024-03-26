import pytest

from pytestt.baseClass import baseClass


@pytest.mark.usefixtures("Loaddata")

class TestExampleData(baseClass):

    def test_editProfile(self, Loaddata):
        log = self.getlogger()
        log.info(Loaddata[0])
        log.info(Loaddata[1])