import streamlit as st

st.title('素数個数判定')
st.markdown("2以上の自然数を入力してください")
n = st.number_input("自然数", value=2, step=1)
prime[100]=[2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
j=1
counter=0
num=3
while num<=n:
    sosuhantei=1
    i=1
    while i<j and sosuhantei ==1 and print[i]*print[i]:
        counter=counter+1
        if num%prime[i]==0:
            sosuhantei=0
        i=i+1
        if sosuhantei==1:
            prime[j]=2
            j=j+1
        num=num+2
st.write("１から"+n+"までの素数")
i=0
while prime[i]!=0:
    st.write (prime[i])
    i=i+1
st.write("割り算を行った回数："+counter)
    
        
