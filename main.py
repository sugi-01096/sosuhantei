import streamlit as st
import json
import pandas as pd
from datetime import datetime
import pytz
import urllib.parse
st.title('素数判定')
st.markdown("自然数を入力してください")
n= input()
sosuhantei=1
i=2
num=n
for num in i+1:
    if n%i==0:
        sosuhantei=0
        i=num
    i=i+1
if n==1:
    st.write(n+"は素数ではありません")
elif sosuhantei ==1:
    st.write(n+"は素数です")
else:
   st.write(n+"は素数ではありません")