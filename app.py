import streamlit as st
import pandas as pd

# 1. 페이지 설정 (브라우저 탭에 표시될 이름)
st.set_page_config(page_title="PMC USA Investment Simulator", layout="wide")

# 2. 메인 제목
st.title("PMC USA & Asia PCE: Investment Analysis")
st.markdown("---")

# 3. 입력창 (사이드바 - 투자자가 직접 조절하는 부분)
st.sidebar.header("Project Inputs")
units = st.sidebar.number_input("Total Units (총 가구 수)", min_value=1, value=100)
rent = st.sidebar.number_input("Avg Monthly Rent (월 임대료 $)", min_value=1, value=2500)
saving_rate = st.sidebar.slider("PCE Technology Cost Reduction (%)", 0, 50, 20)

# 4. 수익 계산 로직
# 가구당 3만 달러 절감 가정 및 공기 단축 수익 계산
total_saving = units * 30000 * (saving_rate / 100)
early_revenue = units * rent * 5  # 5개월 조기 완공 가정

# 5. 메인 결과 화면 출력
col1, col2 = st.columns(2)
with col1:
    st.metric("Total Construction Cost Savings", f"${total_saving:,.0f}")
with col2:
    st.metric("Early Completion Revenue (5 Months)", f"${early_revenue:,.0f}")

st.write("---")

# 6. 상세 분석 표
st.subheader("Detailed Investment Analysis")
analysis_data = {
    "Description": [
        "Total Project Units", 
        "Construction Cost Savings (PCE Tech)", 
        "Early Completion Revenue Benefit", 
        "Total Estimated Project Benefit"
    ],
    "Value": [
        f"{units} Units",
        f"${total_saving:,.0f}",
        f"${early_revenue:,.0f}",
        f"${(total_saving + early_revenue):,.0f}"
    ]
}
df = pd.DataFrame(analysis_data)
st.table(df)

# 7. 하단 정보
st.info("This analysis is based on PMC USA & Asia PCE Technology MOU and standardized US construction costs.")
st.caption("© 2026 PMC USA Management. All rights reserved.")
