import pandas as pd
from datetime import datetime, timedelta
import matplotlib.pyplot as plt


#Importing the .tsv file and converting the df to csv format
data = pd.read_table('2004-2019.tsv', sep = '\t')
data.to_csv('brazil_gasdata.csv', index = True)

#Creating a copy of the data set and storing it in brazil_gasdata
brazil_gasdata = data.copy()

#Dropping a redundant column that was possibly an index column.
brazil_gasdata.drop('Unnamed: 0', inplace = True, axis = 1)

#Defining the English translation of the columns in the dataset
new_col_names = ['Initial_Observed_Date', 'Final_Observed_Date', 'Region', 
                 'State', 'Product', 'No.Gas_Stations', 'Measurement_Unit', 
                 'Mean_Mkt_Value', 'Standard_Deviation', 'Min_Price',
                 'Max_Price', 'Mean_Price_Margin', 'Coefficient_of_Variation', 
                 'Mean_Distribution_Price', 'Distribution_Std_Dev', 'Distribution_Min_Price', 
                 'Distribution_Max_Price', 'Distribution_Coeff_of_Variation', 
                 'Month', 'Year']

#Replacing the column names with their, previously defined, english translations
brazil_gasdata.columns = new_col_names

#Converting the columns that have dates to datetime
brazil_gasdata['Initial_Observed_Date'] = pd.to_datetime(brazil_gasdata['Initial_Observed_Date'])
brazil_gasdata['Final_Observed_Date'] = pd.to_datetime(brazil_gasdata['Final_Observed_Date'])

#Identifying unique product names to convert to their english translation
brazil_gasdata.loc[:,'Product'].unique()

#Product names and their english translation
products = {'ETANOL HIDRATADO':'Hydrous Ethanol', 
            'GASOLINA COMUM':'Regular Gas', 
            'GLP':'LPG', 
            'GNV':'NGV', 
            'ÓLEO DIESEL':'Diesel', 
            'ÓLEO DIESEL S10':'Diesel S10'}

#Replacing the product names in the 'Product' column to their english translation
for product in products.keys():
    brazil_gasdata.loc[brazil_gasdata.Product == product, 'Product'] = products[product]

#Identifying the unique regions in the 'Region' column to translate in english       
brazil_gasdata.loc[:,'Region'].unique()        

#Region names and their english translation
regions = {'CENTRO OESTE':'MID WEST',
          'NORDESTE': 'NORTH EAST',
          'NORTE': 'NORTH',
          'SUDESTE': 'SOUTH EAST',
          'SUL': 'SOUTH'}

#Replacing the region names in the 'Region' column to their english translation
for region in regions.keys():
    brazil_gasdata.loc[brazil_gasdata.Region == region, 'Region'] = regions[region]

#export_csv = brazil_gasdata.to_csv (r'C:/Users/Norberto J Rancharan/Desktop/brazil_gas_data.csv', index = None, header=True)
















