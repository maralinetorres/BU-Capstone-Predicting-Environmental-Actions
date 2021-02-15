#Explore the WRDS dataset

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import missingno as msno

stocks = pd.read_csv("/Users/maralinetorres/Documents/GitHub/Predicting-Environmental-and-Social-Actions/Datasets/wrds_52_dat.csv")


#Exploratory Data Analysis

#What do we have?
stocks.shape #766 rows and 10 columns
stocks.head(3) #We have yearly data from 2005 to 2020 for 52 companies
stocks.info() # 3 columns with null values 
stocks.isna().sum() # coluns act, ni and sales have 3 rows with null 

plt.figure(figsize=(10,5))
sns.heatmap(stocks.isnull(), cbar=False).set(title='Missing Data in the dataset')
plt.show()

msno.heatmap(stocks)
plt.show()
#Grab the records with the null values
stocks[(stocks.act.isna())| (stocks.ni.isna()) |  (stocks.sale.isna())]

#Tick --> BKR (Baker Hughes Company) is the company with null values for years 2014-2016
#See if we have other values for this company
bkr = stocks[stocks['tic'] == 'BKR'] #Yes, we have data for 2017 to 2020, maybe we can impute with average

#Drop duplicates if any
stocks.drop_duplicates(inplace=True) # We dont have duplicates

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
sns.distplot(stocks.act, ax=axs[0], color='b')
axs[0].set_title('Current Assets')
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