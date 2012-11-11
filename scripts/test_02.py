import pytest

import selenium.webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from pages.home import HomePage

from browsermobproxy import Client

class TestTwo(object):
    def setup_method(self, method):
        self.client = Client('http://localhost:8080')
        
        profile  = selenium.webdriver.FirefoxProfile()
        profile.set_proxy(self.client.webdriver_proxy())
        
        self.driver = selenium.webdriver.Firefox(firefox_profile=profile)
        
    def teardown_method(self, method):
        self.driver.quit()
        self.client.close()
        
    @pytest.mark.pycon
    @pytest.mark.deep
    @pytest.mark.blacklist
    def test_one(self):
        self.client.blacklist("http://www\\.google-analytics\\.com/.*", 309)
        self.client.new_har()
        home = HomePage(self.driver).open().wait_until_loaded()
        har = self.client.har
        print(har)
        
        
        
        
        
        
        
        
        
        
        
        
        