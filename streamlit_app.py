
import streamlit as st
import pandas as pd
import os

# 1. 페이지 설정 (아이콘 제거, 깔끔한 제목)
st.set_page_config(page_title="PMC USA Investment Portal", layout="wide")

# 2. 고품격 커스텀 CSS (아이콘 없이 선과 여백 강조)
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;700;800&display=swap');
    
    html, body, [class*="css"] { font-family: 'Inter', sans-serif; }
    
    /* 전체 배경 */
    .main { background-color: #ffffff; }
    
    /* 상단 Hero 섹션: 딥 네이비 톤 */
    .hero-section {
        background-color: #0f172a;
        padding: 70px 50px;
        border-radius: 4px;
        color: white;
        margin-bottom: 50px;
        border-left: 12px solid #2563eb;
    }
    
    /* 섹션 제목: 직선 스타일 */
    .section-title {
        font-size: 26px !important;
        font-weight: 700;
        color: #1e293b;
        margin-top: 50px;
        margin-bottom: 25px;
        text-transform: uppercase;
        letter-spacing: 2px;
        border-bottom: 2px solid #e2e8f0;
        padding-bottom: 12px;
    }
    
    /* 지표 카드 */
    div[data-testid="stMetric"] {
        background-color: #f8fafc;
        padding: 25px;
        border-radius: 4px;
        border: 1px solid #f1f5f9;
        box-shadow: 0 2px 4px rgba(0,0,0,0.02);
    }
</style>
""", unsafe_allow_html=True)

# --- 섹션 1: Hero 섹션 ---
st.markdown("""
<div class="hero-section">
    <p style="font-size: 12px; text-transform: uppercase; letter-spacing: 5px; color: #3b82f6; margin-bottom: 15px; font-weight: 700;">Exclusive Investment Opportunity</p>
    <h1 style="font-size: 52px; font-weight: 800; margin-bottom: 20px; line-height: 1.1; letter-spacing: -1px;">PMC USA & ASIA PCE</h1>
    <p style="font-size: 18px; font-weight: 300; max-width: 850px; line-height: 1.7; opacity: 0.85;">
        Driving high-efficiency residential development in North America through proprietary Precast Concrete Engineering. 
        Strategic synergy between PMC USA and ASIA PCE sets a new global standard for construction speed and ROI.
    </p>
</div>
""", unsafe_allow_html=True)

# --- 섹션 2: 프로젝트 갤러리 ---
st.markdown('<p class="section-title">Technical Design & Assets</p>', unsafe_allow_html=True)

all_files = os.listdir('.')
image_files = sorted([f for f in all_files if f.startswith('pmc_layout') and f.lower().endswith(('.jpg', '.jpeg', '.png'))])

if image_files:
    cols = st.columns(3)
    for idx, img_name in enumerate(image_files):
        with cols[idx % 3]:
            st.markdown('<div style="margin-bottom: 30px;">', unsafe_allow_html=True)
            st.image(img_name, use_container_width=True)
            st.markdown(f'<p style="font-size: 11px; color: #94a3b8; text-transform: uppercase; margin-top: 8px; letter-spacing: 1px;">Asset ID: {img_name}</p>', unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)
else:
    st.info("Synchronizing data assets...")

# --- 섹션 3: 수익 시뮬레이터 ---
st.markdown('<p class="section-title">ROI Analysis Dashboard</p>', unsafe_allow_html=True)

with st.sidebar:
    st.markdown("<p style='font-size: 16px; font-weight: 700; letter-spacing: 1px; color: #0f172a;'>CONFIGURATION</p>", unsafe_allow_html=True)
    st.markdown("---")
    units = st.number_input("Total Project Units", min_value=1, value=100)
    rent = st.number_input("Average Monthly Rent ($)", min_value=1, value=2500)
    saving_rate = st.slider("PCE Technology Savings (%)", 0, 50, 25)
    st.markdown("---")
    st.markdown("<p style='font-size: 11px; color: #64748b; font-weight: 700;'>STRATEGIC GOVERNANCE</p>", unsafe_allow_html=True)
    st.write("SAMSUNG C&T (EPC)")
    st.write("WITH PC (SYSTEM)")
    st.write("PMC USA (EXECUTION)")

# 계산 로직
total_saving = units * 30000 * (saving_rate / 100)
early_revenue = units * rent * 5
total_benefit = total_saving + early_revenue

# 결과 대시보드
c1, c2, c3 = st.columns(3)
with c1:
    st.metric("Total Cost Savings", f"${total_saving:,.0f}")
with c2:
    st.metric("Early Completion Revenue", f"${early_revenue:,.0f}")
with c3:
    st.metric("Projected Total Value", f"${total_benefit:,.0f}")

st.markdown("<br><br>", unsafe_allow_html=True)

# 상세 데이터 테이블
st.subheader("Financial Impact Performance")
df = pd.DataFrame({
    "Key Performance Indicator": ["Total Units", "Construction Efficiency Savings", "Early Market Entry Benefit", "Estimated Alpha Value"],
    "Financial Figure": [f"{units} Units", f"${total_saving:,.0f}", f"${early_revenue:,.0f}", f"${total_benefit:,.0f}"]
})
st.table(df)

# --- 섹션 4: 푸터 ---
st.markdown("<br><br>---", unsafe_allow_html=True)
st.markdown("""
<div style="text-align: center; color: #94a3b8; padding: 40px 0;">
    <p style="font-size: 11px; letter-spacing: 3px; font-weight: 700;">PMC USA MANAGEMENT | HIGHLY CONFIDENTIAL</p>
    <p style="font-size: 10px; margin-top: 5px; opacity: 0.7;">© 2026 PMC USA. All rights reserved.</p>
</div>
""", unsafe_allow_html=True)
