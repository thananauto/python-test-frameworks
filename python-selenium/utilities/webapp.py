from data.config import settings
from selenium import webdriver
import os

class WebApp:
    instance = None

    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = WebApp()
        return cls.instance

    def __init__(self):
        if str(settings['browser']).lower() is "chrome":
            self.driver = webdriver.Chrome(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'chromedriver.exe'))
        elif str(settings['browser']).lower() is "firefox":
            self.driver = webdriver.Firefox()
        else :
             self.driver = webdriver.Chrome(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'chromedriver.exe'))

        self.driver.implicitly_wait(settings['timeout'])

    def get_driver(self):
        return self.driver


webApp = WebApp.get_instance()
