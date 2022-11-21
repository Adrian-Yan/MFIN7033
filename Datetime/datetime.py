'''
File: datetime.ipynb
Project: Datetime
File Created: Wednesday, 16th November 2022 3:15:53 am
Author: Raymond Yan Jin (yanjinn@connect.hku.hk)
-----
Last Modified: Wednesday, 16th November 2022 6:25:19 am
Modified By: Raymond Yan Jin (yanjinn@connect.hku.hk>)
-----
Copyright 2022 - 2022 Business School, The University of Hong Kong
'''


import numpy as np 
import pandas as pd
import datetime as dt

# read the data
data = pd.read_csv(r'./data/ukpound_exchange.csv')

# data exploration
data.shape # (8429, 4)
data.head()

# select the row of date as the end of the month
data['Date'] = pd.to_datetime(data['Date'])
output = data[data['Date'].dt.is_month_end]

# check the output data
output.head()
output.shape # (276, 4)

# write the output data to csv
output.to_csv(r'./data/output.csv', index = False)