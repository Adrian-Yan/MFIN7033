'''
File: data_concatenation.py
Project: Data concatenation
File Created: Wednesday, 16th November 2022 3:15:53 am
Author: Raymond Yan Jin (yanjinn@connect.hku.hk)
-----
Last Modified: Wednesday, 16th November 2022 6:25:57 am
Modified By: Raymond Yan Jin (yanjinn@connect.hku.hk>)
-----
Copyright 2022 - 2022 Business School, The University of Hong Kong
'''

import numpy as np 
import pandas as pd

# Read the data
df1 = pd.read_csv('data/2014.csv')
df2 = pd.read_csv('data/2015.csv')

# data exploration
df1.head()
df2.head()
df1.shape   #(54492, 58)
df2.shape   #(39706, 58)

# check the columns
if df1.columns.tolist() == df2.columns.tolist():
    print('The columns are the same')

# concatenate the data
df = pd.concat([df1, df2], axis=0, ignore_index=True)

# check the shape
df.head()
df.shape   #(94198, 58)

# store the data into the csv file
df.to_csv('data/output.csv', index=False)