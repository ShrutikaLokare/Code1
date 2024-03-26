import pytest


# to do pre requisite and post execution for every step

# @pytest.fixture()  # to define fixture
# def setup():       #to execute pre requisuite steps
#   print("I will execute first")
#   yield          #to execute post executions steps
#   print("I will execute last")

# to do pre requisite and post execution for one time when starting the class and ending the class

@pytest.fixture(scope="class")  # to define fixture and scope="class" to not run for everytime
def setup():  # to execute pre requisuite steps
    print("I will execute first")
    yield  # to execute post executions steps
    print("I will execute last")


# to load the data using fixtures
@pytest.fixture()
def Loaddata():
    print("user profile data is being created")
    return ["shrutika", "lokare", "shrutikalokare@gmail.com"]


@pytest.fixture(params=["chrome", "Firefox", "IE"])
def crossBrowser(request):
    return request.param
