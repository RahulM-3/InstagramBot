from time import sleep

from dotenv import load_dotenv
import os
load_dotenv()

from google_gemini import askgemini

class instagrambot:
    def __init__(self):
        self.cmdlookup = 1
        self.chatend = -1
        
        print("\nActivating Bot")
        sleep(10)
        activatemsg = "Cancer Bot Online, Ready to receive commands!"
        self.driver.find_element("xpath", '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/div/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div[2]/div/div/div[2]/div/div[1]/p').send_keys(activatemsg)
        self.driver.find_element("xpath", '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/div/div/div/div[1]/div/div[2]/div/div/div[1]/div/div/div/div[2]/div/div/div[2]/div/div/div[3]').click()
        sleep(0.5)
        while(True):
            msg = self.getmessage()
            print(msg)
            if(msg[0] == "You sent" and msg[1] == activatemsg):
                break
        print("Bot Activated Successfully")

    def getmessage(self, lookup=0) -> tuple:
        i = lookup
        if(lookup == 0):
           i = self.cmdlookup
        try:
            if(self.chatend == i):
                return (None, None, -1)
            msg = self.driver.find_element("xpath", f'/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/div/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div[1]/div/div/div/div/div/div/div[3]/div/div[{i}]').text
            msg = list(msg.split("\n"))
            if(lookup == 0):
                self.cmdlookup += 1
            if(len(msg) == 1):
                return (None, msg, -1)
            user = msg[0]
            message = msg[1]
            if(len(msg) == 4):
                user = msg[1]
                message = msg[2]
            return (user, message, i)
        
        except Exception as err:
            self.chatend = i
            return (None, None, -1)
    
    def replyto(self, msgid, msg) -> None:
        self.driver.find_element("xpath", f'/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/div/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div[1]/div/div/div/div/div/div/div[3]/div/div[{msgid}]').click()
        self.driver.find_element("xpath", f'/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/div/div/div/div[1]/div/div[2]/div/div/div[1]/div/div/div/div[2]/div/div/div[1]/div/div/div/div/div/div/div[3]/div/div[{msgid}]/div/div/div/div[1]/div/div/div[2]/div[2]/div/div/div/div[2]').click()

        self.driver.find_element("xpath", '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/div/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div[2]/div/div/div[2]/div/div[1]/p').send_keys(msg)
        #self.driver.find_element("xpath", '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/div/div/div/div[1]/div/div[2]/div/div/div[1]/div/div/div/div[2]/div/div/div[2]/div/div/div[3]').click()
        
    def askmecmd(self, prompt, msgid, msg):
        print(msg)
        response = askgemini(prompt).replace("*", '')
        response = response.replace("\n", '')
        print(response)
        #self.replyto(msgid, response)

if(__name__ == "__main__"):
    bot = instagrambot()

    while(True):
        msg = bot.getmessage(bot.cmdlookup)
        if(msg[0] and "/askme" in msg[1]):
            print("Starint to prompt")
            bot.askmecmd(msg[1].replace("/askme", ""), msg[2], msg)
            print("Done")
        sleep(1)