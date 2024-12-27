import streamlit as st

st.title('素数個数判定')
st.markdown("2以上の自然数を入力してください")
n = st.number_input("自然数", value=2, step=1)

# 最大値nに対して、素数のリストを初期化
prime = [0] * 100  # 素数を格納するリスト（サイズ100で初期化）
prime[0] = 2  # 最初の素数2を格納
j = 0 # 素数リストのインデックス
counter = 0  # 割り算回数のカウンター
num = 3  # 次にチェックする数字

# 素数判定のループ
while num <= n:
    sosuhantei = 1  # 素数かどうかのフラグ
    i = 0  # 素数リストのインデックス
    while i<j and prime[i] * prime[i] <= num and prime[i] != 0:  # 素数リスト内の数で割り切れるか判定
        counter += 1  # 割り算回数をカウント
        if num % prime[i] == 0:
            sosuhantei = 0  # 割り切れれば素数ではない
        i += 1  # 次の素数をチェック
    if sosuhantei == 1:
        prime[j] = num  # 素数ならリストに追加
        j += 1  # インデックスを進める
    num += 2 # 次の数に進む

# 結果表示
st.write(f"1から{n}までの素数:")
i = 0
while prime[i] != 0:
    st.write(prime[i])
    i += 1

st.write(f"割り算を行った回数: {counter}")
