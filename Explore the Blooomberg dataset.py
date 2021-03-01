#Explore the Blooomber dataset

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import missingno as msno
from datetime import datetime, date
import math

esg = pd.read_csv("/Users/maralinetorres/Documents/GitHub/Predicting-Environmental-and-Social-Actions/Datasets/ESG_Formatted_52.csv")
stocks = pd.read_csv("/Users/maralinetorres/Documents/GitHub/Predicting-Environmental-and-Social-Actions/Datasets/wrds_52_data.csv")

# Environmental score goes from 1-100 

# % Change in Variables and Scaling by firm size
#GHG %Change 
company = list(esg['Ticker'].unique())

def calculate_growth_ratios(company):
    for com in company:
        a =  esg.loc[esg.Ticker == com, ['Year','Environmental Disclosure Score','GHG Scope 1','Total Energy Consumption']]
        l = len(a)
        count = 0
        eds = []
        ghg = []
        tec = []
        while count < l:
            index = count - 1
            if(count != 0):
                #Environmental Disclosure
                current_eds = a.iloc[count,1]
                last_eds = a.iloc[index,1]
                env = ((current_eds)/(last_eds)-1)*100
                if(math.isnan(env)):
                    env = 0
                eds.append(env)
                ##GHG Scope
                current_ghg = a.iloc[count,2]
                last_ghg = a.iloc[index,2]
                g = ((current_ghg)/(last_ghg)-1)*100
                if(math.isnan(g)):
                    g = 0
                ghg.append(g)
                #Total Energy consumption
                current_energy = a.iloc[count,3]
                last_energy = a.iloc[index,3]
                total = ((current_energy)/(last_energy)-1)*100
                if(math.isnan(total)):
                    total = 0
                tec.append(total)
            else:
                eds.append(0)
                ghg.append(0)
                tec.append(0)
            count += 1

        esg.loc[esg.Ticker == com, 'Change_in_EDS'] = eds
        esg.loc[esg.Ticker == com,'Change_in_GHG'] = ghg
        esg.loc[esg.Ticker == com, 'Change_in_TEC'] = tec

calculate_growth_ratios(company)
    
esg.loc[esg.Ticker == 'CMS',]

esg.to_csv('bloomberg_ratios.csv')

final = pd.merge(esg, stocks, how ='left', left_on = ['Ticker', 'Year'], right_on = ['tic', 'fyear'])

final['Ratio of GHG Emissions to Total Assets'] = final['GHG Scope 1'] * 1000 / final['at']
final['Ratio of GHG Emissions to Total Sales'] = final['GHG Scope 1'] * 1000 / final['sale']
final['Ratio of Total Energy Consumption to Total Assets'] = final['Total Energy Consumption'] * 1000 / final['at']
final['Ratio of Total Energy Consumption to Total Sales'] = final['Total Energy Consumption'] * 1000 / final['sale']

cols = ["fyear", "gvkey", "datadate", "gvkey", "tic", "cusip", "conm","at","ni","sale","cik"]
final.drop(columns=cols, inplace=True)

final.to_csv('esg_52companies.csv')
final.loc[final.Ticker == 'XOM', ['GHG Scope 1']]
stock
#Ratio of GHG Emissions to Total Assets