---
output:
  pdf_document: default
  html_document: default
---
# Predicting Environmental and Social Actions

This project focuses on predicting environmental and social actions based on historical data of ESG score, GHG scope, and total energy consumption. The objective is to give our client investment advice based on a company's environmental factors. To do so, we plan to develop an accurate, unbiased and robust model to determine the future environmental and social accountability of a company.


# Data collection methodology

For our initial pilot model, we collected data from Wharton Research Data Services (WRDS), Yahoo finance API and Bloomberg terminal data. 

After the pilot, we added more data to this project. This new datasource was collected from : Freiberg, David and Park, DG and Serafeim, George and Zochowski, Rob. 2020. Corporate Environmental Impact: Measurement, Data and Information. Harvard Business School, Impact-Weighted Accounts Project report.

## Description of the data

### Individual datasets 

WRDS
Header | Description
---|---------
`gvkey` | Number key assigned to each company (issue, currency, index) in the Capital IQ Compustat database
`datadate` | Date of observation
`fyear` | Fiscal year of observation
`tic` | Ticker of company
`cusip` | Code that identifies a North American financial security for the purposes of facilitating clearing and settlement of trades
`conm` | Full name of company
`act` | Total assets -  it is all the assets, or items of value, a small business owns. Included in total assets is cash, accounts receivable, inventory, equipment, etc.
`ni` | Net income/loss - is an entity's income minus cost of goods sold, expenses, depreciation and amortization, interest, and taxes for an accounting period.
`sale	` | Total sales - the total amount of all cash, credit, installment, and conditional sales made during the period covered by the return.
`cik` | SEC identifying number

Yahoo
Header | Description
---|---------
`Adj Close` | Closing price to reflect that stock's value after accounting for any corporate actions
`Close` | Close price - is the raw price, which is just the cash value of the last transacted price before the market closes.
`High` | Highest stock price of the day
`Low` | Lowest stock price of the day
`Ticker` | Ticker of company
`Volume` | The amount of an asset or security that changed hands during day

Bloomberg
Header | Description
---|---------
`Year` | The year of the data point
`12 Months Ending` | The last date of the year that the data was collected
`GHG Scope 1` | Direct emissions from sources that are owned or controlled by the Agency
`Environmental Disclosure Score` | is a percentage figure that represents the company aggregated level of disclosure against quantitative ESG data points drawn from global standards, that are considered to be most relevant for its industry
`Total Energy Consumption` | Energy used by company during the year
`Ticker` | Ticker of company


### Pilot dataset


Pilot Stock 
Header | Description
---|---------
`Year` | The year of the data point
`Ticker` | Ticker of company
`Environmental Disclosure Score` | is a percentage figure that represents the company aggregated level of disclosure against quantitative ESG data points drawn from global standards, that are considered to be most relevant for its industry
`GHG Scope 1` | Direct emissions from sources that are owned or controlled by the Agency
`Total Energy Consumption` | Energy used by company during the year
`Change_in_EDS` | Change in the Environmental Disclosure Score - ((Environmental Disclosure Score in Current Year) / (Environmental Disclosure Score Last Year) - 1) * 100
`Change_in_GHG` | Change in the GHG Scope 1 - ((GHG Scope 1 in Current Year) / (GHG Scope 1 Last Year) - 1) * 100
`Change_in_TEC` | Change in the Total Energy Consumption- ((Total Energy Consumption in Current Year) / (Total Energy Consumption Last Year) - 1) * 100
`Company` | Full name of company
`Total_Assets` | It is all the assets, or items of value, a small business owns. Included in total assets is cash, accounts receivable, inventory, equipment, etc.
`Net_Income` | It is an entity's income minus cost of goods sold, expenses, depreciation and amortization, interest, and taxes for an accounting period.
`Total_Sales` | The total amount of all cash, credit, installment, and conditional sales made during the period covered by the return.
`Change_in_Sales` | ((Sales in Current Year) / (Sales Last Year) - 1) * 100
`Change_in_Assets` | ((Assets in Current Year) / (Assets Last Year) - 1) * 100
`Change_in_NI` | Change in Net Income - ((Net Income in Current Year) / (Net Income Last Year) - 1) * 100
`ROA` | Return on Assets- indicator of how profitable a company is relative to its total assets.
`Profit_margin` | Indicates how many cents of profit has been generated for each dollar of sale.
`Annual_Stock_Return` | Expresses the stock's increase in value over a designated period of time.
`Ratio of GHG Emissions to Total Assets` | (GHG Scope 1 * 1000) / Total Assets
`Ratio of GHG Emissions to Total Sales` | (GHG Scope 1 * 1000) / Total Sales
`Ratio of Total Energy Consumption to Total Assets` | (Total Energy Consumption * 1000) / Total Assets
`Ratio of Total Energy Consumption to Total Sales` | (Total Energy Consumption * 1000) / Total Sales
`Profitable` | Indicates if the company was profitable that year (Net Income > 0 or not)
`Logarithm_Total_Assets` | Natural logarithm for total assets
`Logarithm_Total_Sales` | Natural logarithm for total sales

### Environmental Impact dataset





# Navigate our analysis

We work with the following notebooks (and in this order):

1. Data Collection, Cleaning and Exploratory Data Analysis
2. Exploratory Data Analysis-PilotStocks
3. GHG Scope 1 Predictive Model Evaluation
4. Fixed_Effects_Regressions
5. EDA_for_ISIN_&_WRDS


