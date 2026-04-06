import streamlit as st
import pandas as pd

# 1. 페이지 설정
st.set_page_config(page_title="PMC USA Investment Simulator", layout="wide")

# 2. 제목
st.title("PMC USA & Asia PCE: Investment Analysis")
st.markdown("---")

# 3. 입력창
st.sidebar.header("Project Inputs")
units = st.sidebar.number_input("Total Units", min_value=1, value=100)
rent = st.sidebar.number_input("Avg Monthly Rent ($)", min_value=1, value=2500)
saving_rate = st.sidebar.slider("Cost Reduction (%)", 0, 50, 20)

# 4. 결과 출력
st.metric("Estimated Cost Savings", f"${units * 30000 * (saving_rate/100):,.0f}")
st.success("Simulation based on Asia PCE Full PC Technology")
