# Dependencies
from splinter import Browser
from bs4 import BeautifulSoup as bs
import requests
import pandas as pd
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

def init_browser():
    executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)

def scrape():
    browser = init_browser()

    url = "https://redplanetscience.com/"
    browser.visit(url)

    news_title = soup.find("div", class_="content_title").text
    paragraph = soup.find("div", class_="article_teaser_body").text
