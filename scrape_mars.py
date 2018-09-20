# Import modules
from splinter import Browser
from bs4 import BeautifulSoup
import requests
import pandas as pd
import time

# Inialize browser
def init_browser():
	executable_path = {'executable_path': '/anaconda3/bin/chromedriver'}
	# browser = Browser('chrome', **executable_path, headless=False)
	return Browser("chrome", **executable_path, headless=True)

 # function to scape for mars data
def scrape():
	browser = init_browser()
	mars = {}

	## Latest Mars News
	url = "https://mars.nasa.gov/news/"
	browser.visit(url)
	html = browser.html
	soup = BeautifulSoup(html, 'html.parser')

	title = soup.find('div', class_='content_title').text
	text_preview = soup.find('div', class_='article_teaser_body').text	
	
	#mars['headline'] = mars_headline
	#mars['article'] = text_preview


	## JPL Mars Space Image
	
	url_3 = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
	browser.visit(url_3)
	html = browser.html
	soup = BeautifulSoup (html, 'html.parser')
	browser.click_link_by_partial_text("FULL IMAGE")
	time.sleep(1)
	browser.click_link_by_partial_text("more info")
	html = browser.html
	soup = BeautifulSoup(html, "html.parser")
	image = soup.find('img', class_="main_image")['src']

	base_url = 'https://www.jpl.nasa.gov'
	featured_image_url = base_url + image
	
	#mars['img'] = featured_image_url


	## Mars Weather
	url_4 = 'https://twitter.com/marswxreport?lang=en'
	browser.visit(url_4)
	html = browser.html
	soup = BeautifulSoup(html, 'html.parser')
	tweet = soup.find('p', class_='TweetTextSize')
	mars_weather = tweet.text.strip()

	#mars['weather'] = mars_weather

	
	
	## Mars Facts

	url = "https://space-facts.com/mars/"
	browser.visit(url)
	time.sleep(1)
	html = browser.html
	soup = BeautifulSoup(html, "html.parser")
	results = soup.find('tbody').find_all('tr')

	mars_facts = []

	for result in results:
		column_2 = result.find('td', class_="column-1").text
		column_fact = result.find('td', class_="column-2").text
		mars_space_facts = {}
		mars_space_facts['column_2'] = column_fact
		mars_facts.append(mars_space_facts)

		#mars['facts'] = mars_facts


	## Mars Hemispheres
	
		


	# Append to empty dictionary named 'mars'
	mars = {
		"headline": title,
		"article": text_preview,
		"img": featured_image_url,
		"weather": mars_weather,
		# "mars_facts": mars_facts
	}

	browser.quit()

	return mars
