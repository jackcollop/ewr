import pandas as pd
import altair as alt
import streamlit as st

import glob

files = glob.glob(r'*.csv')

dates=[]
al_fl = []
ar = []
az_nm = []
ca = []
ga = []
ks_ok = []
la =[]
mo = []
ms = []
nc_va = []
sc = []
tn = []
tx = []

tot_open = []
for file in files:
    temp = pd.read_csv(file).set_index('State')
    dates.append(file[-14:-4])
    al_fl.append(temp.loc['AL & FL']['Total Open'])
    ar.append(temp.loc['AR']['Total Open'])
    az_nm.append(temp.loc['AZ & NM']['Total Open'])
    ca.append(temp.loc['CA']['Total Open'])
    ga.append(temp.loc['GA']['Total Open'])
    ks_ok.append(temp.loc['KS & OK']['Total Open'])
    la.append(temp.loc['LA']['Total Open'])
    mo.append(temp.loc['MO']['Total Open'])
    ms.append(temp.loc['MS']['Total Open'])
    nc_va.append(temp.loc['NC & VA']['Total Open'])
    sc.append(temp.loc['SC']['Total Open'])
    tn.append(temp.loc['TN']['Total Open'])
    tx.append(temp.loc['TX']['Total Open'])

states = pd.DataFrame([dates, al_fl, ar, az_nm, ca, ga,ks_ok, la, mo, ms, nc_va, sc, tn, tx]).T

states.columns = ['Date', 'AL & FL', "AR", "AZ & NM",'CA', 'GA',"KS & OK", 'LA', 'MO','MS', "NC & VA", 'SC', 'TN', 'TX']

states['Southwest'] = states['TX'] + states['KS & OK']
states['Far West'] = states['AZ & NM'] + states['CA']
states['Southeast'] = states['AL & FL'] + states['GA'] + states['NC & VA'] + states['SC']
states['Mid South'] = states['AR'] + states['LA'] + states['MO'] + states['MS'] + states['TN']

states['Date'] = pd.to_datetime(states['Date'], format='mixed')

states.set_index('Date', inplace=True)
states.dropna(inplace=True)




st.subheader("Electronic warehouse receipts")
st.dataframe(states[['AL & FL', "AR", "AZ & NM",'CA', 'GA',"KS & OK", 'LA', 'MO','MS', "NC & VA", 'SC', 'TN', 'TX']].sort_index())

st.line_chart(states[['AL & FL', "AR", "AZ & NM",'CA', 'GA',"KS & OK", 'LA', 'MO','MS', "NC & VA", 'SC', 'TN', 'TX']].sort_index())
