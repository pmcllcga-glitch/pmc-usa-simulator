import streamlit as st
import pandas as pd
import os

# 1. 페이지 설정 및 테마 최적화
st.set_page_config(page_title="PMC USA | Strategic Investment Portal", layout="wide")

# 2. 고품격 커스텀 CSS (아이콘 없이 선과 여백으로 디자인)
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;700;800&display=swap');
    
    html, body, [class*="css"] { font-family: 'Inter', sans-serif; }
    
    /* 배경 및 컨테이너 */
    .main { background-color: #ffffff; }
    
    /* 상단 Hero 섹션: 묵직한 네이비 톤 */
    .hero-section {
        background-color: #0f172a;
        padding: 80px 50px;
        border-radius: 4px;
        color: white;
        margin-bottom: 60px;
        border-left: 10px solid #3b82f6;
    }
    
    /* 섹션 제목: 아이콘 없이 깔끔한 직선 스타일 */
    .section-title {
        font-size: 28px !important;
        font-weight: 700;
        color: #1e293b;
        margin-top: 60px;
        margin-bottom: 30px;
        text-transform: uppercase;
        letter-spacing: 1px;
        border-bottom: 1px solid #e2e8f0;
        padding-bottom: 15px;
    }
    
    /* 카드 및 메트릭 스타일 */
    div[data-testid="stMetric"] {
        background-color: #f8fafc;
        padding: 30px;
        border-radius: 8px;
        border: 1px solid #f1f5f9;
    }
    
    /* 강조 텍스트 */
    .highlight-blue { color: #3b82f6; font-weight: 700; }
</style>
""", unsafe_allow_html=True)

# --- 섹션 1: Hero 섹션 (회사 소개) ---
st.markdown("""
<div class="hero-section">
    <p style="font-size: 13px; text-transform: uppercase; letter-spacing: 4px; color: #3b82f6; margin-bottom: 15px; font-weight: 700;">Investment Opportunity</p>
    <h1 style="font-size: 48px; font-weight: 800; margin-bottom: 25px; line-height: 1.1;">PMC USA & ASIA PCE</h1>
    <p style="font-size: 19px; font-weight: 300; max-width: 800px; line-height: 1.6; opacity: 0.9;">
        A strategic partnership delivering next-generation Precast Concrete solutions to the North American residential market. 
        Optimizing construction speed, cost efficiency, and structural integrity.
    </p>
</div>
""", unsafe_allow_html=True)

# --- 섹션 2: 프로젝트 갤러리 ---
st.markdown('<p class="section-title">Visual Evidence & Technical Design</p>', unsafe_allow_html=True)

all_files = os.listdir('.')
image_files = sorted([f for f in all_files if f.startswith('pmc_layout') and f.lower().endswith(('.jpg', '.jpeg', '.png'))])

if image_files:
    cols = st.columns(3)
    for idx, img_name in enumerate(image_files):
        with cols[idx % 3]:
            st.markdown('<div style="margin-bottom: 30px;">', unsafe_allow_html=True)
            st.image(img_name, use_container_width=True)
            # 캡션도 아이콘 없이 아주 작고 깔끔하게
            st.markdown(f'<p style="font-size: 12px; color: #94a3b8; text-transform: uppercase; margin-top: 10px;">Project Data Ref: {img_name}</p>', unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)
else:
    st.info("System is synchronizing project assets...")

# --- 섹션 3: 수익 시뮬레이터 ---
st.markdown('<p class="section-title">Financial Impact Analysis</p>', unsafe_allow_html=True)

with st.sidebar:
    st.markdown("<h3 style='font-size: 18px; letter-spacing: 1px;'>INPUT PARAMETERS</h3>", unsafe_allow_html=True)
    st.markdown("---")
    units = st.number_input("Total Project Units", min_value
