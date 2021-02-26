#Explore the WRDS dataset

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import missingno as msno
from datetime import datetime, date

stocks = pd.read_csv("/Users/maralinetorres/Documents/GitHub/Predicting-Environmental-and-Social-Actions/Datasets/wrds_52_data.csv")


#Exploratory Data Analysis

#What do we have?
stocks.shape #782 rows and 10 columns
stocks.head(3) #We have yearly data from 2005 to 2020 for 52 companies
stocks.info() # 3 columns with null values 
stocks.isna().sum() # coluns at, ni and sales have 3 rows with null 
#Drop duplicates if any
stocks.drop_duplicates(inplace=True) # We dont have duplicates

#Remove 2020 data
stocks = stocks.loc[stocks.fyear != 2020, ]
stocks.shape #757 rows and 10 columns

plt.figure(figsize=(10,5))
sns.heatmap(stocks.isnull(), cbar=False).set(title='Missing Data in the dataset')
plt.show()

msno.heatmap(stocks)
plt.show()
#Grab the records with the null values
stocks[(stocks['at'].isna()) | (stocks['ni'].isna()) | (stocks['sale'].isna())]

#Tick --> BKR (Baker Hughes Company) is the company with null values for years 2014-2016
#See if we have other values for this company
bkr = stocks.loc[stocks['tic'] == 'BKR', ['at','ni','sale','fyear']] #Yes, we have data for 2017 to 2020, maybe we can impute with average
bkr['fyear'] = pd.to_datetime(bkr.fyear, format='%Y')


#Verify how the variables behave to decide how to impute
plt.figure(figsize=(3,3))
sns.pairplot(bkr)
plt.show()

fig, axs = plt.subplots(1,3, figsize=(25,5))
fig.tight_layout(pad=10)
fig.suptitle('Density distribution for continuous variables')
sns.barplot(bkr['fyear'].dt.year, bkr['at'], ax=axs[0], color='b')
axs[0].set_title('Total Assets')
sns.barplot(bkr['fyear'].dt.year, bkr.ni, ax=axs[1], color='g')
axs[1].set_title('Net Income')
sns.barplot(bkr['fyear'].dt.year, bkr.sale, ax=axs[2], color='r')
axs[2].set_title('Sales')
plt.show()

bkr_impute = bkr.copy()
bkr_impute['at'].fillna(bkr_impute['at'].min(), inplace=True)
bkr_impute['ni'].fillna(bkr_impute['ni'].min(), inplace=True)
bkr_impute['sale'].fillna(bkr_impute['sale'].min(), inplace=True)

fig, axs = plt.subplots(1,3, figsize=(25,5))
fig.tight_layout(pad=10)
fig.suptitle('Density distribution for continuous variables')
sns.barplot(bkr_impute['fyear'].dt.year, bkr_impute['at'], ax=axs[0], color='b')
axs[0].set_title('Total Assets')
sns.barplot(bkr_impute['fyear'].dt.year, bkr_impute.ni, ax=axs[1], color='g')
axs[1].set_title('Net Income')
sns.barplot(bkr_impute['fyear'].dt.year, bkr_impute.sale, ax=axs[2], color='r')
axs[2].set_title('Sales')
plt.show()

##Decide to fill with minimum
stocks['at'].fillna(stocks['at'].min(), inplace=True)
stocks['ni'].fillna(stocks['ni'].min(), inplace=True)
stocks['sale'].fillna(stocks['sale'].min(), inplace=True)

stocks.isna().sum() #no more nulls

#Count for each company how many year data we have
company_byyear = stocks.groupby(by='fyear')['tic'].count()
plt.figure(figsize=(10,5))
plt.title('Number of US companies by fiscal year')
sns.countplot(x='fyear', data=stocks, palette='mako')
plt.xlabel('Fiscal Year')
plt.show()

#Describe the data
stocks.describe().T

#See the asset distribution
fig, axs = plt.subplots(1,3, figsize=(25,5))
fig.tight_layout(pad=10)
fig.suptitle('Density distribution for continuous variables')
sns.distplot(stocks['at'], ax=axs[0], color='b')
axs[0].set_title('Total Assets')
sns.distplot(stocks.ni, ax=axs[1], color='g')
axs[1].set_title('Net Income')
sns.distplot(stocks.sale, ax=axs[2], color='r')
axs[2].set_title('Sales')
plt.show()

# compute the correlation matrix
corr = stocks.corr()
mask = np.triu(np.ones_like(corr, dtype=bool))
f, ax = plt.subplots(figsize=(10, 5))
fig.suptitle('Correlation matrix')
cmap = sns.diverging_palette(230, 20, as_cmap=True)
sns.heatmap(corr, mask=mask, cmap=cmap, vmax=.3, center=0,
            square=True, linewidths=.5, cbar_kws={"shrink": .5}).set(title='Correlation Matrix')
plt.show()

#Calculate $change in variables and FInancial ratios

########### GROWTH RATES ###########
## Sales and Assets should be positive
# Net income --> be careful interpretating net income because of positive and negative signs

company = list(stocks['conm'].unique())

def calculate_growth_ratios(company):
    for com in company:
        a =  stocks.loc[stocks.conm == com, ['fyear','at','ni','sale']]
        l = len(a)
        count = 0
        at2 = []
        ni = []
        sale = []
        while count < l:
            index = count - 1
            if(count != 0):
                #assets ratio
                current_a = a.iloc[count,1]
                last_a = a.iloc[index,1]
                at = ((current_a)/(last_a)-1)*100
                at2.append(at)
                ##net income ratio
                current_ni = a.iloc[count,2]
                last_ni = a.iloc[index,2]
                ni_1 = ((current_ni)/(last_ni)-1)*100
                ni.append(ni_1)
                #Sales ratio
                current_s = a.iloc[count,3]
                last_s = a.iloc[index,3]
                sales = ((current_s)/(last_s)-1)*100
                sale.append(sales)
            else:
                at2.append(0)
                ni.append(0)
                sale.append(0)
            count += 1

        stocks.loc[stocks.conm == com, 'Change_in_Sales'] = sale
        stocks.loc[stocks.conm == com,'Change_in_Assets'] = at2
        stocks.loc[stocks.conm == com, 'Change_in_NI'] = ni

calculate_growth_ratios(company)

######### FINANCIAL RATIOS ################
#ROA --> Return on assets
#Profit Margin
stocks['ROA'] = (stocks.ni/stocks['at']) * 100
stocks['Profit_Margin'] = (stocks.ni/stocks.sale) * 100

stocks.to_csv('stocks_52.csv')