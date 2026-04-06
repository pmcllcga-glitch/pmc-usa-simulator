import streamlit as st
import pandas as pd

# 1. 페이지 설정
st.set_page_config(page_title="PMC USA Investment Simulator", layout="wide")

# 2. 제목
st.title("PMC USA & Asia PCE: Investment Analysis")
st.write("---")

# 3. 사이드바 입력창
st.sidebar.header("Project Inputs")
units = st.sidebar.number_input("Total Units", min_value=1, value=100)
avg_rent = st.sidebar.number_input("Average Monthly Rent ($)", min_value=1, value=2500)
reduction_rate = st.sidebar.slider("Construction Cost Reduction (%)", 0, 50, 20)

# 4. 계산 로직
total_saving = units * 30000 * (reduction_rate / 100) # 예시 계산
early_revenue = units * avg_rent * 5 # 5개월 조기 완공 가정

# 5. 결과 화면
col1, col2 = st.columns(2)
with col1:
    st.metric("Cost Savings", f"${total_saving:,.0f}")
with col2:
    st.metric("Early Revenue Benefit", f"${early_revenue:,.0f}")

st.success("Simulation Complete! This data is based on PMC & Asia PCE MOU.")
