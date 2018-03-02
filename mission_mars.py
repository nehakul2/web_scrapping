import time
from splinter import Browser
from selenium import webdriver
from bs4 import BeautifulSoup as bs

import requests
import pymongo
import re

from selenium import webdriver
driver = webdriver.Chrome()

import mission_to_mars

driver = webdriver.Chrome('/usr/local/bin/chromedriver')
def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
    return Browser("chrome", **executable_path, headless=False)

def scrape():
    browser = init_browser()
    scrape_data = mission_to_mars.mars_scrape_data 
    print(scrape_data)
    return scrape_data