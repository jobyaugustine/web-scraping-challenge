from splinter import Browser
from bs4 import BeautifulSoup as bs
import time
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

def scrape_info():

    mars_data={}

    # Set up Splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    # NASA Mars News
    url = "https://redplanetscience.com/"
    browser.visit(url)

    time.sleep(1)

    # Scrape page into Soup
    html = browser.html
    soup = bs(html, "html.parser")

    news_title = soup.find('div',class_='content_title')
    news_p = soup.find('div', class_='article_teaser_body')

    #mars_data["news_title"] = news_title
    #mars_data["news_p"] = news_p

 # NASA  JPL Mars Space Images - Featured Image
    url = "https://spaceimages-mars.com"
    browser.visit(url)

    time.sleep(1)

    # Scrape page into Soup
    html = browser.html
    soup = bs(html, "html.parser")

    topclass=soup.find('div',class_ = 'floating_text_area')

    featureimg=topclass.a['href']

    featured_image_url =jplurl + "/" + featureimg
    featured_image_url = "'" + featured_image_url + "'" 
    
    mars_data["featured_image_url"] = featured_image_url

# Mars Facts
    url = "https://galaxyfacts-mars.com"
    browser.visit(url)

    time.sleep(1)

    # Scrape page into Soup
    html = browser.html
    soup = bs(html, "html.parser")

    tables = pd.read_html(url)
    df = tables[0]
    html_table = df.to_html()

    #Adding to the dictionary
    mars_data["html_table"] = html_table

# Mars Hemisphears
    url = "https://marshemispheres.com/"
    browser.visit(url)

    time.sleep(1)

    # Scrape page into Soup
    html = browser.html
    soup = bs(html, "html.parser")
    imgurl_list=[]
    title_list =[]
    counter = 0
    allimages=soup.find_all('div',class_='description')


    for im in allimages:
    
        link = im.find('a')
        href=link['href']
        each_title = im.a.find('h3')
    
        each_title2= each_title.text
        title_list.append(each_title2) 
        nextpage=hemsph_url + href
        imgurl_list.append(nextpage)
        counter = counter + 1
    
        if (counter ==4):
            break
        
# Storing in a python dictionary as a list

    final_list = []

# print(len(title_list))
# print(len(imgurl_list))

    listitem1 = {"title": title_list[0], "img_url":imgurl_list[0]}
    listitem2 = {"title": title_list[1], "img_url":imgurl_list[1]}
    listitem3 = {"title": title_list[2], "img_url":imgurl_list[2]}
    listitem4 = {"title": title_list[3], "img_url":imgurl_list[3]}

    final_list = [listitem1,listitem2,listitem3,listitem4]

    mars_data["final_list"] = final_list

    return mars_data

if __name__=="__main__":
    scrape()
