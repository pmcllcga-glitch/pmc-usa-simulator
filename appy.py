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
import streamlit as st
import pandas as pd

# 1. 페이지 설정
st.set_page_config(page_title="PMC USA Investment Simulator", layout="wide")

# 2. 제목 (GDP 대신 정식 명칭)
st.title("PMC USA & Asia PCE: Investment Analysis")
st.markdown("---")

# 3. 입력창 (사이드바)
st.sidebar.header("Project Inputs")
units = st.sidebar.number_input("Total Units (가구 수)", min_value=1, value=100)
rent = st.sidebar.number_input("Avg Monthly Rent (평균 임대료 $)", min_value=1, value=2500)
saving_rate = st.sidebar.slider("Construction Cost Reduction (공사비 절감률 %)", 0, 50, 20)

# 4. 수익 계산 로직
construction_cost_per_unit = 150000  # 가구당 공사비 가이드
total_saving = units * 30000 * (saving_rate / 100)
early_revenue = units * rent * 5  # 5개월 조기 완공 가정

# 5. 메인 화면 결과 출력
col1, col2 = st.columns(2)
with col1:
    st.metric("Total Cost Savings", f"${total_saving:,.0f}")
with col2:
    st.metric("Early Revenue Benefit", f"${early_revenue:,.0f}")

st.write("---")

# 6. 상세 분석 표 (GDP 표 대신 들어가는 진짜 데이터)
st.subheader("Detailed Investment Analysis")
analysis_data = {
    "Description": ["Total Construction Cost", "Estimated Savings", "Early Completion Bonus", "Project ROI"],
    "Value": [
        f"${units * construction_cost_per_unit:,.0f}",
        f"${total_saving:,.0f}",
        f"${early_revenue:,.0f}",
        f"{((total_saving + early_revenue) / (units * construction_cost_per_unit) * 100):.2f}%"
    ]
}
df = pd.DataFrame(analysis_data)
st.table(df)

st.info("본 시뮬레이션은 PMC USA와 Asia PCE 간의 MOU에 근거한 기술 데이터를 바탕으로 작성되었습니다.")
