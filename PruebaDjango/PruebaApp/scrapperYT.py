import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pandas as pd
import time
def scrapSelenium():
    options=Options()
    options.headless=False
    driver=webdriver.Chrome(executable_path=r'chromedriver', options=options)
    driver.get("https://www.youtube.com/@FusgoTV/videos")
    driver.maximize_window()

    last_height = driver.execute_script("return document.documentElement.scrollHeight")
    while True:
        driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
        time.sleep(2)
        new_height = driver.execute_script("return document.documentElement.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height
    videos = driver.find_elements("xpath",'//*[@id="video-title-link"]')
    for video in videos:
        if(video.get_attribute("href")!= None):
            print(video.get_attribute("href"))
scrapSelenium()


def try1():
    page = requests.get("https://www.youtube.com/@FusgoTV/videos")
    soup = BeautifulSoup(page.content, 'html.parser')
    print ("quee")
    #listalinks = soup.find_all()
    for a in soup.find_all(class_ = 'yt-simple-endpoint inline-block style-scope ytd-thumbnail', href=True):
        print("Found the URL:", a['href'])