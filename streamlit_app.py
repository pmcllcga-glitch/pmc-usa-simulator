import streamlit as st
import pandas as pd

# 1. 페이지 설정
st.set_page_config(page_title="PMC USA | Precast Concrete Technology", layout="wide", page_icon="🏢")

# 2. 스타일 설정
st.markdown("""
<style>
    .main-title { font-size: 45px !important; font-weight: 800; color: #1E3A8A; margin-bottom: 10px; }
    .sub-title { font-size: 20px !important; color: #6B7280; margin-bottom: 30px; }
    .section-header { font-size: 28px !important; font-weight: 700; color: #1F2937; margin-top: 40px; margin-bottom: 20px; border-left: 5px solid #2563EB; padding-left: 15px; }
    .stat-card { background-color: #F3F4F6; padding: 20px; border-radius: 10px; text-align: center; border: 1px solid #E5E7EB; }
</style>
""", unsafe_allow_html=True)

st.markdown('<p class="main-title">PMC USA & Asia PCE: Modern Housing Solution</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-title">Innovative Precast Concrete (PCE) System for the US Residential Market</p>', unsafe_allow_html=True)

# 3. 홍보 이미지 갤러리 (형님이 방금 올려주신 실제 파일명 반영)
st.markdown('<p class="section-header">Project Visualization & Execution</p>', unsafe_allow_html=True)

# 형님이 올려주신 실제 파일명들입니다. (오타 하나라도 있으면 안 나옵니다!)
images = [
    "pmc_layout.jpg1.jpg", 
    "pmc_layout.jpg2.jpg", 
    "pmc_layout.jpg3.jpg", 
    "pmc_layout.jpg4.jpg", 
    "pmc_layout.jpg5.jpg", 
    "pmc_layout.jpg6.jpg"
]

# 3열로 사진 배치
cols = st.columns(3)
for idx, img_name in enumerate(images):
    with cols[idx % 3]:
        try:
            # 캡션(설명)은 형님 자료 내용에 맞춰서 넣었습니다.
            captions = [
                "Modern Multifamily Design", 
                "Precise Structural Engineering", 
                "Efficient Site Assembly", 
                "Quality Interior Finish", 
                "Advanced Foundation System", 
                "PCE Technical Standard"
            ]
            st.image(img_name, use_container_width=True, caption=captions[idx])
        except:
            st.warning(f"'{img_name}' 파일을 찾을 수 없습니다.")

st.markdown("---")

# 4. 시장 분석 (보고서 데이터 활용)
st.markdown('<p class="section-header">Market Opportunity</p>', unsafe_allow_html=True)
c1, c2, c3 = st.columns(3)
with c1:
    st.markdown('<div class="stat-card"><h3>3.8M Units</h3><p>US Housing Deficit</p></div>', unsafe_allow_html=True)
with c2:
    st.markdown('<div class="stat-card"><h3>400K Workers</h3><p>Labor Shortage</p></div>', unsafe_allow_html=True)
with c3:
    st.markdown('<div class="stat-card"><h3>5 Months</h3><p>Faster Time-to-Market</p></div>', unsafe_allow_html=True)

# 5. 수익성 시뮬레이터 (사이드바 입력값 사용)
st.markdown('<p class="section-header">Investment ROI Simulator</p>', unsafe_allow_html=True)

with st.sidebar:
    st.header("Project Parameters")
    units = st.number_input("Total Units (총 가구 수)", min_value=1, value=100)
    rent = st.number_input("Monthly Rent ($)", min_value=1, value=2500)
    saving_rate = st.slider("PCE Tech Savings (%)", 0, 50, 20)

total_saving = units * 30000 * (saving_rate / 100)
early_revenue = units * rent * 5

col_a, col_b = st.columns(2)
with col_a:
    st.metric("Estimated Cost Savings", f"${total_saving:,.0f}")
with col_b:
    st.metric("Early Completion Benefit", f"${early_revenue:,.0f}")

# 6. 파트너십 정보 (듀얼 트랙 전략 반영)
st.write("---")
st.info("Global Governance: SAMSUNG C&T (EPC) | System: WITH PC | Execution: PMC USA")
st.caption("© 2026 PMC USA Management. All rights reserved.")
