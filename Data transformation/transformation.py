'''
File: transformation.ipynb
Project: Data transformation
File Created: Wednesday, 26th October 2022 2:43:08 pm (UTC+8:00)
Author: Raymond Yan Jin (yanjinn@connect.hku.hk)
-----
Last Modified: Monday, 21st November 2022 10:06:35 am (UTC+8:00)
Modified By: Raymond Yan Jin (yanjinn@connect.hku.hk>)
-----
Copyright 2022 - 2022 Business School, The University of Hong Kong
'''

import numpy as np 
import pandas as pd
import os

# Read the data
deal_data = pd.read_csv('data/deal_level_data.csv')
quarter_data = pd.read_csv('data/quarter_level_data.csv')

# Data exploration
deal_data.head()
quarter_data.head()
deal_data.shape # (3005,1467)
quarter_data.shape  # (75125,42)
deal_data.columns.to_list()
quarter_data.columns.to_list()
# 75125/3005 = 25 so the logic is to divide the deal data according to the quarters

# too slow, takes 20mins on intel i5-12500H
# even though I could improve the efficiency by using multiprocessing, I don't think it's technically meaningful.
for i in range(quarter_data.shape[0]):
    deal = quarter_data.iloc[i,:]
    acquirer = deal['Acquirer_CUSIP']
    target = deal['Target_CUSIP']
    year = deal['Year_Announced']
    quarter_to_event = deal['quarter_to_the_event_date']

    if quarter_to_event < 0:
        for j in range(16,42):
            quarter_data.iloc[i,j] = deal_data.loc[(deal_data['Acquirer_CUSIP'] == acquirer)\
                                                 & (deal_data['Target_CUSIP'] == target)\
                                                 & (deal_data['Year_Announced'] == year),\
                                                     quarter_data.columns[j]+'__'+str(-quarter_to_event)].values[0]
    elif quarter_to_event > 0:
        for j in range(16,42):
            quarter_data.iloc[i,j] = deal_data.loc[(deal_data['Acquirer_CUSIP'] == acquirer)\
                                                 & (deal_data['Target_CUSIP'] == target)\
                                                 & (deal_data['Year_Announced'] == year),\
                                                     quarter_data.columns[j]+'_'+str(quarter_to_event)].values[0]
    else:
        for j in range(16,42):
            quarter_data.iloc[i,j] = deal_data.loc[(deal_data['Acquirer_CUSIP'] == acquirer)\
                                                 & (deal_data['Target_CUSIP'] == target)\
                                                 & (deal_data['Year_Announced'] == year),\
                                                     quarter_data.columns[j]].values[0]

quarter_data.to_csv('data/quarter_level_data_output.csv',index=False)
                