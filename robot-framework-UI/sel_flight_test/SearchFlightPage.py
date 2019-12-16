
from sel_flight_test.Web import Web
from selenium.webdriver.common.by import By

class SearchFlightPage:
    __url = "http://blazedemo.com/"

    def open(self):
        self._web.open(self.__url)

    def __init__(self, browser):
        self._web = Web(browser)

    def select_departure_city(self, city):
        self._web.get_web_element_by_xpath("//select[@name='fromPort']/option[@value='{}']".format(city)).click()

    def select_destination_city(self, city):
        self._web.get_web_element_by_xpath("//select[@name='toPort']/option[@value='{}']".format(city)).click()

    def search_for_flights(self):
        self._web.get_web_element_by_xpath("//input[@type='submit']").click()

    def get_found_flights(self):
        return self._web.get_web_elements_by_xpath("//table[@class='table']/tbody/tr")

    def submit_the_login(self):
        self._web.click_button(By.CSS_SELECTOR, "input[type='submit']")

    def close(self):
        self._web.close_all()