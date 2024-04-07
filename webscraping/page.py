from element import BasePageElement
from locators import BasePageLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import random
class SearchInputElement(BasePageElement):
    locator = 'twotabsearchtextbox'

class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

class MainPage(BasePage):

    SearchInput = SearchInputElement()
  
    def titleIsTrue(self):
        return "Amazon" in self.driver.title

    def clickGoButton(self):
        element = self.driver.find_element(*BasePageLocators.GO_BUTTON)
        element.click()


class SearchResultPage(BasePage):
    def clickGoDetailProduct(self):
        driver = self.driver
        links = driver.find_elements(
            By.XPATH , '//div[@class="aok-relative"]/span[@class="rush-component"]/a[1]')
        
        productLinks = [link.get_attribute('href') for link in links]

        productsDetail = []

        suppliers = {}
        
        cnt =0
        for link in productLinks:
            if cnt ==1:
                break
            driver.get(link)
            WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.ID, 'centerCol'))
            )

            productDetail = driver.find_element(By.ID, 'centerCol')

            title = productDetail.find_element(By.ID, 'productTitle')
            price = productDetail.find_element(By.CLASS_NAME, 'a-price-whole')
            productType = self.driver.find_element(*BasePageLocators.GO_BUTTON) 
            brand=title.text.split(' ')[0]
            check =0
            for supplier in suppliers:
                if supplier==brand:
                    check=1
                    break
            if check==0:
                suppliers[brand]=random.randint(1000,1100)

                
            supplierID=suppliers[brand]
            productID=random.randint(10000,99999)
            

            data={
                'supplierID':str(supplierID),
                'productID':str(productID),
                'title': title.text,
                'stock:':random.randint(10000,1000000),
                'price': price.text,
                'productType': 'gaming keyboard',
                'brand':brand,
                }
            productsDetail.append(data)

            driver.back()
            cnt+=1
        return productsDetail
