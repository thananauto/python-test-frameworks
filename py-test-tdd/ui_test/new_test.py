import pytest
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from conf.conftest import init_browser


@pytest.mark.usefixtures("init_browser")
class BasicTest:
    pass

@pytest.mark.incremental
class Test_URL(BasicTest):
    def test_open_url(self):
        self.driver.get("https://www.lambdatest.com/")
        print(self.driver.title)
        sleep(5)

    def test_search_flight(self):
        wait = WebDriverWait(self.driver, 3)
        self.driver.get("http://blazedemo.com/")
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[value='Find Flights']"))).click()

    def test_choose_any_flight(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[value='Choose This Flight']"))).click()
        text = self.driver.find_element_by_tag_name("h2").text
        assert text == "Your flight from Paris to Buenos Aires has been reserved."


