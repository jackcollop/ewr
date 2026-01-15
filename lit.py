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
    if not 'ytd' in file: 
        f = pd.read_csv(file)
        dates.append(file[-14:-4])
        ccc.append(f.iloc[-1,4])
        so.append(f['Under Shipping Order'].iloc[-1])
        tot_open.append(f[f'Total Open'].iloc[-1])
        open25.append(f.iloc[-1,6])
#%%
ewr = pd.DataFrame([dates,ccc,so, tot_open, open25]).T
#%%
ewr.columns = ['Date', 'CCC', 'SO','Total Open','Current Year Open']



st.subheader("Electronic warehouse receipts")
st.dataframe(ewr.set_index('Date').sort_index(ascending=False))

st.line_chart(ewr.set_index('Date'))

st.subheader("Electronic warehouse receipts delta")
st.dataframe(ewr.set_index('Date').sort_index(ascending=False).diff())










