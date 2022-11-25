'''
File: scholar.ipynb
Project: webscrap
File Created: Monday, 21st November 2022 3:02:42 pm (UTC+8:00)
Author: Raymond Yan Jin (yanjinn@connect.hku.hk)
-----
Last Modified: Monday, 21st November 2022 7:42:11 pm (UTC+8:00)
Modified By: Raymond Yan Jin (yanjinn@connect.hku.hk>)
-----
Copyright 2022 - 2022 Business School, The University of Hong Kong
'''


import pandas as pd 
import numpy as np
import selenium
from selenium import webdriver
import time


browser = webdriver.Chrome(r"C:\Program Files\Development\chromedriver.exe")

vol = input("Enter the volume number(can be list seperated by comma, e.g 140;141): ")
issue = input("Enter the issue number(can be list seperated by comma, e.g 1;2): ")

vol = vol.split(";")
issue = issue.split(";")


for v in vol:
    for i in issue:
        url = "https://www.sciencedirect.com/journal/journal-of-financial-economics/vol/{}/issue/{}".format(v,i)
        browser.get(url)
        #time.sleep(5)
        num = len(browser.find_elements("class name", "js-article-title"))
        articles = []
        articles_url = []
        authors = []
        for j in range(num):
            articles.append(browser.find_elements("class name", "js-article-title")[j].text)
            # get the link of each article
            articles_url.append(browser.find_elements("class name", "article-content-title")[j].get_attribute("href"))
            # get the author of each article
            authors.append(browser.find_elements("class name", "js-article-author-list")[j].text)
            #drop the empty url
            articles_url = [x for x in articles_url if x != '']
        scholar = pd.DataFrame({"Article":articles, "Author":authors, "URL":articles_url})

scholar.to_csv("scholar.csv", index = False)