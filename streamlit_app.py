import streamlit as st
import pandas as pd
import os

# 1. 페이지 설정 및 디자인 (Premium Dark & Professional White)
st.set_page_config(page_title="PMC USA | Capital Efficiency Tool", layout="wide")

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;700;800&display=swap');
    html, body, [class*="css"] { font-family: 'Inter', sans-serif; }
    .hero-section {
        background-color: #0f172a; padding: 80px 50px; border-radius: 4px; color: white;
        margin-bottom: 50px; border-left: 12px solid #2563eb;
    }
    .section-title {
        font-size: 26px !important; font-weight: 700; color: #1e293b;
        margin: 50px 0 25px 0; text-transform: uppercase; letter-spacing: 2px;
        border-bottom: 2px solid #e2e8f0; padding-bottom: 12px;
    }
    .scenario-card {
        background-color: #f8fafc; padding: 25px; border-radius: 8px; border: 1px solid #e2e8f0;
    }
</style>
""", unsafe_allow_html=True)

# --- 섹션 1: Hero 섹션 (GPT 제안 반영) ---
st.markdown("""
<div class="hero-section">
    <p style="font-size: 12px; text-transform: uppercase; letter-spacing: 5px; color: #3b82f6; margin-bottom: 15px; font-weight: 700;">Strategic Investment Platform</p>
    <h1 style="font-size: 48px; font-weight: 800; margin-bottom: 25px; line-height: 1.1;">ASIA PCE: Accelerating Capital Efficiency</h1>
    <p style="font-size: 19px; font-weight: 300; max-width: 900px; line-height: 1.7; opacity: 0.9;">
        Asia PCE delivers faster multifamily development through a proprietary precast concrete system 
        designed to <span style="color:#3b82f6; font-weight:700;">reduce schedule risk</span>, 
        improve quality control, and <span style="color:#3b82f6; font-weight:700;">accelerate revenue generation</span>.
    </p>
    <div style="margin-top: 40px; display: flex; gap: 20px;">
        <a href="#roi-simulator" style="text-decoration:none; background:#2563eb; color:white; padding:15px 30px; border-radius:4px; font-weight:700;">Run ROI Simulation</a>
        <a href="#" style="text-decoration:none; border:1px solid white; color:white; padding:15px 30px; border-radius:4px; font-weight:700;">Download Overview</a>
    </div>
</div>
""", unsafe_allow_html=True)

# --- 섹션 2: 시각적 증거 (형님 사진 갤러리) ---
st.markdown('<p class="section-title">Technical Design & Assets</p>', unsafe_allow_html=True)
all_files = os.listdir('.')
image_files = sorted([f for f in all_files if f.startswith('pmc_layout') and f.lower().endswith(('.jpg', '.jpeg', '.png'))])

if image_files:
    cols = st.columns(3)
    for idx, img in enumerate(image_files[:6]):
        with cols[idx % 3]:
            st.image(img, use_container_width=True)
else:
    st.info("Visual assets are synchronizing...")

# --- 섹션 3: ROI 시뮬레이터 (시나리오 기능 추가) ---
st.markdown('<p id="roi-simulator" class="section-title">Scenario-Based ROI Simulator</p>', unsafe_allow_html=True)

with st.sidebar:
    st.markdown("### Base Parameters")
    total_units = st.number_input("Total Units", min_value=1, value=100)
    avg_rent = st.number_input("Avg. Monthly Rent ($)", min_value=1, value=2500)
    st.markdown("---")
    st.markdown("### Strategic Governance")
    st.write("SAMSUNG C&T (EPC)")
    st.write("ASIA PCE (System)")
    st.write("PMC USA (Execution)")

# 시나리오 정의
scenarios = {
    "Conservative": {"saving": 10, "speed": 3},
    "Base Case": {"saving": 20, "speed": 5},
    "Upside Case": {"saving": 35, "speed": 8}
}

tab1, tab2, tab3 = st.tabs(["Conservative", "Base Case", "Upside Case"])

def render_scenario(name, data):
    saving_val = total_units * 30000 * (data['saving'] / 100)
    speed_val = total_units * avg_rent * data['speed']
    total_val = saving_val + speed_val
    
    col_a, col_b, col_c = st.columns(3)
    with col_a:
        st.metric("Construction Cost Savings", f"${saving_val:,.0f}", f"{data['saving']}% Efficiency")
    with col_b:
        st.metric("Earlier Revenue Capture", f"${speed_val:,.0f}", f"{data['speed']} Months Gain")
    with col_c:
        st.metric("Total Financial Advantage", f"${total_val:,.0f}", "Project Alpha")
    
    st.markdown(f"""
    > **Executive Summary:** Under the **{name}**, Asia PCE optimizes the capital stack by reducing 
    hard costs by **${saving_val:,.0f}** and accelerating the stabilization phase by **{data['speed']} months**.
    """)

with tab1: render_scenario("Conservative", scenarios["Conservative"])
with tab2: render_scenario("Base Case", scenarios["Base Case"])
with tab3: render_scenario("Upside Case", scenarios["Upside Case"])

# --- 섹션 4: Assumptions & Exclusions (신뢰도 확보) ---
st.markdown('<p class="section-title">Model Assumptions & Exclusions</p>', unsafe_allow_html=True)
col_ass, col_exc = st.columns(2)

with col_ass:
    with st.expander("View Calculation Assumptions", expanded=True):
        st.write("- Hard Cost Reduction: Calculated on $30k/unit baseline")
        st.write("- Speed Advantage: Compared to traditional stick-build (18 mo)")
        st.write("- Rent Stabilization: Assumes immediate occupancy upon PC completion")

with col_exc:
    with st.expander("What is not included", expanded=True):
        st.write("- Land Acquisition & Financing Costs")
        st.write("- Local Permitting & Entitlement Risks")
        st.write("- Site-specific Crane/Logistics Variances")

# --- 섹션 5: Lead Capture (영업 도구화) ---
st.markdown('<p class="section-title">Request a Feasibility Review</p>', unsafe_allow_html=True)
with st.form("contact_form"):
    c1, c2 = st.columns(2)
    with c1:
        st.text_input("Full Name")
        st.text_input("Company Name")
    with c2:
        st.text_input("Email Address")
        st.selectbox("Project State", ["Louisiana", "Texas", "Florida", "Georgia", "Other"])
    st.text_area("Project Brief (Estimated Unit Count, Site Info)")
    st.form_submit_button("Submit Request for Analysis")

# --- 섹션 6: 브랜드 포지셔닝 문구 ---
st.markdown("---")
st.markdown("""
<div style="text-align: center; padding: 40px; color: #64748b; font-style: italic;">
    "Asia PCE does not replace the developer, architect, or GC. We provide a precast concrete delivery system 
    that helps existing builders deliver faster and more predictably."
</div>
""", unsafe_allow_html=True)
