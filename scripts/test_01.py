import pytest

from selenium.webdriver import Remote
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from pages.home import HomePage

class TestOne(object):
    def setup_method(self, method):
        self.driver = Remote(desired_capabilities=DesiredCapabilities().FIREFOX)
        self.home = HomePage(self.driver).open().wait_until_loaded()

    def teardown_method(self, method):
        self.driver.quit()
        
    @pytest.mark.pycon
    @pytest.mark.shallow
    def test_one(self):
        assert(self.home.speak_blurb_title == "SPEAK")

    @pytest.mark.pycon
    @pytest.mark.deep
    @pytest.mark.adam
    def test_one_b(self):
        schedule = self.home.go_to_schedule()
        assert(schedule.tuesday_fake_table_venue == "720 Bathurst Street, suite 500")
        
        
        
        
        
        
        
        
        
        
        
        
        