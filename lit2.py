import pandas as pd
import altair as alt
import streamlit as st
import datetime as dt

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
    al_fl.append(temp.loc['AL & FL']['Held by CCC 2024'])
    ar.append(temp.loc['AR']['Held by CCC 2024'])
    az_nm.append(temp.loc['AZ & NM']['Held by CCC 2024'])
    ca.append(temp.loc['CA']['Held by CCC 2024'])
    ga.append(temp.loc['GA']['Held by CCC 2024'])
    ks_ok.append(temp.loc['KS & OK']['Held by CCC 2024'])
    la.append(temp.loc['LA']['Held by CCC 2024'])
    mo.append(temp.loc['MO']['Held by CCC 2024'])
    ms.append(temp.loc['MS']['Held by CCC 2024'])
    nc_va.append(temp.loc['NC & VA']['Held by CCC 2024'])
    sc.append(temp.loc['SC']['Held by CCC 2024'])
    tn.append(temp.loc['TN']['Held by CCC 2024'])
    tx.append(temp.loc['TX']['Held by CCC 2024'])

states = pd.DataFrame([dates, al_fl, ar, az_nm, ca, ga,ks_ok, la, mo, ms, nc_va, sc, tn, tx]).T

states.columns = ['Date', 'AL & FL', "AR", "AZ & NM",'CA', 'GA',"KS & OK", 'LA', 'MO','MS', "NC & VA", 'SC', 'TN', 'TX']

states['Southwest'] = states['TX'] + states['KS & OK']
states['Far West'] = states['AZ & NM'] + states['CA']
states['Southeast'] = states['AL & FL'] + states['GA'] + states['NC & VA'] + states['SC']
states['Mid South'] = states['AR'] + states['LA'] + states['MO'] + states['MS'] + states['TN']

states['Date'] = pd.to_datetime(states['Date'], format='mixed')

states.set_index('Date', inplace=True)
states.dropna(inplace=True)


dif = states.sort_index().diff()

st.subheader("Held by CCC 2024")
st.dataframe(states.sort_index(ascending=False))
st.subheader("Weekly change in CCC totals")
st.dataframe(dif.groupby(dif.index.isocalendar().week).sum().sort_index(ascending=False))

st.area_chart(states[['Southwest','Mid South','Southeast','Far West']], stacked=True)




