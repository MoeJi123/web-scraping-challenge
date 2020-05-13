#!/usr/bin/env python
# coding: utf-8

# In[209]:


from splinter import Browser
from bs4 import BeautifulSoup
import re
import time
import requests
import pandas as pd


# ### NASA Mars News

# In[4]:


# URL of page to be scraped
url = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'


# In[5]:


# Retrieve page with the requests module
response = requests.get(url)


# In[125]:


# Create BeautifulSoup object; parse with 'html.parser'
soup = BeautifulSoup(response.text, 'lxml')


# In[126]:


# Examine the results, then determine element that contains sought info
print(soup.prettify())


# In[147]:


# results are returned as an iterable list
results = soup.find_all("div", class_="image_and_description_container")


# In[148]:


results


# In[157]:


list = soup.find_all("ul", class_="item_list")


# In[158]:


list


# ### JPL Mars Space Images - Featured Image

# In[173]:


get_ipython().system('which chromedriver')


# In[174]:


executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
browser = Browser('chrome', **executable_path, headless=False)


# In[178]:


url = 'https://www.jpl.nasa.gov/spaceimages'
browser.visit(url)


# In[179]:


for x in range(1):
    # HTML object
    html = browser.html
    # Parse HTML with Beautiful Soup
    soup = BeautifulSoup(html, 'html.parser')
    articles = soup.find_all('article', class_="carousel_item")   
    print(articles)


# In[183]:


featured_image_url = "https://www.jpl.nasa.gov/spaceimages"+"/images/wallpaper/PIA19092-1920x1200.jpg"


# In[184]:


featured_image_url


# ### Mars Weather

# In[185]:


url = "https://twitter.com/marswxreport?lang=en"


# In[186]:


response = requests.get(url)


# In[195]:


soup = BeautifulSoup(response.text, 'lxml')


# In[196]:


results = soup.find('div', attrs={"aria-label": "Mars Weather"})


# In[197]:


results 


# In[207]:


tweet = soup.find('div', class_="css-901oao css-16my406 r-1qd0xha r-ad9z0x r-bcqeeo r-qvutc0")


# In[208]:


tweet


# ### Mars Facts

# In[210]:


url = "https://space-facts.com/mars/"


# In[216]:


tables = pd.read_html(url)
tables


# In[217]:


type(tables)


# In[233]:


df = tables[1]
df = df.iloc[:, [0,1]]


# In[231]:


df.columns = ["Facts","Value"]


# In[232]:


df


# In[236]:


#convert the data to a HTML table string
html_table = df.to_html()
html_table


# In[237]:


#strip unwanted newlines to clean up the table
html_table.replace('\n', '')


# In[238]:


df.to_html('mars_fact.html')


# In[239]:


get_ipython().system('open table.html')


# ### Mars Hemispheres

# In[289]:


cerberus_url = "https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced"
schiaparelli_url = "https://astrogeology.usgs.gov/search/map/Mars/Viking/schiaparelli_enhanced"
syrtis_url = "https://astrogeology.usgs.gov/search/map/Mars/Viking/syrtis_major_enhanced"
valles_url ="https://astrogeology.usgs.gov/search/map/Mars/Viking/valles_marineris_enhanced"


# In[290]:


url_list = [cerberus_url,schiaparelli_url,syrtis_url,valles_url]


# In[291]:


hem_list = ["Cerberus Hemisphere","Schiaparelli Hemisphere","Syrtis Major Hemisphere","Valles Marineris Hemisphere"]


# In[292]:


link_dic =[]

for i in range(len(hem_list)):


    response = requests.get(url_list[i])
    soup = BeautifulSoup(response.text, 'html.parser')
    results = soup.find_all('li')
    link = [result.a['href'] for result in results][0]

    link_dic.append({"title":hem_list[i], "img_url":link})
    


# In[293]:


link_dic


# In[ ]:




