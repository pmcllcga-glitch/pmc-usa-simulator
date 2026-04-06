import streamlit as st
import pandas as pd

# 1. 페이지 설정 (브라우저 탭 이름)
st.set_page_config(page_title="PMC USA Investment Simulator", layout="wide")

# 2. 메인 제목
st.title("PMC USA & Asia PCE: Investment Analysis")
st.markdown("---")

# 3. 홍보 이미지 배포 (방금 올리신 그 조감도!)
# 파일 이름을 꼭 형님이 깃허브에 올리신 이름으로 바꾸세요!
# 예: pmc_layout.jpg
try:
    st.image("pmc_layout.jpg", use_container_width=True, caption="PMC Precast Concrete System: From Foundation to Finished Modular Living")
except:
    st.info("조감도 이미지를 업로드 중입니다... (pmc_layout.jpg 파일이 필요합니다)")

st.write("Modern multifamily development in Texas.jpg", ...")

# 4. 입력창 (사이드바)
st.sidebar.header("Project Inputs")
units = st.sidebar.number_input("Total Units (총 가구 수)", min_value=1, value=100)
rent = st.sidebar.number_input("Avg Monthly Rent (월 임대료 $)", min_value=1, value=2500)
saving_rate = st.sidebar.slider("PCE Technology Cost Reduction (%)", 0, 50, 20)

# 5. 수익 계산 로직
total_saving = units * 30000 * (saving_rate / 100)
early_revenue = units * rent * 5  # 5개월 조기 완공 가정

# 6. 메인 결과 화면 출력
st.subheader("Key Investment Results")
col1, col2 = st.columns(2)
with col1:
    st.metric("Total Construction Cost Savings", f"${total_saving:,.0f}")
with col2:
    st.metric("Early Completion Revenue (5 Months)", f"${early_revenue:,.0f}")

st.write("---")

# 7. 상세 분석 표
st.subheader("Detailed Investment Analysis")
analysis_data = {
    "Description": ["Total Project Units", "Construction Cost Savings", "Early Completion Benefit", "Total Project Benefit"],
    "Value": [f"{units} Units", f"${total_saving:,.0f}", f"${early_revenue:,.0f}", f"${(total_saving + early_revenue):,.0f}"]
}
df = pd.DataFrame(analysis_data)
st.table(df)

# 8. 하단 정보
st.info("This analysis is based on PMC USA & Asia PCE Technology MOU.")
st.caption("© 2026 PMC USA Management. All rights reserved.")
