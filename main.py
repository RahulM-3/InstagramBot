from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from time import sleep

from dotenv import load_dotenv
import os
load_dotenv()


class instagrambot:
    def __init__(self):
        options = Options()
        options.add_experimental_option('detach', True)
        options.add_argument(os.getenv("chromepath"))
        self.driver = webdriver.Chrome(options)
        self.driver.get("https://www.instagram.com/direct/t/7516610245113642/")
        if("Login" in self.driver.title):
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
        
    def getcommand(self) -> None:
        sleep(1)
        for i in range(1, 10):
            print("Text in", i)
            print(self.driver.find_element("xpath", f'/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/div/div/div/div[1]/div/div[2]/div/div/div[1]/div/div/div/div[2]/div/div/div[1]/div/div/div/div/div/div/div[3]/div/div[{i}]').text)
            print()
        
if(__name__ == "__main__"):
    bot = instagrambot()
    bot.getcommand()