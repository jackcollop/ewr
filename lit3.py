import pandas as pd
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

y21 = []
y22 = []
y23 = []
y24 = []
y25 = []

tot_open = []

dfs = []

for file in files:
    if 'ytd' in file:
        temp = pd.read_csv(file)
        dates.append(file[-14:-4])
        y21.append(temp['2021'].sum())
        y22.append(temp['2022'].sum())
        y23.append(temp['2023'].sum())
        y24.append(temp['2024'].sum())
        y25.append(temp['2025'].sum())
        temp['Date'] = file[-14:-4]
        dfs.append(temp)
        
usa = pd.DataFrame({'2021':y21,'2022':y22,'2023':y23,'2024':y24,'2025':y25}, index=dates).sort_index(ascending=False)

st.dataframe(usa)
st.line_chart(usa)

us = usa
us['2021'] = us['2021']/17523000
us['2022'] = us['2022']/14468000
us['2023'] = us['2023']/12066000
us['2024'] = us['2024']/14413000
us['2025'] = us['2025']/14268000

st.dataframe(us.round(3).mul(100))
st.line_chart(us.round(3).mul(100))

f = pd.concat(dfs)

st.dataframe(f)
