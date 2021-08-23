# Predicting Environmental and Social Actions

This project focuses on predicting environmental and social actions based on historical data of ESG score, GHG scope, and total energy consumption. The objective is to give our client investment advice based on a company's environmental factors. To do so, we plan to develop an accurate, unbiased and robust model to determine the future environmental and social accountability of a company.


# Data collection methodology

For our initial pilot model, we collected data from Wharton Research Data Services (WRDS), Yahoo finance API and Bloomberg terminal data. 

After the pilot, we added more data to this project. This new datasource was collected from : Freiberg, David and Park, DG and Serafeim, George and Zochowski, Rob. 2020. Corporate Environmental Impact: Measurement, Data and Information. Harvard Business School, Impact-Weighted Accounts Project report.

# Navigate our analysis

We work with the following notebooks (and in this order):

1. Data Collection, Cleaning and Exploratory Data Analysis
2. Exploratory Data Analysis-PilotStocks
3. GHG Scope 1 Predictive Model Evaluation
4. Fixed_Effects_Regressions
5. PredictingTimeSeries_&_PilotStock_CompDescription
6. IndustriesPredictingTimeSeries
7. PredictingTimeSeries - GHG Scope
8. DistilBERT_and_level_regressions
9. DistilBERT_Companiesdescription
10. Building_Classification_Model
Appendix Notebook: Environmental-Impact-Data Cleaning

# Description of the data

## Individual datasets 

WRDS

Preview
![Image of WRDS](https://github.com/maralinetorres/Predicting-Environmental-and-Social-Actions/blob/main/Datasets/Previews/WRDS.png?raw=true)

Feature | Description
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

Preview
![Image of Yahoo](https://github.com/maralinetorres/Predicting-Environmental-and-Social-Actions/blob/main/Datasets/Previews/Yahoo.png?raw=true)

Feature | Description
---|---------
`Adj Close` | Closing price to reflect that stock's value after accounting for any corporate actions
`Close` | Close price - is the raw price, which is just the cash value of the last transacted price before the market closes.
`High` | Highest stock price of the day
`Low` | Lowest stock price of the day
`Ticker` | Ticker of company
`Volume` | The amount of an asset or security that changed hands during day

Bloomberg

Preview
![Image of Bloomberg](https://github.com/maralinetorres/Predicting-Environmental-and-Social-Actions/blob/main/Datasets/Previews/Bloomberg.png?raw=true)
Feature | Description
---|---------
`Year` | The year of the data point
`12 Months Ending` | The last date of the year that the data was collected
`GHG Scope 1` | Direct emissions from sources that are owned or controlled by the Agency
`Environmental Disclosure Score` | is a percentage figure that represents the company aggregated level of disclosure against quantitative ESG data points drawn from global standards, that are considered to be most relevant for its industry
`Total Energy Consumption` | Energy used by company during the year
`Ticker` | Ticker of company


## Pilot dataset


Pilot Stock 
Feature | Description
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

## Environmental Impact dataset


Environmental Impact
Feature | Description
---|---------
`ISIN` | An International Securities Identification Number (ISIN) is a code that uniquely identifies a specific securities issue
`Year` | The year in which the environmental impact was incurred by the firm's operations.
`Company Name` | The name of the issuer.
`Country ` | The country in which the companies' headquarters are located.
`Industry` | Exiobase industry category to which the firm belongs
`Environmental Intensity (Sales)` | The monetized environmental impact of the firm's operations during the specific year indicated in column Year divided by revenue in that year
`Environmental Intensity (Op Inc)` | The monetized environmental impact of the firm's operations during the specific year indicated in column Year divided by operating income in that year
`Total Environmental Cost`  | The total monetized environmental impact of the firm's operations during the specific year indicated in Column Year.
`Working Capacity` | Captures human health effects from climate change, air pollution, and toxicity.
`Fish Production Capacity` | Includes acidification, eutrophication, climate change, and toxicity. 
`Crop Production Capacity` | Captures soil degradation, air pollution, climate change, and land use. 
`Meat Production Capacity` | Includes soil degradation, climate change, land use, and toxicity. 
`Biodiversity` | Captures land use and toxicity. 
`Abiotic Resources` | Includes environmental impacts from mining. 
`Water production capacity` | Captures climate change, land use, and water pollution. 
`Wood Production Capacity` | Includes climate change, air pollution, and land use. 
`SDG 1.5` | By 2030, build the resilience of the poor and those in vulnerable situations and reduce their exposure and vulnerability to climate-related extreme events and other economic, social and environmental shocks and disasters.
`SDG 2.1` | By 2030, end hunger and ensure access by all people, in particular the poor and people in vulnerable situations, including infants, to safe, nutritious and sufficient food all year round.
`SDG 2.2` | By 2030, end all forms of malnutrition, including achieving, by 2025, the internationally agreed targets on stunting and wasting in children under 5 years of age, and address the nutritional needs of adolescent girls, pregnant and lactating women and older persons.
`SDG 2.3` | By 2030, double the agricultural productivity and incomes of small-scale food producers, in particular women, indigenous peoples, family farmers, pastoralists and fishers, including through secure and equal access to land, other productive resources and inputs, knowledge, financial services, markets and opportunities for value addition and non-farm employment.
`SDG 2.4` | By 2030, ensure sustainable food production systems and implement resilient agricultural practices that increase productivity and production, that help maintain ecosystems, that strengthen capacity for adaptation to climate change, extreme weather, drought, flooding and other disasters and that progressively improve land and soil quality.
`SDG 3.3` | By 2030, end the epidemics of AIDS, tuberculosis, malaria and neglected tropical diseases and combat hepatitis, water-borne diseases and other communicable diseases.
`SDG 3.4` | By 2030, reduce by one third premature mortality from non-communicable diseases through prevention and treatment and promote mental health and well-being.
`SDG 3.9` | By 2030, substantially reduce the number of deaths and illnesses from hazardous chemicals and air, water and soil pollution and contamination.
`SDG 6` | Ensure availability and sustainable management of water and sanitation for all.
`SDG 12.2` | By 2030, achieve the sustainable management and efficient use of natural resources.
`SDG 14.1` | By 2025, prevent and significantly reduce marine pollution of all kinds, in particular from land-based activities, including marine debris and nutrient pollution.
`SDG 14.2` |By 2020, sustainably manage and protect marine and coastal ecosystems to avoid significant adverse impacts, including by strengthening their resilience, and take action for their restoration in order to achieve healthy and productive oceans.
`SDG 14.3` | Minimize and address the impacts of ocean acidification, including through enhanced scientific cooperation at all levels.
`SDG 14.c` | Enhance the conservation and sustainable use of oceans and their resources by implementing international law as reflected in UNCLOS, which provides the legal framework for the conservation and sustainable use of oceans and their resources.
`SDG 15.1` |By 2020, ensure the conservation, restoration and sustainable use of terrestrial and inland freshwater ecosystems and their services, in particular forests, wetlands, mountains and drylands, in line with obligations under international agreements.
`SDG 15.2` | By 2020, promote the implementation of sustainable management of all types of forests, halt deforestation, restore degraded forests and substantially increase afforestation and reforestation globally.
`SDG 15.5` | Take urgent and significant action to reduce the degradation of natural habitats, halt the loss of biodiversity and, by 2020, protect and prevent the extinction of threatened species.
`% Imputed` | Refers to the percentage of a firm-year's total environmental impact that is derived from our imputation methodology using the Exiobase's industry-level data.

Source: “Freiberg, David and Park, DG and Serafeim, George and Zochowski, Rob. 2020. Corporate Environmental Impact: Measurement, Data and Information. Harvard Business School, Impact-Weighted Accounts Project report.”


## Financial Information dataset


Preview
![Image of Financial](https://github.com/maralinetorres/Predicting-Environmental-and-Social-Actions/blob/main/Datasets/Previews/Financial_Dataset.png?raw=true)

Financial Information
Feature | Description
---|---------
`gvkey` | The Global Company Key is a unique six-digit number key assigned to each company
`fyear` | Fiscal year
`at` | Assets
`isin` | An International Securities Identification Number (ISIN) is a code that uniquely identifies a specific securities issue
`conm` | Company name
`fic` | ISO country code -Incorporation
`sic` | Standard industry classification code 
 
 

