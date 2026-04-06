import streamlit as st
import pandas as pd

# 1. 페이지 설정
st.set_page_config(page_title="PMC USA Investment Simulator", layout="wide")

# 2. 메인 제목
st.title("PMC USA & Asia PCE: Investment Analysis")
st.markdown("---")

# 3. 입력창 (사이드바)
st.sidebar.header("Project Inputs")
units = st.sidebar.number_input("Total Units (가구 수)", min_value=1, value=100)
rent = st.sidebar.number_input("Avg Monthly Rent ($)", min_value=1, value=2500)
saving_rate = st.sidebar.slider("Cost Reduction (%)", 0, 50, 20)

# 4. 수익 계산
total_saving = units * 30000 * (saving_rate / 100)
early_revenue = units * rent * 5

# 5. 결과 화면 출력
col1, col2 = st.columns(2)
with col1:
    st.metric("Total Cost Savings", f"${total_saving:,.0f}")
with col2:
    st.metric("Early Revenue Benefit", f"${early_revenue:,.0f}")

st.write("---")

# 6. 상세 분석 표
st.subheader("Detailed Investment Analysis")
analysis_data = {
    "Description": ["Total Units", "Construction Cost Savings", "Early Completion Revenue", "Estimated Project Benefit"],
    "Value": [
        f"{units} Units",
        f"${total_saving:,.0f}",
        f"${early_revenue:,.0f}",
        f"${(total_saving + early_revenue):,.0f}"
    ]
}
df = pd.DataFrame(analysis_data)
st.table(df)

st.info("Based on PMC USA & Asia PCE Technology MOU")  
