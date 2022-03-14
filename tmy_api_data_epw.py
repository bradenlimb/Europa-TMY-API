#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 15:17:28 2022

@author: bradenlimb
"""


#%% Import Modules
from IPython import get_ipython
get_ipython().magic('reset -sf')

import pandas as pd
import sys
import requests
import datetime
begin_time = datetime.datetime.now()

#%% Import Inputs Spreadsheet

xslx_path = "/Users/bradenlimb/CloudStation/Quinn Group/Reid API/inputs.xlsx"  # Input spreadsheet path
df_inputs = pd.read_excel (xslx_path)           # Read the inputs spreadsheet as a Panda's data frame
column_names = df_inputs.columns                # Extract all of the column names for the parameters

#%% Call API and Save the Files

# Example Base URL "https://re.jrc.ec.europa.eu/api/v5_1/tool_name?param1=value1&param2=value2&..."
# Example TMY URL "https://re.jrc.ec.europa.eu/api/tmy?lat=45&lon=8"

base_url = "https://re.jrc.ec.europa.eu/api/"   # Base URL of the API
tool_name = "tmy?"                              # Tool Name + "?" for url
separator = "&"                                 # Separator string for url
url = base_url+tool_name                        # Add the tool name to the base url


for i in range(len(df_inputs)):                 # Loop through all of the lines on the input spreadsheet
    for j in range(len(column_names)):          # Loop through the different parameters on the input spreadsheet
        param = column_names[j]                 # Extract the parameter name
        value = str(df_inputs.loc[i,param])     # Pull the value for the given parameter and row (i)
        url = url+param+"="+value               # Add parameter and value to url
        if j < len(column_names)-1:
            url = url+separator                 # If there are more parameters to add then add the separator
        output = requests.get(url)              # Call the url to get the data from the API
        with open(f'{i}.epw','w') as f:         # Write the text recived to a epw file
            f.write(output.text)
            f.close()
    
    
    

