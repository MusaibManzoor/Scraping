from selenium import webdriver
from bs4 import BeautifulSoup
import csv 
import time
import pandas as pd

from wsproto import Headers 

#Nasa exoplant URL

START_URL = "https://exoplanets.nasa.gov/discovery/exoplanet-catalog/"

#Web Drivers
 
browser = webdriver.Chrome("/Users/musaibmanzoorbhat/Documents/student activities /Data scraping/chromedriver")
browser.get(START_URL)  
time.sleep(10)

planets_data=[]

headers = ["name","light_years_from_earth","planet_mars","discovery_data","hyperlink","Planet_type","Planet_radius","Orbital_radius","Orbital_period"]
def scrape() : 
    for i in range(1,5):
        while True:
            time.sleep(2)

            soup = BeautifulSoup(browser.page_source,"html.parser")

# Check page number
            current_page_num = int(soup.find_all("input", attrs={"class", "page_num"})[0].get("value")) 
            if current_page_num < i: 
                browser.find_element(By.XPATH, value='//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a').click() 
            elif current_page_num > i: 
                    browser.find_element(By.XPATH, value='//*[@id="primary_column"]/footer/div/div/div/nav/span[1]/a').click() 
            else: 
                 break
        for ul_tag in soup.find_all("ul",attrs={"class","exoplanet"}):
            li_tags = ul_tag.find_all("li") 
            temp_list = [] 
            for index, li_tag in enumerate(li_tags): 
                if index == 0: 
                    temp_list.append(li_tag.find_all("a")[0].contents[0]) 
                else: 
                    try: 
                        temp_list.append(li_tag.contents[0]) 
                    except: 
                            temp_list.append("")

                # Get Hyperlink Tag 
                hyperlink_li_tag = li_tags[0] 
                temp_list.append("https://exoplanets.nasa.gov"+ hyperlink_li_tag.find_all("a", href=True)[0]["href"]) 
                planets_data.append(temp_list) 
                browser.find_element(By.XPATH, value='//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a').click() 
                
                print(f"Page {i} scraping completed")

#calling method        
scrape()