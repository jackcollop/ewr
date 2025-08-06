import pandas as pd
import altair as alt
import streamlit as st

import glob

files = glob.glob(r'*.csv')
dates = []
ccc = []
so = []
tot_open = []
open25 = []
for file in files:
    f = pd.read_csv(file)
    dates.append(file[-14:-4])
    year = file[4:8]
    ccc.append(f[f'Held by CCC {year}'].iloc[-1])
    so.append(f['Under Shipping Order'].iloc[-1])
    tot_open.append(f[f'Total Open'].iloc[-1])
    open25.append(f['Open 2025'].iloc[-1])
#%%
ewr = pd.DataFrame([dates,ccc,so, tot_open, open25]).T
#%%
ewr.columns = ['Date', 'CCC', 'SO','Total Open','Open 2025']



st.subheader("Electronic warehouse receipts")
st.dataframe(ewr.set_index('Date').sort_index(ascending=False))

st.line_chart(ewr.set_index('Date'))





