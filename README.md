# Predicting Environmental and Social Actions

This project focuses on predicting environmental and social actions based on historical data of ESG score, GHG scope, and total energy consumption. The objective is to give our client investment advice based on a company's environmental factors.
# Data collection methodology

We have used Yahoo finance API, WHARTON Research Data Services, and Bloomberg terminal data. 

## Description of the data

Bloomberg
Header | Description
---|---------
`Year` | The year of the data point
`12 Months Ending` | The last date of the year that the data was collected
`Environmental Disclosure Score` | Corporate environmental and social performance
`Total Energy Consumption` | Energy used by company during the year
`Ticker` | Ticker of company


WRDS
Header | Description
---|---------
`gvkey` | Number key assigned to each company (issue, currency, index) in the Capital IQ Compustat database
`datadate` | Date of observation
`fyear` | Fiscal year of observation
`tic` | Ticker of company
`cusip` | Code that identifies a North American financial security for the purposes of facilitating clearing and settlement of trades
`conm` | Full name of company
`act` | ??????????
`ni` | ??????????
`sale	` | ??????
`cik` | ????


## Usage

```python
import foobar

foobar.pluralize('word') # returns 'words'
foobar.pluralize('goose') # returns 'geese'
foobar.singularize('phenomena') # returns 'phenomenon'
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)

