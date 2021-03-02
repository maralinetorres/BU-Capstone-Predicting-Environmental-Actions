import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import missingno as msno
from datetime import datetime, date

df = pd.read_csv("/Users/maralinetorres/Documents/GitHub/Predicting-Environmental-and-Social-Actions/Datasets/company_data.csv")
df.isna().sum() # coluns at, ni and sales have 3 rows with null 

df[(df.Ticker == 'BKR') & (df['Total_Assets'].isna()) & (df['Total_Sales'].isna()) & (df['Total_Assets'].isna())]
df.loc[(df.Ticker == 'BKR') & (df.Year <= 2016) &(df.Year >= 2014),  ['Total_Assets','Total_Sales','Net_Income','Company','Profitable','Change_in_Assets']]
df.loc[(df.Ticker == 'BKR') & (df.Year <= 2016) &(df.Year >= 2014),  ['Total_Assets','Total_Sales','Net_Income','Profit_Margin','Logarithm_Total_Assets','Logarithm_Total_Sales','ROA']] = np.nan
df.loc[(df.Ticker == 'BKR') & (df.Year <= 2016) &(df.Year >= 2014),['Change_in_Assets','Change_in_Sales','Change_in_NI']] = np.nan
df.loc[df.Ticker == 'BKR',:]
df.to_csv('company_data.csv', index=False)

df.info()

df.loc[(df.Ticker == 'BKR'), ['Year','Total_Assets','Total_Assets','Net_Income','Change_in_Sales','Change_in_Assets','Change_in_NI']]

df.Year.unique()

bloomberg = pd.read_csv("/Users/maralinetorres/Documents/GitHub/Predicting-Environmental-and-Social-Actions/Datasets/esg_52companies.csv")
bloomberg.Year.unique()

#Count for each company how many year data we have
company_byyear = stocks.groupby(by='fyear')['tic'].count()
plt.figure(figsize=(10,5))
plt.title('Number of US companies by fiscal year')
sns.countplot(x='fyear', data=stocks, palette='mako')
plt.xlabel('Fiscal Year')
plt.show()

df.isna().sum()

plt.figure(figsize=(10,5))
msno.matrix(df)
plt.show()

plt.figure(figsize=(10,5))
sns.barplot(x="Ticker", y="Profit_Margin", data=df)
plt.show()

df.loc[:,['Ticker','Profit_Margin']]
profit_margin_mean = df.groupby('Ticker')[['Profit_Margin']].mean().reset_index()
profit_margin_mean.sort_values(by='Profit_Margin', ascending=True)[:5]


plt.figure(figsize=(10,5))
sns.barplot(x="Ticker", y="Profit_Margin", data=profit_margin_mean.loc[profit_margin_mean.Ticker != 'BKR'])
plt.xticks(rotation=45)
plt.title('Companies Average Profit Margin')
plt.ylabel('Average profit margin')
plt.show()

plt.figure(figsize=(10,5))
sns.barplot(x="Ticker", y="Profit_Margin", data=profit_margin_mean)
plt.xticks(rotation=45)
plt.title('Companies Average Profit Margin')
plt.ylabel('Average profit margin')
plt.show()

bkr = df.loc[df.Ticker == 'BKR', :]
bkr['Year'] = pd.to_datetime(bkr.Year, format='%Y')
bkr['Year'] = bkr.Year.dt.year
x = bkr.groupby('Ticker')[['Total_Assets','Net_Income','Total_Sales']].describe().T
sns.barplot(x='Year',y='Profit_Margin', data = bkr)
plt.table(cellText=x.values,
          rowLabels=x.index,
          colLabels=x.columns,
          cellLoc = 'left', rowLoc = 'center',
          loc='left', bbox=[.30,.05,.3,.7])
plt.title('Baker Hughes CO Profit Margin')
plt.show()


plt.figure(figsize=(10,5))
sns.barplot(x="Ticker", y="Profit_Margin", data=profit_margin_mean.loc[profit_margin_mean.Ticker == 'BKR'])
plt.xticks(rotation=45)
plt.title('Companies Average Profit Margin')
plt.ylabel('Average profit margin')
plt.show()


#See the asset distribution
fig, axs = plt.subplots(1,3, figsize=(25,5))
fig.tight_layout(pad=10)
fig.suptitle('Density distribution')
sns.distplot(df.Total_Assets, ax=axs[0], color='b')
axs[0].set_title('Total Assets')
sns.distplot(df.Net_Income, ax=axs[1], color='g')
axs[1].set_title('Net Income')
sns.distplot(df.Total_Sales, ax=axs[2], color='r')
axs[2].set_title('Sales')
plt.show()


df.describe().T.to_csv('describe_data.csv')

y = df.loc[:,['Ticker','Profitable']]

profitable = df[df.Profitable == True].groupby('Year')[['Ticker']].count().reset_index()

sns.barplot(x='Year', y='Ticker', data=profitable, palette='mako')
plt.title('Number of profitable companies by year')
plt.show()