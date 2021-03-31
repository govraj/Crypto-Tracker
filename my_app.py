# -*- coding: utf-8 -*-
"""
Created on Wed Mar 31 21:15:54 2021

@author: GOVINDA
"""

import streamlit as st
import pandas_datareader.data as web
from datetime import datetime as dt, timedelta as td

st.title('PathToDataScience Crypto Tracker')

# Add as many pairs as you like
opts = st.selectbox('Select Pair',(
    'BTC-USD',
    'ETH-USD',
    'BNB-USD',
    'XRP-USD',
    'LINK-USD',
    'DOGE-USD',
    'EOS-USD',
    'BSV-USD'))

# Get one year data based on selection
prices = web.get_data_yahoo(
    opts,
    start=dt.now() - td(days=365),
    end = dt.now()
)
# Chart It
st.line_chart(prices)