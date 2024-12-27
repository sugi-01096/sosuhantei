import streamlit as st

st.title('素数個数判定')
st.markdown("自然数を入力してください")
n = st.number_input("自然数", value=0, step=1)
