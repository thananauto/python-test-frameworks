from selenium import webdriver

class WebDriverManager:
    __driver = None

    @classmethod
    def get_web_driver(cls, browser):
        if cls.__driver is None:
            if(browser.lower()) == 'chrome':
                cls.__driver = webdriver.Chrome("C:\\projects\\python-workspace\\drivers\\chromedriver.exe")

        return cls.__driver