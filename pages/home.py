from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from pages.schedule import Schedule

locators = {
    "speak blurb title": (By.CSS_SELECTOR, ".speak h2"),
    "schedule link": (By.CSS_SELECTOR, ".schedule .more-info")
}

class SpeakBlurbTitle(object):
    def __init__(self):
        self.locator = locators["speak blurb title"]
        
    def __set__(self, obj, val):
        pass

    def __get__(self, obj, cls=None):
        return obj.driver.find_element(*self.locator).text

class HomePage(object):
    speak_blurb_title = SpeakBlurbTitle()
    
    def __init__(self, driver):
        self.driver = driver
        
    def open(self):
        self.driver.get('http://www.pycon.ca')
        return self
        
    def wait_until_loaded(self):
        w = WebDriverWait(self.driver, 10)
        w.until(lambda driver: driver.find_element(*locators["speak blurb title"]))
        return self
        
    def go_to_schedule(self):
        self.driver.find_element(*locators["schedule link"]).click()
        return Schedule(self.driver).wait_until_loaded()
        
        
        
        
        
        
        
        
        
        
        
        