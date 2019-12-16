import pytest
from conf.conftest import init_browser
from time import sleep

@pytest.mark.usefixtures("init_browser")
class BasicTest:
    pass

@pytest.mark.incremental
class Test_(BasicTest):

    def test_launch_url(self):
        self.driver.get("https://www.lambdatest.com/")
        print(self.driver.title)
        assert 0

    def test_open_url(self):
        self.driver.get("https://www.google.com")
        print(self.driver.title)

        sleep(5)



