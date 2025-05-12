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
    al_fl.append(temp.loc['AL & FL']['Under Shipping Order'])
    ar.append(temp.loc['AR']['Under Shipping Order'])
    az_nm.append(temp.loc['AZ & NM']['Under Shipping Order'])
    ca.append(temp.loc['CA']['Under Shipping Order'])
    ga.append(temp.loc['GA']['Under Shipping Order'])
    ks_ok.append(temp.loc['KS & OK']['Under Shipping Order'])
    la.append(temp.loc['LA']['Under Shipping Order'])
    mo.append(temp.loc['MO']['Under Shipping Order'])
    ms.append(temp.loc['MS']['Under Shipping Order'])
    nc_va.append(temp.loc['NC & VA']['Under Shipping Order'])
    sc.append(temp.loc['SC']['Under Shipping Order'])
    tn.append(temp.loc['TN']['Under Shipping Order'])
    tx.append(temp.loc['TX']['Under Shipping Order'])

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





