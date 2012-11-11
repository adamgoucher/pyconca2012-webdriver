from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

locators = {
    "tuesday block": (By.ID, "tuesday"),
    "tuesday fake table venue": (By.XPATH, '//h2[@id="tuesday"]/following-sibling::div//a[3]')
}

class TuesdayFakeTableVenue(object):
    def __init__(self):
        self.locator = locators["tuesday fake table venue"]
        
    def __set__(self, obj, val):
        pass

    def __get__(self, obj, cls=None):
        e = obj.driver.find_element(*self.locator)
        return obj.driver.execute_script('return arguments[0].textContent', e)
        
class Schedule(object):
    tuesday_fake_table_venue = TuesdayFakeTableVenue()
    
    def __init__(self, driver):
        self.driver = driver
        
    def open(self):
        self.driver.get('http://pycon.ca/schedule')
        return self
        
    def wait_until_loaded(self):
        w = WebDriverWait(self.driver, 10)
        w.until(lambda driver: driver.find_element(*locators["tuesday block"]))
        return self
        
    def get_title(self):
        self.driver.find_element(*locator(["schedule link"])).click()
        return Schedule().wait_until_loaded()
