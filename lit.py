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
ewr.Date = pd.to_datetime(ewr.Date).dt.normalize()


df = pd.melt(ewr, id_vars=['Date'])


st.subheader("Electronic warehouse receipts")
st.dataframe(ewr.set_index('Date').sort_index(ascending=False))

c = alt.Chart(df).mark_line().encode(
    x='Date:T',
    y='value:Q',
    color='variable:N'
)

st.altair_chart(c)
