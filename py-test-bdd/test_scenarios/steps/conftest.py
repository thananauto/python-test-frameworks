import pytest
from selenium import webdriver

@pytest.fixture(scope='module')
def browser_driver():
    print('calling inside every steps')
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

