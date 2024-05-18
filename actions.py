from browser import browser

from dotenv import load_dotenv
import os
load_dotenv()

class instagram:
    def __init__(self):

        if("Login" in browser.gettitle()):
            print("\nLogging-in")
            browser.write('//*[@id="loginForm"]/div/div[1]/div/label/input', os.getenv("botusername"))
            browser.write('//*[@id="loginForm"]/div/div[2]/div/label/input', os.getenv("botpassword"))
            browser.click('//*[@id="loginForm"]/div/div[3]')
            
            #self.driver.find_element("xpath", '//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys(os.getenv("botusername"))
            #self.driver.find_element("xpath", '//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys(os.getenv("botpassword"))
            #self.driver.find_element("xpath", '//*[@id="loginForm"]/div/div[3]').click()
            print("Logged-in Successfully")

    def getmessage(self, msgid):
        pass

    def sendmessage(self, msg):
        pass

    def replyto(self, msgid, msg):
        pass