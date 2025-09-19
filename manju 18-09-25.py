#program to open any website
from random import*
import webbrowser
import time
list=['google.com','youtube.com','gmail.com','rediff.com','bing.com','flipkart.com']
while True:
    site=choice(list)
    webbrowser.open(f'http://{site}')
    sec=randint(5,20)
    time.sleep(sec)