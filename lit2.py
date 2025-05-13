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


dif = states[['Southwest','Far West','Southeast','Mid South']].sort_index().diff()

st.dataframe(dif.groupby(dif.index.isocalendar().week).sum())
st.subheader("Southwest")
st.bar_chart(dif[['Southwest']])
st.subheader("Mid South")
st.bar_chart(dif[['Mid South']])
st.subheader("Southeast")
st.bar_chart(dif[['Southeast']])
st.subheader("Far West")
st.bar_chart(dif[['Far West']])


st.subheader("Texas")
st.bar_chart(states.sort_index()['TX'].diff())
st.subheader("Georgia")
st.bar_chart(states.sort_index()['GA'].diff())
st.subheader("Arkansas")
st.bar_chart(states.sort_index()['AR'].diff())
st.subheader("Kansas / Oklahoma")
st.bar_chart(states.sort_index()['KS & OK'].diff())
st.subheader("Mississippi")
st.bar_chart(states.sort_index()['MS'].diff())
st.subheader("Tennessee")
st.bar_chart(states.sort_index()['TN'].diff())
st.subheader("North Carolina / Virginia")
st.bar_chart(states.sort_index()['NC & VA'].diff())





