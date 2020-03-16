from bs4 import BeautifulSoup as bs
from splinter import Browser
import os
import pandas as pd
import time
from selenium import webdriver

def scrape():
    browser = Browser("chrome", executable_path = "chromedriver.exe", headless = True)
    mars_facts_data = {}
    
    # NASA Mars News Site

    url_news = "https://mars.nasa.gov/news/"
    browser.visit(url_news)
    time.sleep(3)
    html = browser.html
    news_soup = bs(html, "html.parser")
    
    # Extract the latest news title and paragraph text

    news_title = news_soup.find("div",class_="content_title").text
    news_p = news_soup.find("div", class_="article_teaser_body").text
    mars_facts_data['news_title'] = news_title
    mars_facts_data['news_paragraph'] = news_p

    # JPL Mars Space Images - Featured Image
    url_image = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(url_image)
    time.sleep(3)
    
    # Extracting the base url
    from urllib.parse import urlsplit
    base_url = "{0.scheme}://{0.netloc}/".format(urlsplit(url_image))
    
    # xpath selector to grab the image
    xpath = "//*[@id=\"page\"]/section[3]/div/ul/li[1]/a/div/div[2]/img"

    results = browser.find_by_xpath(xpath)
    img = results[0]
    img.click()
    time.sleep(3)
    
    # Extracting the image url

    html_image = browser.html
    img_soup = bs(html_image, "html.parser")
    img_url = img_soup.find("img", class_="thumb")["src"]
    full_img_url = base_url + img_url
    mars_facts_data["featured_image"] = full_img_url
    
    # Getting latest Mars weather tweet

    url_weather = "https://twitter.com/marswxreport?lang=en"
    browser.visit(url_weather)
    html_weather = browser.html
    soup = bs(html_weather, "html.parser")
    mars_weather = soup.find("p", class_="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text").text
    mars_facts_data["mars_weather"] = mars_weather
    
    # Extracting Mars Facts

    url_facts = "https://space-facts.com/mars/"
    time.sleep(3)
    df = pd.read_html(url_facts)
    df[0]

    df_facts = df[0]
    df_facts.columns = ["Description", "Value"]
    df_facts.set_index("Description", inplace=True)
    html_factstable = df_facts.to_html(classes="table table-striped")
    facts_table = html_factstable.replace("\n", "")
    mars_facts_data["mars_facts_table"] = facts_table

    # Getting images for each of Mar's hemispheres
    
    url_hemispheres = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(url_hemispheres)
    
    # Getting the base url
    hemisphere_base_url = "{0.scheme}://{0.netloc}/".format(urlsplit(url_hemispheres))
    hemisphere_img_urls = []
    hemisphere_img_urls

    # Cerberus-Hemisphere-image-url

    hemisphere_img_urls = []
    results = browser.find_by_xpath( "//*[@id='product-section']/div[2]/div[1]/a/img").click()
    time.sleep(2)
    cerberus_open_click = browser.find_by_xpath( "//*[@id='wide-image-toggle']").click()
    time.sleep(1)
    cerberus_image = browser.html
    soup = bs(cerberus_image, "html.parser")
    cerberus_url = soup.find("img", class_="wide-image")["src"]
    cerberus_img_url = hemisphere_base_url + cerberus_url
    cerberus_title = soup.find("h2",class_="title").text
    back_button = browser.find_by_xpath("//*[@id='splashy']/div[1]/div[1]/div[3]/section/a").click()
    cerberus = {"image title":cerberus_title, "image url": cerberus_img_url}
    hemisphere_img_urls.append(cerberus)


    # Schiaparelli-Hemisphere-image-url

    results1 = browser.find_by_xpath( "//*[@id='product-section']/div[2]/div[2]/a/img").click()
    time.sleep(2)
    schiaparelli_open_click = browser.find_by_xpath( "//*[@id='wide-image-toggle']").click()
    time.sleep(1)
    schiaparelli_image = browser.html
    soup = bs(schiaparelli_image, "html.parser")
    schiaparelli_url = soup.find("img", class_="wide-image")["src"]
    schiaparelli_img_url = hemisphere_base_url + schiaparelli_url
    schiaparelli_title = soup.find("h2",class_="title").text
    back_button = browser.find_by_xpath("//*[@id='splashy']/div[1]/div[1]/div[3]/section/a").click()
    schiaparelli = {"image title":schiaparelli_title, "image url": schiaparelli_img_url}
    hemisphere_img_urls.append(schiaparelli)


    # Syrtis Major Hemisphere

    results1 = browser.find_by_xpath( "//*[@id='product-section']/div[2]/div[3]/a/img").click()
    time.sleep(2)
    syrtis_major_open_click = browser.find_by_xpath( "//*[@id='wide-image-toggle']").click()
    time.sleep(1)
    syrtis_major_image = browser.html
    soup = bs(syrtis_major_image, "html.parser")
    syrtis_major_url = soup.find("img", class_="wide-image")["src"]
    syrtis_major_img_url = hemisphere_base_url + syrtis_major_url
    syrtis_major_title = soup.find("h2",class_="title").text
    back_button = browser.find_by_xpath("//*[@id='splashy']/div[1]/div[1]/div[3]/section/a").click()
    syrtis_major = {"image title":syrtis_major_title, "image url": syrtis_major_img_url}
    hemisphere_img_urls.append(syrtis_major)


    # Valles Marineris Hemisphere

    results1 = browser.find_by_xpath( "//*[@id='product-section']/div[2]/div[4]/a/img").click()
    time.sleep(2)
    valles_marineris_open_click = browser.find_by_xpath( "//*[@id='wide-image-toggle']").click()
    time.sleep(1)
    valles_marineris_image = browser.html
    soup = bs(valles_marineris_image, "html.parser")
    valles_marineris_url = soup.find("img", class_="wide-image")["src"]
    valles_marineris_img_url = hemisphere_base_url + syrtis_major_url
    valles_marineris_title = soup.find("h2",class_="title").text
    back_button = browser.find_by_xpath("//*[@id='splashy']/div[1]/div[1]/div[3]/section/a").click()
    valles_marineris = {"image title":valles_marineris_title, "image url": valles_marineris_img_url}
    hemisphere_img_urls.append(valles_marineris)

    mars_facts_data["hemisphere_img_url"] = hemisphere_img_urls

    return mars_facts_data