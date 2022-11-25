'''
File: SFC.ipynb
Project: webscrap
File Created: Thursday, 24th November 2022 6:23:06 pm (UTC+8:00)
Author: Raymond Yan Jin (yanjinn@connect.hku.hk)
-----
Last Modified: Friday, 25th November 2022 5:01:44 pm (UTC+8:00)
Modified By: Raymond Yan Jin (yanjinn@connect.hku.hk>)
-----
Copyright 2022 - 2022 Business School, The University of Hong Kong
'''


import pandas as pd 
import numpy as np
import selenium
from selenium import webdriver
import time
import math

browser = webdriver.Chrome(r"C:\Program Files\Development\chromedriver.exe")

url = "https://apps.sfc.hk/productlistWeb/searchProduct/UTMF.do"
browser.get(url)

fund_list = pd.DataFrame(columns = ['Product_Name', 'Sub_Fund_Name', 'Issuer', 'Auth_Date', 'Doc', 'Deriv_Fund'])

for i in range(2,2087):
    Product_Name = browser.find_elements("xpath", "/html/body/div[3]/div/div[2]/form[2]/div[3]/div/table/tbody/tr[{}]/td[1]".format(i))[0].text
    Sub_Fund_Name = browser.find_elements("xpath", "/html/body/div[3]/div/div[2]/form[2]/div[3]/div/table/tbody/tr[{}]/td[2]".format(i))[0].text
    Issuer = browser.find_elements("xpath", "/html/body/div[3]/div/div[2]/form[2]/div[3]/div/table/tbody/tr[{}]/td[3]".format(i))[0].text
    Auth_Date = browser.find_elements("xpath", "/html/body/div[3]/div/div[2]/form[2]/div[3]/div/table/tbody/tr[{}]/td[4]".format(i))[0].text
    Doc = browser.find_elements("xpath", "/html/body/div[3]/div/div[2]/form[2]/div[3]/div/table/tbody/tr[{}]/td[5]".format(i))[0].text
    Deriv_Fund = browser.find_elements("xpath", "/html/body/div[3]/div/div[2]/form[2]/div[3]/div/table/tbody/tr[{}]/td[6]".format(i))[0].text
    #fund_list = fund_list.append({'Product_Name': Product_Name, 'Sub_Fund_Name': Sub_Fund_Name, 'Issuer': Issuer, 'Auth_Date': Auth_Date, 'Doc': Doc, 'Deriv_Fund': Deriv_Fund}, ignore_index=True)
    fund_list = pd.concat([fund_list, pd.DataFrame({'Product_Name': Product_Name, 'Sub_Fund_Name': Sub_Fund_Name, 'Issuer': Issuer, 'Auth_Date': Auth_Date, 'Doc': Doc, 'Deriv_Fund': Deriv_Fund}, index=[0])], ignore_index=True)

fund_list.to_csv("data/temp_fund_list.csv", index=False)

fund_list = pd.read_csv('data/temp_fund_list.csv')
fund_list['Product_ID'] = fund_list['Product_Name'].apply(lambda x: x.split(' ')[-1].strip('()'))
fund_list['Sub_Fund_ID'] = fund_list['Sub_Fund_Name'].apply(lambda x: x.split(' ')[-1].strip('()') if type(x) == str else np.nan)
#fund_list['doc_url'] = "https://apps.sfc.hk/productlistWeb/searchProduct/getDocListNoDate.do?lang=EN&ceref={}&docType=OD".format(fund_list['Sub_Fund_ID'])
for i in range(fund_list.shape[0]):
    if fund_list.loc[i, 'Doc'] != ' ':
        fund_list.loc[i, 'doc_url'] = "https://apps.sfc.hk/productlistWeb/searchProduct/getDocListNoDate.do?lang=EN&ceref={}&docType=OD".format(fund_list.loc[i, 'Sub_Fund_ID'])
fund_list.to_csv('data/fund_list.csv', index=False)

options = webdriver.ChromeOptions()
prefs = {"profile.default_content_settings.popups": 0,
        "download.default_directory": r"C:\Projects\FundsData\data\Key_Stats\\", # IMPORTANT - ENDING SLASH V IMPORTANT
        "directory_upgrade": True}
options.add_experimental_option("prefs",prefs)
browser = webdriver.Chrome(executable_path=r"C:\Program Files\Development\chromedriver.exe", options=options)
fund_list = pd.read_csv('data/fund_list.csv')
# in my project this should be range(2086), for your time and convenience, I have set it to 10
for i in range(15):
    if type(fund_list.iloc[i]['doc_url']) != float:
        url = fund_list.iloc[i]['doc_url']
        browser.get(url)
        try:
            browser.find_element_by_xpath('/html/body/div/div/div[3]/div/div/div/div[2]/table/tbody/tr[3]/td/a').click()
        except:
            pass