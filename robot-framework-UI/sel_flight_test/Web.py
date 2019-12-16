from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from sel_flight_test.WebDriverManager import WebDriverManager

class Web(object):

    __driver = None

    def __init__(self, browser):
           self.__driver = WebDriverManager.get_web_driver(browser)
           self.__wait = WebDriverWait(self.__driver, 10)

    def get_web_element_by_xpath(self, xpath):
        return self.__wait.until(EC.presence_of_element_located((By.XPATH, xpath)))

    def get_web_elements_by_xpath(self, xpath):
        return self.__wait.until(EC.presence_of_all_elements_located((By.XPATH, xpath)))

    def click_button(self, identifier, properties):
        self.__driver.find_element(identifier, properties).click()

    def open(self, path):
        self.__driver.get(path)

    def close_all(self):
        self.__driver.quit()


