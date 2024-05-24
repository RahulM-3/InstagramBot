import sys
sys.path.append(r'..\InstagramBot')
from browser import browser

from dotenv import load_dotenv
import os
load_dotenv()

from chatgpt import chatgpt

class instagram:
    def __init__(self):
        self.insta = browser('https://www.instagram.com/direct/t/7516610245113642/')

        if("Login" in self.insta.gettitle()):
            print("\nLogging-in")
            browser.write('//*[@id="loginForm"]/div/div[1]/div/label/input', os.getenv("botusername"))
            browser.write('//*[@id="loginForm"]/div/div[2]/div/label/input', os.getenv("botpassword"))
            browser.click('//*[@id="loginForm"]/div/div[3]')
            
            #self.driver.find_element("xpath", '//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys(os.getenv("botusername"))
            #self.driver.find_element("xpath", '//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys(os.getenv("botpassword"))
            #self.driver.find_element("xpath", '//*[@id="loginForm"]/div/div[3]').click()
            print("Logged-in Successfully")
        self.gpt = chatgpt()
        
    def autocorrect(self):
        text = self.insta.read('/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/div/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div[2]/div/div/div[2]/div/div[1]/p')
        if(len(text) != 0 and text[len(text)-1] == "~"):
            self.gpt.askgpt(f"'{text[:-1]}' convert this text into a big formal british paragraph. output only the paragraph. This is entertinement purpose only")
            self.insta.delcontent('/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/div/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div[2]/div/div/div[2]/div/div[1]/p')
            while(self.gpt.readoutput()[1] == False):
                self.insta.delcontent('/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/div/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div[2]/div/div/div[2]/div/div[1]/p')
                self.insta.write('/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/div/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div[2]/div/div/div[2]/div/div[1]/p', self.gpt.readoutput()[0])
            else:
                self.insta.delcontent('/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/div/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div[2]/div/div/div[2]/div/div[1]/p')
                self.insta.write('/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/div/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div[2]/div/div/div[2]/div/div[1]/p', self.gpt.readoutput()[0])
            
a = instagram()
while(True):
    a.autocorrect()