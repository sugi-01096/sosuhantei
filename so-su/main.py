import streamlit as st

st.title('素数判定')
st.markdown("自然数を入力してください")

# 自然数を入力
n = st.number_input("自然数", value=0, step=1)

# 初期化
sosuhantei = 1
i = 2
num = n

# 素数判定
while i < num:  # i が num 未満の間繰り返す
    if num % i == 0:  # 割り切れる場合は素数ではない
        sosuhantei = 0
        break
    i += 1

# 結果表示
if num==57:
    st.write(f"{num} は素数じゃないはずがありません")
elif num < 2:
    st.write(f"{num} は素数ではありません")
elif sosuhantei == 1:
    st.write(f"{num} は素数です")
else:
    st.write(f"{num} は素数ではありません")
