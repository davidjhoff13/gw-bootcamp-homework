
import pandas as pd
from splinter import Browser
from splinter.exceptions import ElementDoesNotExist
from bs4 import BeautifulSoup
import datetime as dt
import time

#%%

executable_path = {'executable_path': 'chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=False)

#%%

def mars_news(browser):
    newsurl='https://mars.nasa.gov/news/'
    browser.visit(newsurl)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    time.sleep(5)
    try:
        
        itemlist= soup.find("ul", class_="item_list")
        title=itemlist.find("div", class_="content_title").get_text()
        teaser=itemlist.find('div', class_="article_teaser_body").get_text()
      
        print(title)
        print(teaser) 
        return title,teaser
    except Exception as e: 
        print(e)
  



#%%

def featured_image(browser):
    
    imageurl='https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(imageurl)
    html=browser.html
    soup=BeautifulSoup(html, 'html.parser')
    try:
        image_url=soup.find('a', class_="button fancybox")['data-fancybox-href']
    except AttributeError:
        return None
    nasa_url='jpl.nasa.gov'
    featured_image_url= str(nasa_url)+str(image_url)

    print(featured_image_url)
    
    return featured_image_url



#%%

def twitter (browser):
    twitterurl='https://twitter.com/marswxreport?lang=en'
    browser.visit(twitterurl)
    html = browser.html
    time.sleep(5)
    soup = BeautifulSoup(html, 'html.parser')

    weather=soup.find(class_="css-901oao r-hkyrab r-1qd0xha r-a023e6 r-16dba41 r-ad9z0x r-bcqeeo r-bnwqim r-qvutc0").text.strip()


    print(weather)
    return weather





#%%

def marsfacts(browser):

    tableurl = 'https://space-facts.com/mars'
    browser.visit(tableurl)
    try:
        table = pd.read_html(tableurl)
    except AttributeError:
            return None
    tabledf=table[0]
    tabledf.columns=['Description', 'Measurement']
    html_table=tabledf.to_html()
    html_table.replace('\n', '')
 
    print ("Table is finished")
    return html_table       



#%%
def hemisphere_images (browser):
    hemis=['Valles Marineris', 'Cerberus', 'Schiaparelli', 'Syrtis Major']
    mars_urls=[]
    hemis_url='https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    print('The hemis list' + str(hemis))

    for h in hemis:
    
        browser.visit(hemis_url)
        browser.click_link_by_partial_text(h)
        html=browser.html
        soup=BeautifulSoup(html, 'html.parser')
        try:
            target_url=soup.find(class_='wide-image')['src']
        except AttributeError:
            return None
        image_url=(f'https://astrogeology.usgs.gov'+target_url)
        mars_urls.append(image_url)
    print(mars_urls)

    hemisphere_image_urls = [
        {'title':hemis[0], 'img_url': mars_urls[0]},
        {'title':hemis[1], 'img_url': mars_urls[1]},
        {'title':hemis[2], 'img_url': mars_urls[2]},
        {'title':hemis[3], 'img_url': mars_urls[3]}]

    return hemisphere_image_urls



#%%
def scrape_everything(browser):
    #executable_path = {'executable_path': 'chromedriver.exe'}
    #browser = Browser('chrome', **executable_path, headless=False)
    

    title = mars_news(browser)
    teaser = mars_news(browser)
    featured_image_url = featured_image(browser)
    weather=twitter(browser)
    html_table=marsfacts(browser)
    hemisphere_image_urls=hemisphere_images(browser)
    timestamp=dt.datetime.now()

    marsdata = {
       'news_title':title,
       'news_teaser':teaser,
       'featured_image':featured_image_url,
       'mars_weather':weather,
       'marsfacts':html_table,
       'hemisphere_images':hemisphere_image_urls,
       'update_time':timestamp}
    print(marsdata)
    
    return marsdata

scrape_everything(browser)







