import sys
sys.path.append(r'..\InstagramBot')
from browser import browser

class chatgpt:
    def __init__(self):
        self.gpt = browser("https://chatgpt.com/", firefox=True)
        self.output = 1
    
    def askgpt(self, prompt):
        self.gpt.write('/html/body/div[1]/div[1]/div[2]/main/div[1]/div[2]/div[1]/div/form/div/div[2]/div/div/div[2]/textarea', prompt)
        self.gpt.click('/html/body/div[1]/div[1]/div[2]/main/div[1]/div[2]/div[1]/div/form/div/div[2]/div/div/button')
        self.output += 2
        return True

    def readoutput(self):
        completed_path = f'/html/body/div[1]/div[1]/div[2]/main/div[1]/div[1]/div/div/div/div/div[{self.output}]/div/div/div[2]/div/div[2]'
        read_path = f'/html/body/div[1]/div[1]/div[2]/main/div[1]/div[1]/div/div/div/div/div[{self.output}]/div/div/div[2]/div/div[1]/div/div/div/p'
        while(not self.gpt.isloded(completed_path)):
            return (self.gpt.read(read_path), False)
        return (self.gpt.read(read_path), True)