'''
File: geolocation.ipynb
Project: Google API geolocation
File Created: Wednesday, 16th November 2022 3:15:53 am
Author: Raymond Yan Jin (yanjinn@connect.hku.hk)
-----
Last Modified: Wednesday, 16th November 2022 6:23:37 am
Modified By: Raymond Yan Jin (yanjinn@connect.hku.hk>)
-----
Copyright 2022 - 2022 Business School, The University of Hong Kong
'''

from vincenty import vincenty
import googlemaps
from datetime import datetime
import pandas as pd
import time
import numpy as np

comp_data = pd.read_excel("./data/coname_addresses.xlsx")
gmaps = googlemaps.Client(key='')
# geocode_result = gmaps.geocode('1600 Amphitheatre Parkway, Mountain View, CA')
WhiteHouse = (38.8976763, -77.0365298)

output = pd.DataFrame()
# initialize the output dataframe
output['index'] = comp_data.index
output['CONAME'] = comp_data['CONAME']
output['address'] = comp_data['address']
output['distance'] = 0
output['lat'] = 0
output['lng'] = 0


for i in range(comp_data.shape[0]):
    #sleep for 1 sec
    if output['distance'][i] == 0:
        
        data_comp = comp_data.iloc[i]
        coname = data_comp['CONAME']
        address = data_comp['address']
        geocode_result = gmaps.geocode(address)
        try:
            lat = geocode_result[0]['geometry']['location']['lat']
            lng = geocode_result[0]['geometry']['location']['lng']
            distance = vincenty((lat, lng), WhiteHouse)

            output['distance'][i] = distance    
            output['lat'][i] = lat
            output['lng'][i] = lng
        except:
            print("Error: ", i, coname, address)
            pass
        output.to_excel("temp.xlsx", index=False)
        time.sleep(np.random.uniform(2, 4))

# count the number of zero distance
geocode_result = gmaps.geocode(comp_data.iloc[593]['address'])

# export to excel
output.to_excel("output.xlsx", index=False)
