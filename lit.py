import pandas as pd
import streamlit as st
import plotly.express as px
import glob

files = glob.glob(r'*.csv')
dates = []
ccc = []
so = []
tot_open = []
open25 = []
new25 = []
for file in files:
    if not 'ytd' in file: 
        f = pd.read_csv(file)
        dates.append(file[-14:-4])
        ccc.append(f.iloc[-1,4])
        so.append(f['Under Shipping Order'].iloc[-1])
        tot_open.append(f[f'Total Open'].iloc[-1])
        open25.append(f.iloc[-1,6])
        new25.append(f.iloc[-1,3])
#%%
ewr = pd.DataFrame([dates,ccc,so, tot_open, open25, new25]).T
#%%
ewr.columns = ['Date', 'CCC', 'SO','Total Open','CY Open','New']

ewr['CY Lost'] = ewr['New'] - ewr['CY Open']


st.subheader("Electronic warehouse receipts")
st.dataframe(ewr.set_index('Date').sort_index(ascending=False))

fig = px.line(ewr.set_index('Date'))
st.plotly_chart(fig)

st.subheader(r"Electronic warehouse receipts $\Delta$")
st.dataframe(ewr.set_index('Date').sort_index(ascending=True).diff().sort_index(ascending=False))




















