from splinter import Browser
from bs4 import BeautifulSoup
import re
import time
import requests
import pandas as pd

def scrape():

    executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
    browser = Browser('chrome', **executable_path, headless=False)
    
# Scrape the NASA Mars News Site and collect the latest News Title and Paragraph Text.

    news_url = "https://mars.nasa.gov/news/"
    browser.visit(news_url)

    time.sleep(1)

    html= browser.html
    soup = BeautifulSoup(html, "html.parser")

    news_result = soup.select_one("ul.item_list li.slide")
    news_title = result.find("div", class_="content_title").get_text()
    news_p = result.find("div", class_="article_teaser_body").get_text()

# Use splinter to navigate the site and find the image url for the current Featured Mars Image

    image_url = "https://www.jpl.nasa.gov/spaceimages"
    browser.visit(image_url)

    for x in range(1):
        # HTML object
        html = browser.html
        # Parse HTML with Beautiful Soup
        soup = BeautifulSoup(html, "html.parser")
        articles = soup.find_all("article", class_="carousel_item")   
    
    featured_image_url = "https://www.jpl.nasa.gov/spaceimages"+"/images/wallpaper/PIA19092-1920x1200.jpg"

#  Visit the Mars Weather twitter account and scrape the latest Mars weather tweet from the page   

    tweet_url = "https://twitter.com/marswxreport?lang=en"

    browser.visit(tweet_url)

    time.sleep(5)
    html= browser.html
    soup = BeautifulSoup(html, 'html.parser')

    mars_weather = soup.find("span", text=re.compile("InSight")).text

# Visit the Mars Facts webpage here and use Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc.
   fact_url = "https://space-facts.com/mars/"

   tables = pd.read_html(fact_url)
   df = tables[1]
   df = df.iloc[:, [0,1]]
   df.columns = ["Facts","Value"]
   html_table = df.to_html()
   html_table = html_table.replace('\n', '')

# Visit the USGS Astrogeology site here to obtain high resolution images for each of Mar's hemispheres.
   cerberus_url = "https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced"
   schiaparelli_url = "https://astrogeology.usgs.gov/search/map/Mars/Viking/schiaparelli_enhanced"
   syrtis_url = "https://astrogeology.usgs.gov/search/map/Mars/Viking/syrtis_major_enhanced"
   valles_url ="https://astrogeology.usgs.gov/search/map/Mars/Viking/valles_marineris_enhanced"

   url_list = [cerberus_url,schiaparelli_url,syrtis_url,valles_url]

   hem_list = ["Cerberus Hemisphere","Schiaparelli Hemisphere","Syrtis Major Hemisphere","Valles Marineris Hemisphere"]

   link_dic =[]
   
   for i in range(len(hem_list)):
       response = requests.get(url_list[i])
       soup = BeautifulSoup(response.text, 'html.parser')
       results = soup.find_all('li')
       link = [result.a['href'] for result in results][0]

       link_dic.append({"title":hem_list[i], "img_url":link})


# Store all scraped data in a dictionary

    mars_data = {
        "news_title" : news_title,
        "news" : news_p,
        "image_url" : featured_image_url,
        "weather" :  mars_weather,
        "facts" : html_table,
        "hemispheres" : link_dic
    }

# Close the browser after scraping
    browser.quit()

# Return results
    return mars_data









