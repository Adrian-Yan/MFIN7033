'''
File: multiprocessing.ipynb
Project: Fuzzy and multiprocessing
File Created: Wednesday, 16th November 2022 3:15:53 am
Author: Raymond Yan Jin (yanjinn@connect.hku.hk)
-----
Last Modified: Wednesday, 16th November 2022 6:24:17 am
Modified By: Raymond Yan Jin (yanjinn@connect.hku.hk>)
-----
Copyright 2022 - 2022 Business School, The University of Hong Kong
'''

import pandas as pd 
from multiprocessing import Pool
#from multiprocessing import Manager
from fuzzywuzzy import fuzz
import numpy as np
import csv

# read the data
acquirer_data = pd.read_excel("./data/acquirers.xlsx")
bank_data = pd.read_csv("./data/bank_names.csv")
output = pd.DataFrame(columns=["acquirer", "match1", "match2", "match3", "match4", "match5"])
output["acquirer"] = acquirer_data["Acquirer Name"] 

bank_list = bank_data['bank_names'].tolist()


# fuzzy match
def fuzzy_match(index):
    
    match_list = []
    firm_name = acquirer_data.loc[index, 'Acquirer Name']
    for bank_name in bank_list:
        similarity = fuzz.ratio(firm_name, bank_name) + \
                    fuzz.partial_ratio(firm_name, bank_name) + \
                    fuzz.token_sort_ratio(firm_name, bank_name) + \
                    fuzz.token_set_ratio(firm_name, bank_name)
        match_list.append((similarity, bank_name))
    
    match_list.sort(key=lambda x: x[0], reverse=True)
    match = [element[1] for element in match_list[:5]]
    # append the result to a csv file
    with open("./data/output.csv", "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([index] + [firm_name] + match)
        f.close()

# parallelize the fuzzy match
if __name__ == '__main__':
    global output
    pool = Pool(4)
    pool.map(fuzzy_match, range(acquirer_data.shape[0]))

# sort the result
output = pd.read_csv("./data/output.csv", header=None)
output.columns = ["index", "acquirer", "match1", "match2", "match3", "match4", "match5"]
output = output.sort_values(by="index")

