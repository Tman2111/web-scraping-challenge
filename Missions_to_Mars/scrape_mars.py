# Dependencies
from splinter import Browser
from bs4 import BeautifulSoup as bs
import requests
import pandas as pd
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# Mars articles

def init_browser():
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)
    return browser
def scrape():
    browser = init_browser()

    url = "https://redplanetscience.com/"
    browser.visit(url)

    html = browser.html
    soup = bs(html, "html.parser")

    news_title = soup.find("div", class_="content_title").text
    paragraph = soup.find("div", class_="article_teaser_body").text

#executable_path = {'executable_path': ChromeDriverManager().install()}
#browser = Browser('chrome', **executable_path, headless=False)

# Featured Image
    images_url = "https://spaceimages-mars.com/"

    browser.visit(images_url)

    html = browser.html

    images_soup = bs(html, 'html.parser')

    mars_image = images_soup.find("img", class_="headerimage fade-in").get("src")
    print(mars_image)

# Mars Facts

    facts_url = "https://galaxyfacts-mars.com/"
    
    # pandas "read_html"
    table = pd.read_html(facts_url)
    table
    facts_df = table[0]
    facts_df

    facts_df.columns=["Comparison", "Mars", "Earth"]
    facts_df
    mars_html_table = facts_df.to_html()
    mars_html_table.replace('\n', '')

# Mars Hemispheres
    hemisphere_image_urls = [
    {"title": "Valles Marineris Hemisphere", "img_url": "https://marshemispheres.com/valles.html#open"},
    {"title": "Cerberus Hemisphere", "img_url": "https://marshemispheres.com/cerberus.html#open"},
    {"title": "Schiaparelli Hemisphere", "img_url": "https://marshemispheres.com/schiaparelli.html#open"},
    {"title": "Syrtis Major Hemisphere", "img_url": "https://marshemispheres.com/syrtis.html#open"},
]

# Store Data

    mars_data ={
        "news_title": news_title,
        "news_p": paragraph,
        "featured_image_url": mars_image,
        "mars_facts": mars_html_table,
        "hemisphere_image_urls": hemisphere_image_urls   
    }

# Close Browser
    browser.quit()

# return data
    return mars_data

if __name__ == '__main__':
    scrape()





