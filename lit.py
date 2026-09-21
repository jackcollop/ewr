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
states = []
states_new = []
for file in files:
    if not 'ytd' in file: 
        f = pd.read_csv(file)
        dates.append(file[-14:-4])
        ccc.append(f.iloc[-1,4])
        so.append(f['Under Shipping Order'].iloc[-1])
        tot_open.append(f[f'Total Open'].iloc[-1])
        open25.append(f.iloc[-1,6])
        new25.append(f.iloc[-1,3])
        states.append(f[f'Total Open'].iloc[:-1])
        states_new.append(f.iloc[:-1,3])
#%%
ewr = pd.DataFrame([dates,ccc,so, tot_open, open25, new25]).T
#%%
ewr.columns = ['Date', 'CCC', 'SO','Total Open','CY Open','New']

ewr['CY Lost'] = ewr['New'] - ewr['CY Open']


st.subheader("Electronic warehouse receipts")
st.dataframe(ewr.set_index('Date').sort_index(ascending=False))

fig = px.line(ewr.set_index('Date').sort_index(ascending=False))
st.plotly_chart(fig)

st.subheader(r"Electronic warehouse receipts $\Delta$")
st.dataframe(ewr.set_index('Date').sort_index(ascending=True).diff().sort_index(ascending=False))

st.subheader(r"Total open receipts by state")
state_frame = pd.DataFrame(states)
state_frame.columns = ['AL/FL','AR','AZ/NM','CA','GA','KS/OK','LA','MO','MS','NC/VA','SC','TN','TX']
state_frame['WEST'] = state_frame['AZ/NM'] + state_frame['CA']
state_frame['SW'] = state_frame['KS/OK'] + state_frame['TX']
state_frame['MID'] = state_frame['LA'] + state_frame['MO'] + state_frame['MS'] + state_frame['TN']+ state_frame['AR']
state_frame['SE'] = state_frame['AL/FL'] + state_frame['GA'] + state_frame['NC/VA'] + state_frame['SC']

state_frame['Date'] = dates
state_frame.set_index('Date', inplace=True)
st.dataframe(state_frame.sort_index(ascending=False))


st.subheader(r"New receipts by state (season-to-date)")
state_frame2 = pd.DataFrame(states_new)
state_frame2.columns = ['AL/FL','AR','AZ/NM','CA','GA','KS/OK','LA','MO','MS','NC/VA','SC','TN','TX']
state_frame2['WEST'] = state_frame2['AZ/NM'] + state_frame2['CA']
state_frame2['SW'] = state_frame2['KS/OK'] + state_frame2['TX']
state_frame2['MID'] = state_frame2['LA'] + state_frame2['MO'] + state_frame2['MS'] + state_frame2['TN']+ state_frame2['AR']
state_frame2['SE'] = state_frame2['AL/FL'] + state_frame2['GA'] + state_frame2['NC/VA'] + state_frame2['SC']
state_frame2['Date'] = dates
state_frame2.set_index('Date', inplace=True)
st.dataframe(state_frame2.sort_index(ascending=False))

st.subheader(r"Daily receipts by state")
st.dataframe(state_frame2.sort_index(ascending=True).diff().sort_index(ascending=False))





















