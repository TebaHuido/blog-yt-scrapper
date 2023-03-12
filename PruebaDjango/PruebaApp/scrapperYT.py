import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pandas as pd
import time

class Video:
    instances = []
    def __init__(self, title, id, channel):
        self.channel = channel
        self.title = title
        self.id = id
        _current_index = 0
        self.__class__.instances.append(self)
    def __iter__(self):
        return self
    def __next__(self):
        if len(self.instances) < self._current_index:
            return self.instances[self._current_index]
        else:
            raise StopIteration
    def __str__(self):
        return self.title + " " + self.id + " " + self.channel
def scrapChannel(channel : str,limite):
    options=Options()
    options.headless=False
    driver=webdriver.Chrome(executable_path=r'chromedriver', options=options)
    driver.get("https://www.youtube.com/@"+channel+"/videos")
    driver.maximize_window()

    last_height = driver.execute_script("return document.documentElement.scrollHeight")
    while True:
        time.sleep(2)
        videos = driver.find_elements("xpath",'//*[@id="video-title-link"]')
        if len(videos)>=limite+1 :
            break
        driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
        new_height = driver.execute_script("return document.documentElement.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height
        
    n=0
    for video in videos:
        if(video.get_attribute("href")!= None):
            Video(video.get_attribute("title"),video.get_attribute("href")[32 : 43],channel)
    return Video.instances[0:limite]