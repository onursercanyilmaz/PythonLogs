# from extract_emails import EmailExtractor
# from extract_emails.browsers import RequestsBrowser
# z

# with RequestsBrowser() as browser:
#     email_extractor = EmailExtractor("https://izu.edu.tr", browser, depth=2)
#     emails = email_extractor.get_emails()


# for email in emails:
#     print(email)
#     print(email.as_dict())


#%%
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time 
from time import sleep



class ExtractMail:
    def __init__(self):
        
     
        self.driver = webdriver.Chrome()
        self.driver.get("https://akademik.yok.gov.tr/AkademikArama/")
      
        self.driver.find_element_by_link_text('Mühendislik').click()
        sleep(4)
        
        i=1
        
        while i<=3000:
      
            self.driver.find_element_by_xpath("//button[contains(text(), 'Aktar')]").click()
            sleep(2)
                    
            self.driver.find_element_by_link_text('Excel').click()
            sleep(2)
                    
            self.driver.find_element_by_link_text(str(i+1)).click()
            sleep(2)
            
            if ((i+1) % 10==0):
                self.driver.find_element_by_link_text('»').click()
                sleep(4)
         
            
            i=i+1
            
                
        
            
        
        self.driver.find_element_by_link_text('»').click()
        sleep(4)
      
  
            
ExtractMail()
