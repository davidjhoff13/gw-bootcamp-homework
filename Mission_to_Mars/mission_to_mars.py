#!/usr/bin/env python
# coding: utf-8

# # Scraping with Pandas

# In[19]:


import pandas as pd
from splinter import Browser
from splinter.exceptions import ElementDoesNotExist
from bs4 import BeautifulSoup


# In[2]:


executable_path = {'executable_path': 'chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=False)


# In[3]:


newsurl='https://mars.nasa.gov/news/'
browser.visit(newsurl)


# In[4]:


html = browser.html
soup = BeautifulSoup(html, 'html.parser')

title=soup.find(class_='bottom_gradient').get_text()
teaser=soup.find(class_="article_teaser_body").get_text()

print(title)
print(teaser)


# In[5]:


imageurl='https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
browser.visit(imageurl)


# In[6]:


html=browser.html
soup=BeautifulSoup(html, 'html.parser')

image_url=soup.find('a', class_="button fancybox")['data-fancybox-href']

nasa_url='jpl.nasa.gov'
featured_image_url= str(nasa_url)+str(image_url)

print(featured_image_url)


# In[7]:


twitterurl='https://twitter.com/marswxreport?lang=en'
browser.visit(twitterurl)


# In[21]:


html = browser.html
soup = BeautifulSoup(html, 'html.parser')

weather=soup.find(class_='css-901oao r-hkyrab r-1qd0xha r-a023e6 r-16dba41 r-ad9z0x r-bcqeeo r-bnwqim r-qvutc0').get_text()


print(weather)


# In[9]:


tableurl = 'https://space-facts.com/mars'


# In[10]:


table = pd.read_html(tableurl)
table


# In[11]:


tabledf = table[0]

tabledf.columns = ['Feature', 'Data']

tabledf

## DataFrames as HTML


# In[12]:


html_table = tabledf.to_html()

html_table


# In[13]:


html_table.replace('\n', '')


# In[14]:


hemis=['Valles Marineris', 'Cerberus', 'Schiaparelli', 'Syrtis Major']
mars_urls=[]
hemis_url='https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
print('The hemis list' + str(hemis))


# In[15]:


for h in hemis:
    
    browser.visit(hemis_url)
    browser.click_link_by_partial_text(h)
    html=browser.html
    soup=BeautifulSoup(html, 'html.parser')
    target_url=soup.find(class_='wide-image')['src']
    image_url=(f'https://astrogeology.usgs.gov'+target_url)
    mars_urls.append(image_url)

    


# In[17]:


print(mars_urls)


# In[18]:


hemphisphere_image_urls = [
    {'title':hemis[0], 'img_url': mars_urls[0]},
    {'title':hemis[1], 'img_url': mars_urls[1]},
    {'title':hemis[2], 'img_url': mars_urls[2]},
    {'title':hemis[3], 'img_url': mars_urls[3]}
]

hemphisphere_image_urls


# In[ ]:




