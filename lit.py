import pandas as pd
import altair as alt
import streamlit as st

import glob

files = glob.glob(r'*.csv')
dates = []
ccc = []
so = []
tot_open = []
for file in files:
    f = pd.read_csv(file)
    dates.append(file[-14:-4])
    ccc.append(f.iloc[13,4])
    so.append(f.iloc[13,5])
    tot_open.append(f.iloc[13,10])
#%%
ewr = pd.DataFrame([dates,ccc,so, tot_open]).T
#%%
ewr.columns = ['Date', 'CCC', 'SO','Total Open']



st.subheader("Electronic warehouse receipts")
st.dataframe(ewr.set_index('Date').sort_index(ascending=False))

st.line_chart(ewr.set_index('Date'))
