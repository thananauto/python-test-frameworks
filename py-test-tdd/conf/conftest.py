import pytest
from selenium import webdriver

url = "https://reqres.in/api"

#fixture for API test
@pytest.fixture(scope="class")
def api_url():
	if True:
		print('........calling every time....')
		return url


# fixture for UI test
@pytest.fixture(scope="class")
def init_browser(request):
	driver = webdriver.Chrome("C:\\projects\\python-workspace\\drivers\\chromedriver.exe")
	request.cls.driver = driver
	yield
	driver.quit()


def pytest_runtest_makereport(item, call):
    if "incremental" in item.keywords:
        if call.excinfo is not None:
            parent = item.parent
            parent._previousfailed = item

def pytest_runtest_setup(item):
    if "incremental" in item.keywords:
        previousfailed = getattr(item.parent, "_previousfailed", None)
        if previousfailed is not None:
            pytest.xfail("previous test failed (%s)" %previousfailed.name)

# write all fixtures for other tests.......



