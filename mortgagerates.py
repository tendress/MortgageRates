import streamlit as st
from datetime import datetime
import pandas as pd
from fredapi import Fred
import matplotlib.pyplot as plt
#plt.style.use('fivethirtyeight')
 
API_Key = '5e8ed80210b838d7123b16e9e8faf111'
  
# First Create the FRED Object#
 
fred = Fred(api_key=API_Key)
 
######### Treasrury Spread 10 Year minus 2 Year##########
FEDFUNDSStats = fred.get_series(series_id='FEDFUNDS')
PrimeStats = fred.get_series(series_id='PRIME')

MORTGAGE30USStats = fred.get_series(series_id='MORTGAGE30US')
MORTGAGE15USStats = fred.get_series(series_id='MORTGAGE15US')
T10Y2YStats = fred.get_series(series_id='T10Y2Y')
DGS10Stats = fred.get_series(series_id='DGS10')
DGS2Stats = fred.get_series(series_id='DGS2')
#print(TreasurySpreadStats)


FedFundsData = pd.DataFrame(FEDFUNDSStats)
CurrentFedFundsRate = FedFundsData.tail(1).to_string(header=False)

PrimeData = pd.DataFrame(PrimeStats)
CurrentPrimeRate = PrimeData.tail(1).to_string(header=False)

Treasury10yrData = pd.DataFrame(DGS10Stats)
Current10yrTreasuryRate = Treasury10yrData.tail(1).to_string(header=False)

Treasury2yrData = pd.DataFrame(DGS2Stats)
Current2yrTreasuryRate = Treasury2yrData.tail(1).to_string(header=False)

Treasury10over2Data = pd.DataFrame(T10Y2YStats)
Current10over2Rate = Treasury10over2Data.tail(1).to_string(header=False)

Mortgage30yrData = pd.DataFrame(MORTGAGE30USStats)
Current30yrRate = Mortgage30yrData.tail(1).to_string(header=False)


Mortgage15yrData = pd.DataFrame(MORTGAGE15USStats)
Current15yrRate = Mortgage15yrData.tail(1).to_string(header=False)










st.title('Mortgage Rates Dashboard')

st.header('Fed Funds Rate')
st.write(CurrentFedFundsRate)
st.line_chart(FedFundsData)

st.header('Prime Rate')
st.write(CurrentPrimeRate)
st.line_chart(PrimeData)

st.header('10 Year vs. 2 Year Treasury')
st.write(Current10over2Rate)
st.line_chart(Treasury10over2Data)

st.header('10 Year Treasury Rate')
st.write(Current10yrTreasuryRate)
st.line_chart(Treasury10yrData)

st.header('2 Year Treasury Rate')
st.write(Current2yrTreasuryRate)
st.line_chart(Treasury2yrData)


st.header('30 Year Mortgage Rate')
st.write(Current30yrRate)
st.line_chart(Mortgage30yrData)

st.header('15 Year Mortgage Rate')
st.write(Current15yrRate)
st.line_chart(Mortgage15yrData)



