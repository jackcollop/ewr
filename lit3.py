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
for file in files:
    if 'ytd' in file:
        temp = pd.read_csv(file)
        dates.append(file[-14:-4])
        y21.append(temp['2021'].sum())
        y22.append(temp['2022'].sum())
        y23.append(temp['2023'].sum())
        y24.append(temp['2024'].sum())
        y25.append(temp['2025'].sum())
        
st.dataframe(pd.DataFrame({'2021':y21,'2022':y22,'2023':y23,'2024':y24,'2025':y25}, index=dates).sort_index(ascending=False))

st.dataframe(pd.DataFrame({'2021':y21/17523000,'2022':y22,'2023':y23,'2024':y24,'2025':y25}, index=dates).sort_index(ascending=False))
