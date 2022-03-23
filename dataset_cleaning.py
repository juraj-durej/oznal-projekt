import pandas as pd
import numpy as np
import os

data_path = '/Users/jdurej/Documents/škola/ING_2/OZNAL/projekt/data/'

# stlpce v datasete

# BOROUGH
# NEIGHBORHOOD
# BUILDING CLASS CATEGORY
# TAX CLASS AT PRESENT
# BLOCK
# LOT
# EASE-MENT
# BUILDING CLASS AT PRESENT
# ADDRESS
# APARTMENT NUMBER
# ZIP CODE
# RESIDENTIAL UNITS
# COMMERCIAL UNITS
# TOTAL UNITS
# LAND SQUARE FEET
# GROSS SQUARE FEET
# YEAR BUILT
# TAX CLASS AT TIME OF SALE
# BUILDING CLASS AT TIME OF SALE
# SALE PRICE
# SALE DATE

for root, dirs, files in os.walk(data_path, topdown=False):
    for name in files:

        if name[len(name)-4:] == '.xls':
            df = pd.read_excel(os.path.join(root, name),
                               sheet_name='Manhattan', skiprows=3)

            df = df[df['SALE PRICE'] > 10000]
            # df = df[df['TOTAL UNITS'] != 0] ?
            df = df[df['YEAR BUILT'] != 0]
            df = df[df['NEIGHBORHOOD'] != '']
            df = df[df['ADDRESS'] != '']
            df = df[df['SALE DATE'] != '']

            print(df)
