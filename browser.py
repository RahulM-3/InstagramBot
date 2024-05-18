from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

from dotenv import load_dotenv
import os
load_dotenv()

class browser:
    def __init__(self):
        # selenium setup
        options = Options()
        options.add_experimental_option('detach', True)
        options.add_argument(os.getenv("chromepath"))
        self.driver = webdriver.Chrome(options)
        self.driver.get("https://www.instagram.com/direct/t/7516610245113642/")

        if("Login" in self.driver.title):
            print("\nLogging-in")
            while(True):
                try:
                    self.driver.find_element("xpath", '//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys(os.getenv("botusername"))
                    self.driver.find_element("xpath", '//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys(os.getenv("botpassword"))
                    self.driver.find_element("xpath", '//*[@id="loginForm"]/div/div[3]').click()
                    #while(True):
                    #    try:
                    #        self.driver.find_element("xpath", '//*[@id="mount_0_0_i0"]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div/div').click()
                    #        break
                    #   except:
                    #        pass
                    break
                except:
                    pass
            print("Logged-in Successfully")
   
    def click(self, path):
        while(True):
            try:
                return self.driver.find_element("xpath", path).click()
            except:
                pass

    def read(self, path):
        while(True):
            try:
                return self.driver.find_element("xpath", path).text
            except:
                pass

    def write(self, path, text):
        while(True):
            try:
                self.driver.find_element("xpath", path).send_keys(text)
            except:
                pass

    def fineelement(self, path):
        while(True):
            try:
                return self.driver.find_element("xpath", path)
            except:
                pass

    def gettitle(self):
        while(True):
            try:
                return self.driver.title
            except:
                pass