#get_ipython().system('pip install splinter')



# Dependencies
# https://splinter.readthedocs.io/en/latest/drivers/chrome.html
from splinter import Browser
from bs4 import BeautifulSoup as bs

import requests
import pymongo
import re



from splinter import Browser
executable_path = {'executable_path':'/usr/local/bin/chromedriver'}

browser = Browser('chrome', **executable_path, headless=False )




def init_browser():
   # @NOTE: Replace the path with your actual path to the chromedriver
   executable_path = {"executable_path": "/usr/local/bin/chromedriver/chromedriver.exe"}
   return Browser("chrome", **executable_path, headless=False)



# Initialize PyMongo to work with MongoDBs
conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)



# Define database and collection
db = client.nasa_news
collection = db.misson_to_mars


# # NASA Mars News




#def mars_news():
title_text = []
para_text = []
url = 'https://mars.nasa.gov/news/'
browser.visit(url)
# Retrieve page with the requests module
response = requests.get(url)
# Create a Beautiful Soup object
soup = bs(response.text, 'html.parser')
news_title = soup.title.text
title_text.append(news_title)
print(title_text)
# Print all paragraph texts
paras = soup.find_all(class_="content_title")
for para in paras:
    ptext = para.find('_self')
    ptext = para.text.strip()
    para_text.append(ptext)
    print(para_text)
    #return (title_text ,para_text)
#test = mars_news()
#print(test)


# # JPL Mars Space Images - Featured Image

from splinter import Browser
from bs4 import BeautifulSoup
import time
#def Mars_Featured_image():
browser = Browser('chrome', headless=False)
url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
browser.visit(url)
html = browser.html
# create a soup object from the html
img_soup = BeautifulSoup(html, "html.parser")
featured_image_url= 'https://www.jpl.nasa.gov/' + img_soup.find(class_="button fancybox")['data-fancybox-href']
print(featured_image_url)
    #return (featured_image_url)
#test = Mars_Featured_image()
#print(test)

# # Mars Weather - get latest Mars weather tweet

# def Mars_latest_tweet():
url = "https://twitter.com/MarsWxReport?lang=en"
response = requests.get(url)
soup = bs(response.text, 'lxml') 
latest_tweet = soup.title.text
mars_weather = soup.find(class_="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text")
print(mars_weather)
#return (mars_weather)
#test=Mars_latest_tweet()
#print(test)


# # Mars Facts
# Visit the Mars Facts webpage here and use Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc.
# Use Pandas to convert the data to a HTML table string.



#def mars_Facts():
import pandas as pd
url = "http://space-facts.com/mars/"
response = requests.get(url)
soup = bs(response.text, 'html.parser')
type(soup)
tables = pd.read_html(url)
tables
df = tables[0]
df.columns = ['Description' ,'Value']
df.head()
#Use Pandas to convert the data to a HTML table string.
html_table = df.to_html()
html_table
facts_table = html_table.replace('\n', '')
facts_table
type(facts_table)
#lets save this table to a file
df.to_html('table.html')
get_ipython().system('open table.html')
    #return()
#test = mars_Facts()


# # Mars Hemisperes

# Visit the USGS Astrogeology site here to obtain high resolution images for each of Mar's hemispheres.
# You will need to click each of the links to the hemispheres in order to find the image url to the full resolution image.
# Save both the image url string for the full resolution hemipshere image, and the Hemisphere title containing the hemisphere name. Use a Python dictionary to store the data using the keys img_url and title.
# Append the dictionary with the image url string and the hemisphere title to a list. This list will contain one dictionary for each hemisphere.


# URL of page to be scraped
url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
 
browser.visit(url)

# Retrieve page with the requests module
response = requests.get(url)
# Create BeautifulSoup object; parse with 'lxml'
soup = BeautifulSoup(response.text, 'lxml')

hemisphere_image_urls = []
results = soup.find_all('a', class_='itemLink product-item')
for result in results:
    print("=================")
    
    hemisphere_title = result.find('h3').get_text()
    print(hemisphere_title)
    
    new_url = "https://astrogeology.usgs.gov" + result['href']
    browser.visit(new_url)
    print(new_url)
    
    # Retrieve page with the requests module
    response2 = requests.get(new_url)
 
    browser2 = Browser('chrome', headless=False)
    soup2 = BeautifulSoup(response2.text, 'lxml')
    
    next_page = soup2.find('div', class_='downloads')
    #print(next_page)
    
    
    link = next_page.find('a')['href']
    #print(link)
    hemisphere_url = link
    #print("This is ")
    print(hemisphere_url)
    
    hemisphere_image_urls.append({'title': hemisphere_title, 'img_url': hemisphere_url})

print("=====================================================")
print(hemisphere_image_urls)
print("=====================================================")


hemisphere_image_urls

# # Step 2 - MongoDB and Flask Application

# Create a dictionary with all of the above scraped variables 
mars_scrape_data = {'hemispheres': hemisphere_image_urls,
                    'facts': facts_table,
                    'mars_weather': mars_weather,
                    "featured_image_url": featured_image_url,
                    'news_title': title_text,
                    'news_text': para_text}

mars_scrape_data
 
type(mars_scrape_data)

mars_scrape_data["news_text"]

mars_scrape_data["hemispheres"][-1]

