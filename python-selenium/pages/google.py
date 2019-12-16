from utilities.webapp import webApp
from selenium.webdriver.common.keys import Keys

class Google:
    instance = None

    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = Google()

        return cls.instance

    def __init__(self):
        self.driver = webApp.get_driver()

    def launch_application(self, url):
        self.driver.get(url)

    def search_google(self, keyword):
        self.driver.find_element_by_css_selector("input[name=q]").send_keys(keyword)
        self.driver.find_element_by_css_selector("input[name=q]").send_keys(Keys.ENTER)


    def search_amazon(self, keyword):
        self.driver.find_element_by_id("twotabsearchtextbox").send_keys(keyword)
        self.driver.find_element_by_id("twotabsearchtextbox").send_keys(Keys.ENTER)

    def product_list_page(self):
        product_list = self.driver.find_elements_by_class_name("sg-col-inner")
        assert len(product_list)>=1, "Search page didn't retrieve any results"

    def google_list_page(self):
        search_list = self.driver.find_elements_by_tag_name("h3")
        assert len(search_list) >= 1, "Search page didn't retrieve any results"

google = Google.get_instance()