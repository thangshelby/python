
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

class BasePage ():
    def __init__(self,driver):
        self.driver= driver

class Post(object):
    title=''
    # imgLink=''
    def __init__(self,title) -> None:
        self.title=title
        # self.imgLink=imgLink

class MainPage(BasePage):
    def  titleIsTrue(userName):
        return 'Instagram/'+userName
    
    def getImgAvatar(self):
        WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "img")))    
        imgAvatar= self.driver.find_element(By.TAG_NAME,'img')
        return imgAvatar.get_attribute('src')
    
    def getPosts(self,target):
        response =[]
        root = WebDriverWait(self.driver,10).until(
            EC.presence_of_all_elements_located((By.TAG_NAME,'article'))
        )
        # print(root.getattribute('text'))
        postList=self.driver.find_elements(By.CLASS_NAME,'_aagu')
        
        for postItem in postList:
            if len(response)== target:
                return response
            post= postItem.find_element(By.TAG_NAME,'img')
            if (post):
                response.append(post.get_attribute('alt'))


        




    
