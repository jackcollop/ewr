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
        y21.append(temp['2021'].sum(axis=1))
        
st.dataframe(pd.Series(y21))
