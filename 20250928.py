
import pandas as pd
import streamlit as st

# 1. 데이터 불러오기
df = pd.read_excel("test_input.xlsx")

# 2. Name_get 기준으로 정렬
df_sorted = df.sort_values(by="Name_get")

# 3. Streamlit에서 이름별로 나눠서 표시
st.title("이름별 정렬된 표")

# 고유한 이름 추출
unique_names = df_sorted["Name_get"].unique()

for name in unique_names:
    st.subheader(f"이름: {name}")
    # 해당 이름만 필터링
    sub_df = df_sorted[df_sorted["Name_get"] == name]
    st.dataframe(sub_df)
