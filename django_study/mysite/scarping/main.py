
from selenium import webdriver
from .page import MainPage


class InstagramScraping(object):
    userName=''
    def setUp(self) :
        print('test',self.userName)
        self.driver= webdriver.Chrome()
        # self.driver.get('https://www.instagram.com/'+self.userName)
        self.driver.get('http://localhost:5173/auth/sign-in')
    
    def test_Search_Test(self):
        mainpage= MainPage(self.driver)
        # self.assertTrue(mainpage.titleIsTrue(self.userName))
        imgAvatar= mainpage.getImgAvatar()
        print(imgAvatar)
   
   
    def tearDown(self):
        print('success')
        self.driver.quit()


def startScraping(userName):
    driver= webdriver.Chrome()
    driver.get('https://www.instagram.com/'+userName)
    mainpage= MainPage(driver)
    imgAvatar= mainpage.getImgAvatar()
    posts= mainpage.getPosts(3)
    print(posts)


    
    # InstagramScraping.userName=userName
    # unittest.main() 



