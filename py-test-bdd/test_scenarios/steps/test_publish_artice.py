from pytest_bdd import scenario, given, when, then, parsers
from selenium.webdriver.common.keys import Keys
from pytest_bdd import scenarios


@scenario('../features/publish_article.feature', 'Basic DuckDuckGo Search')
def test_publish():
   pass

scenarios('../features')


DUCKDUCKGO_HOME = 'https://duckduckgo.com/'

# Given Steps

@given('the DuckDuckGo home page is displayed')
def ddg_home(browser_driver):
    print('Inside the first method')
    browser_driver.get(DUCKDUCKGO_HOME)


# When Steps

@when(parsers.parse('the user searches for "{phrase}"'))
def search_phrase(browser_driver, phrase):
    search_input = browser_driver.find_element_by_name('q')
    search_input.send_keys(phrase + Keys.RETURN)


# Then Steps

@then(parsers.parse('results are shown for "{phrase}"'))
def search_results(browser_driver, phrase):
    links_div = browser_driver.find_element_by_id('links')
    assert len(links_div.find_elements_by_xpath('//div')) > 0
    search_input = browser_driver.find_element_by_name('q')
    assert search_input.get_attribute('value') == phrase