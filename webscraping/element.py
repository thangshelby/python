from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from locators import BasePageLocators



class BasePageElement(object):
    def __set__(self, obj, value):
        driver = obj.driver
        WebDriverWait(driver, 10).until(
            lambda driver: driver.find_element(*BasePageLocators.GO_INPUT)
        )
        driver.find_element(By.ID, self.locator).clear()
        driver.find_element(By.ID, self.locator).send_keys(value)




    
      
            







