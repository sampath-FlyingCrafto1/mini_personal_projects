
from bot1 import spammingBot

with open('D:\work\Projects\Bot\text.txt','r') as txt :
    content = txt.read()
    for word in content.split(" "):
        print(word)
        spammingBot(word)
