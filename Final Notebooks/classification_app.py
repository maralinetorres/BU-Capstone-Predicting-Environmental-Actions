import streamlit as st
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from streamlit_metrics import metric, metric_row

st.title('Pilot Stocks - Predicting environmental and social actions')

stocks = pd.read_csv('/Users/maralinetorres/Documents/GitHub/Predicting-Environmental-and-Social-Actions/Datasets/pilot_stocks.csv')
stocks_utility = pd.read_csv('/Users/maralinetorres/Documents/GitHub/Predicting-Environmental-and-Social-Actions/Datasets/UtilityClassification.csv')
stocks_energy = pd.read_csv("/Users/maralinetorres/Documents/GitHub/Predicting-Environmental-and-Social-Actions/Datasets/EnergyClassification.csv")
companies_utility = stocks_utility.Company.unique().tolist()
companies_utility.append(' ')
companies_utility.sort()
companies_energy = stocks_energy.Company.unique().tolist()
companies_energy.append(' ')
companies_energy.sort()


option = st.selectbox('Which industry are you interested in?',(' ','Utility', 'Energy'), index=0)
show_table = False
if(option == 'Utility'):
    options_com = list(range(len(companies_utility)))
    company_map = dict(zip(options_com,companies_utility))
    option_com = st.selectbox('Which company are you interested in?',options_com, format_func=lambda x: companies_utility[x])
else:
    options_com = list(range(len(companies_energy)))
    company_map = dict(zip(options_com,companies_energy))
    option_com = st.selectbox('Which company are you interested in?',options_com, format_func=lambda x: companies_energy[x])
# st.write('You selected:', option)

# st.write('You selected: ', company_map[option_com])

# st.write('Below, we present the observations for the industry selected:')
com = company_map[option_com]
text = '###'+ ' '+ 'Metrics'
st.markdown(text)

show_table = option != ' ' and option_com != 0
if (show_table == True):
    if (option == 'Utility'):
        data = stocks_utility[stocks_utility.Company == com]
        orig_data = stocks.loc[stocks.Company == com,].groupby('Ticker')[['Year']].count().reset_index()
        emissions = int(data['GHG Scope 1'].iloc[0])
        classification = data.Classification.iloc[0]
        cluster = data.cluster.iloc[0]
        obs_in_cluster = stocks_utility[stocks_utility.cluster == cluster]['Company'].count()
        st.write(data)
        metric_row(
            {
                'Cluster Number': cluster,
                'Observations in cluster': obs_in_cluster
            }
        )

        metric_row(
            {
                'GHG Classification': data.GHG_Emission_category.iloc[0],
                'GHG Emissions': emissions
            }
        )

        metric_row(
            {
                'Years in data': orig_data['Year'].iloc[0]
            }
        )
        if (classification == 'Neutral'):
            st.warning('Neutral')
        elif(classification == 'Good Forecast'):
            st.success('Good Forecast')
        else:
            st.info('Improving')
    else:
        data = stocks_energy[stocks_energy.Company == com]
        orig_data = stocks.loc[stocks.Company == com,].groupby('Ticker')[['Year']].count().reset_index()
        emissions = int(data['GHG Scope 1'].iloc[0])
        classification = data.Classification.iloc[0]
        cluster = data.k3.iloc[0]
        obs_in_cluster = stocks_energy[stocks_energy.k3 == cluster]['Company'].count()
        st.write(data)
        metric_row(
            {
                'Cluster Number': cluster,
                'Observations in cluster': obs_in_cluster
            }
        )

        metric_row(
            {
                'GHG Classification': data.GHG_Emission_category.iloc[0],
                'GHG Emissions': emissions
            }
        )

        metric_row(
            {
                'Years in data': orig_data['Year'].iloc[0]
            }
        )
        if (classification == 'Neutral'):
            st.warning('Neutral')
        elif(classification == 'Good Forecast'):
            st.success('Good Forecast')
        else:
            st.info('Improving')