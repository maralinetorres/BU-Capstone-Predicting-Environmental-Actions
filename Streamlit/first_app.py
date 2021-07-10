import streamlit as st
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import numpy as np
import pandas as pd
# for distance and h-clustering

st.title('Pilot Stocks - Predicting environmental and social actions')

stocks_utility = pd.read_csv('/Users/maralinetorres/Documents/GitHub/Predicting-Environmental-and-Social-Actions/Datasets/Utility_comp_clustering.csv')
stocks_energy = pd.read_csv("/Users/maralinetorres/Documents/GitHub/Predicting-Environmental-and-Social-Actions/Datasets/Energy_comp_clustering.csv")


option = st.selectbox('Which industry are you interested in?',('<select>','Utility', 'Energy'), index=0)
st.write('You selected:', option)

st.write('Below, we present the observations for the industry selected:')

if option != '<select>':
    if option == 'Utility':
        data = stocks_utility
    else:
        data = stocks_energy

    st.write(data)


st.write('Below, the cluster formation for the industry selected:')
if option != '<select>':
    if option == 'Utility':
        # 1) Standarized the data
        st.write(stocks_utility)
