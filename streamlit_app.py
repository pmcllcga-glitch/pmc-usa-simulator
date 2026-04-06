import streamlit as st
import pandas as pd

# 1. 페이지 설정
st.set_page_config(page_title="PMC USA | Precast Concrete Technology", layout="wide", page_icon="🏢")

# 2. 메인 제목 및 스타일
st.markdown("""
<style>
    .main-title { font-size: 45px !important; font-weight: 800; color: #1E3A8A; margin-bottom: 0px; }
    .sub-title { font-size: 20px !important; color: #6B7280; margin-bottom: 30px; }
    .section-header { font-size: 28px !important; font-weight: 700; color: #1F2937; margin-top: 40px; margin-bottom: 20px; border-left: 5px solid #2563EB; padding-left: 15px; }
    .stat-card { background-color: #F3F4F6; padding: 20px; border-radius: 10px; text-align: center; border: 1px solid #E5E7EB; }
</style>
""", unsafe_allow_html=True)

st.markdown('<p class="main-title">PMC USA & Asia PCE: Modern Housing Solution</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-title">Innovative Precast Concrete (PCE) System for the US Residential Market</p>', unsafe_allow_html=True)

# 3. 홍보 이미지 갤러리 (형님이 올리신 사진들)
st.markdown('<p class="section-header">Project Visualization & Execution</p>', unsafe_allow_html=True)

# 사진 파일 리스트 (형님이 올린 파일명과 정확히 일치해야 함)
images = [
    "pmc_layout.jpg1.jpg", 
    "pmc_layout.jpg2.jpg", 
    "pmc_layout.jpg3.jpg", 
    "pmc_layout.jpg4.jpg", 
    "pmc_layout.jpg5.jpg", 
    "pmc_layout.jpg6.jpg"
]

# 갤러리 형태로 배치 (3열)
cols = st.columns(3)
for idx, img in enumerate(images):
    with cols[idx % 3]:
        try:
            st.image(img, use_container_width=True, caption=f"PCE Technical Detail {idx+1}")
        except:
            st.caption(f"Image {idx+1} (Pending Upload)")

st.markdown("---")

# 4. 사업의 당위성 (보고서 내용 요약)
st.markdown('<p class="section-header">Why PMC PCE System?</p>', unsafe_allow_html=True)
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown('<div class="stat-card"><h3>3.8M Units</h3><p>US Housing Deficit</p></div>', unsafe_allow_html=True)
with col2:
    st.markdown('<div class="stat-card"><h3>400K Workers</h3><p>Labor Shortage Gap</p></div>', unsafe_allow_html=True)
with col3:
    st.markdown('<div class="stat-card"><h3>5 Months</h3><p>Faster Completion</p></div>', unsafe_allow_html=True)

st.markdown("---")

# 5. 수익성 시뮬레이터 (형님의 핵심 무기)
st.markdown('<p class="section-header">Investment ROI Simulator</p>', unsafe_allow_html=True)

with st.sidebar:
    st.header("Project Parameters")
    units = st.number_input("Total Units (가구 수)", min_value=1, value=100)
    rent = st.number_input("Monthly Rent ($/mo)", min_value=1, value=2500)
    saving_rate = st.slider("Cost Reduction Rate (%)", 0, 50, 20)

# 계산 로직
total_saving = units * 30000 * (saving_rate / 100)
early_revenue = units * rent * 5  # 5개월 조기 완공 수익

c1, c2 = st.columns(2)
with c1:
    st.metric("Estimated Cost Savings", f"${total_saving:,.0f}")
with c2:
    st.metric("Early Completion Revenue", f"${early_revenue:,.0f}")

# 6. 상세 분석 테이블
st.subheader("Analysis Summary")
df = pd.DataFrame({
    "Category": ["Construction Units", "PCE Savings", "Time-to-Market Benefit", "Total Investor Value"],
    "Value": [f"{units} Units", f"${total_saving:,.0f}", f"${early_revenue:,.0f}", f"${(total_saving + early_revenue):,.0f}"]
})
st.table(df)

# 7. 푸터
st.markdown("---")
st.info("Strategy: Samsung C&T (EPC Governance) | WITH PC (System) | PMC USA (Execution)")
st.caption("© 2026 PMC USA Management. All rights reserved.")
