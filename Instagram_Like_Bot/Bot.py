
#%%
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time 
from time import sleep


class InstaBot:
    def __init__(self, username, password):
        
        self.username = username
        self.password = password
        self.driver = webdriver.Firefox()
        self.driver.get("https://www.instagram.com/accounts/login/?source=auth_switcher")
        sleep(4)
        self.driver.find_element_by_xpath("//input[@name=\"username\"]")\
            .send_keys(username)
        self.driver.find_element_by_xpath("//input[@name=\"password\"]")\
            .send_keys(password)
        self.driver.find_element_by_xpath('//button[@type="submit"]')\
            .click()
        sleep(4)
        self.driver.find_element_by_xpath("//button[contains(text(), 'Şimdi Değil')]")\
            .click()
        sleep(4)
        self.driver.find_element_by_xpath("//button[contains(text(), 'Şimdi Değil')]")\
            .click()
        sleep(4)
        
        
    def searchHashtag(self, hashtag):
           
            self.driver.get("https://www.instagram.com/explore/tags/"+hashtag)
            
    def likePhotos(self,amount):
        self.driver.find_element_by_class_name('v1Nh3').click()
        
        i=1
        while i <= amount:
            time.sleep(7)
            self.driver.find_element_by_class_name("fr66n").click()
            self.driver.find_element_by_class_name("coreSpriteRightPaginationArrow").click()
            i+=1
            
insta = InstaBot('Your_UserName', 'Your_Password')


insta.searchHashtag("tech")
insta.likePhotos(100)