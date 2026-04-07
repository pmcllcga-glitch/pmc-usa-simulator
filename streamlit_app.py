import streamlit as st
import os
import plotly.graph_objects as go

# --------------------------------------------------
# 1. Page Setup
# --------------------------------------------------
# 페이지 기본 설정
st.set_page_config(
    page_title="PMC USA | Capital Efficiency Tool",
    layout="wide"
)

# --------------------------------------------------
# 2. Custom CSS
# --------------------------------------------------
# 전체 디자인 스타일 정의
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700;800&display=swap');

    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }

    .hero-section {
        background: linear-gradient(135deg, #0f172a 0%, #111827 100%);
        padding: 70px 50px;
        border-radius: 10px;
        color: white;
        margin-bottom: 40px;
        border-left: 8px solid #2563eb;
    }

    .section-title {
        font-size: 24px !important;
        font-weight: 800;
        color: #111827;
        margin: 45px 0 20px 0;
        text-transform: uppercase;
        letter-spacing: 1.5px;
        border-bottom: 2px solid #e5e7eb;
        padding-bottom: 10px;
    }

    .subtle-text {
        color: #6b7280;
        font-size: 15px;
        line-height: 1.7;
    }

    .value-box {
        background: #f8fafc;
        border: 1px solid #e5e7eb;
        border-radius: 8px;
        padding: 22px;
        height: 100%;
    }

    .positioning-box {
        text-align: center;
        padding: 35px 20px;
        color: #6b7280;
        font-style: italic;
        font-size: 16px;
    }

    .small-note {
        color: #6b7280;
        font-size: 13px;
    }
</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# 3. Hero Section
# --------------------------------------------------
# 상단 핵심 소개 섹션
st.markdown("""
<div class="hero-section">
    <p style="font-size: 12px; text-transform: uppercase; letter-spacing: 4px; color: #60a5fa; margin-bottom: 12px; font-weight: 700;">
        Strategic Investment Platform
    </p>
    <h1 style="font-size: 46px; font-weight: 800; margin-bottom: 18px; line-height: 1.1;">
        Build Faster. Deliver Earlier. Capture More Value.
    </h1>
    <p style="font-size: 18px; font-weight: 300; max-width: 920px; line-height: 1.7; opacity: 0.95;">
        Asia PCE delivers faster multifamily development through a precast concrete system
        designed to reduce schedule risk, improve quality control, and accelerate revenue generation.
    </p>
</div>
""", unsafe_allow_html=True)

# --------------------------------------------------
# 4. About Section
# --------------------------------------------------
# 서비스 설명 섹션
st.markdown('<p class="section-title">About Asia PCE</p>', unsafe_allow_html=True)

col_about1, col_about2, col_about3 = st.columns(3)

with col_about1:
    st.markdown("""
    <div class="value-box">
        <h4>Faster Delivery</h4>
        <p class="subtle-text">
            Standardized precast assembly can reduce field complexity and shorten the overall construction timeline.
        </p>
    </div>
    """, unsafe_allow_html=True)

with col_about2:
    st.markdown("""
    <div class="value-box">
        <h4>Greater Predictability</h4>
        <p class="subtle-text">
            A system-based delivery approach improves consistency across manufacturing, installation, and project execution.
        </p>
    </div>
    """, unsafe_allow_html=True)

with col_about3:
    st.markdown("""
    <div class="value-box">
        <h4>Earlier Revenue Capture</h4>
        <p class="subtle-text">
            Faster project delivery may allow earlier occupancy, lease-up, and revenue generation compared with conventional methods.
        </p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("""
<p class="subtle-text">
Asia PCE is designed to work within the existing developer, architect, and general contractor structure.
It is positioned as a precast concrete delivery system for multifamily, townhome, and workforce housing projects
where speed, quality, and capital efficiency matter.
</p>
""", unsafe_allow_html=True)

# --------------------------------------------------
# 5. Visual Assets Section
# --------------------------------------------------
# 이미지 자산 표시 섹션
st.markdown('<p class="section-title">Technical Design & Visual Assets</p>', unsafe_allow_html=True)

# assets 폴더 기준으로 이미지 검색
image_dir = "assets"
image_files = []

if os.path.exists(image_dir):
    image_files = sorted([
        os.path.join(image_dir, f)
        for f in os.listdir(image_dir)
        if f.lower().endswith((".png", ".jpg", ".jpeg", ".webp"))
    ])

if image_files:
    cols = st.columns(3)
    for idx, img in enumerate(image_files[:6]):
        with cols[idx % 3]:
            st.image(img, use_container_width=True)
else:
    st.info("No visual assets found. Add project images to the 'assets' folder to display them here.")

# --------------------------------------------------
# 6. Sidebar Inputs
# --------------------------------------------------
# ROI 계산용 사용자 입력
with st.sidebar:
    st.header("Project Inputs")

    total_units = st.number_input(
        "Total Units",
        min_value=1,
        value=100,
        step=1
    )

    avg_monthly_rent = st.number_input(
        "Average Monthly Rent per Unit (USD)",
        min_value=1,
        value=2500,
        step=100
    )

    baseline_cost_per_unit = st.number_input(
        "Baseline Construction Cost per Unit (USD)",
        min_value=50000,
        value=150000,
        step=5000
    )

    conventional_duration = st.number_input(
        "Conventional Construction Duration (Months)",
        min_value=1,
        value=18,
        step=1
    )

    st.markdown("---")
    st.markdown("### Delivery Structure")
    st.caption("Illustrative delivery model for presentation purposes")
    st.write("- EPC / Delivery Partner")
    st.write("- Asia PCE System Provider")
    st.write("- PMC USA Execution Platform")

# --------------------------------------------------
# 7. Scenario Definitions
# --------------------------------------------------
# 시나리오별 절감률 및 공기단축 설정
scenarios = {
    "Conservative": {"saving_pct": 10, "schedule_gain": 3},
    "Base Case": {"saving_pct": 20, "schedule_gain": 5},
    "Upside Case": {"saving_pct": 30, "schedule_gain": 7}
}

# --------------------------------------------------
# 8. ROI Simulator Section
# --------------------------------------------------
# ROI 시뮬레이터 메인 섹션
st.markdown('<p class="section-title">Scenario-Based ROI Simulator</p>', unsafe_allow_html=True)
st.markdown("""
<p class="subtle-text">
Adjust the project inputs in the sidebar to evaluate the potential financial impact of Asia PCE under
Conservative, Base Case, and Upside assumptions.
</p>
""", unsafe_allow_html=True)

tab1, tab2, tab3 = st.tabs(["Conservative", "Base Case", "Upside Case"])

def render_scenario(name, scenario):
    # 시나리오 계산
    saving_pct = scenario["saving_pct"]
    schedule_gain = scenario["schedule_gain"]

    total_project_cost = total_units * baseline_cost_per_unit
    construction_savings = total_project_cost * (saving_pct / 100)
    early_revenue = total_units * avg_monthly_rent * schedule_gain
    total_advantage = construction_savings + early_revenue

    pce_duration = max(conventional_duration - schedule_gain, 1)

    # KPI 카드 표시
    col1, col2, col3 = st.columns(3)
    col1.metric(
        "Construction Cost Savings",
        f"${construction_savings:,.0f}",
        f"{saving_pct}% vs. baseline"
    )
    col2.metric(
        "Earlier Revenue Capture",
        f"${early_revenue:,.0f}",
        f"{schedule_gain} months faster"
    )
    col3.metric(
        "Total Financial Advantage",
        f"${total_advantage:,.0f}",
        "Illustrative estimate"
    )

    # 요약 문장
    st.markdown(f"""
    **Executive Summary:** Under the **{name}** scenario, Asia PCE may reduce total project cost by
    **${construction_savings:,.0f}**, accelerate delivery by **{schedule_gain} months**, and generate
    approximately **${early_revenue:,.0f}** in earlier revenue capture.
    """)

    # 차트 1: 공사비 비교
    conventional_cost = total_project_cost
    pce_cost = total_project_cost - construction_savings

    fig_cost = go.Figure(data=[
        go.Bar(name="Conventional", x=["Total Construction Cost"], y=[conventional_cost], text=[f"${conventional_cost:,.0f}"], textposition="outside"),
        go.Bar(name="Asia PCE", x=["Total Construction Cost"], y=[pce_cost], text=[f"${pce_cost:,.0f}"], textposition="outside")
    ])
    fig_cost.update_layout(
        barmode="group",
        height=420,
        margin=dict(l=20, r=20, t=30, b=20),
        yaxis_title="USD",
        legend_title="Method"
    )
    st.plotly_chart(fig_cost, use_container_width=True)

    # 차트 2: 공기 비교
    fig_schedule = go.Figure(data=[
        go.Bar(name="Conventional", x=["Construction Duration"], y=[conventional_duration], text=[f"{conventional_duration} mo"], textposition="outside"),
        go.Bar(name="Asia PCE", x=["Construction Duration"], y=[pce_duration], text=[f"{pce_duration} mo"], textposition="outside")
    ])
    fig_schedule.update_layout(
        barmode="group",
        height=420,
        margin=dict(l=20, r=20, t=30, b=20),
        yaxis_title="Months",
        legend_title="Method"
    )
    st.plotly_chart(fig_schedule, use_container_width=True)

with tab1:
    render_scenario("Conservative", scenarios["Conservative"])

with tab2:
    render_scenario("Base Case", scenarios["Base Case"])

with tab3:
    render_scenario("Upside Case", scenarios["Upside Case"])

# --------------------------------------------------
# 9. Assumptions & Exclusions
# --------------------------------------------------
# 계산 가정 및 제외 항목 표시
st.markdown('<p class="section-title">Model Assumptions & Exclusions</p>', unsafe_allow_html=True)

col_ass, col_exc = st.columns(2)

with col_ass:
    with st.expander("View Calculation Assumptions", expanded=True):
        st.write(f"- Baseline construction cost per unit: ${baseline_cost_per_unit:,.0f}")
        st.write(f"- Conventional construction duration: {conventional_duration} months")
        st.write("- Earlier revenue capture is modeled using monthly rent × unit count × schedule gain")
        st.write("- Asia PCE scenarios are presented as illustrative ranges for feasibility discussion")

with col_exc:
    with st.expander("What Is Not Included in This Model", expanded=True):
        st.write("- Land acquisition cost")
        st.write("- Financing and interest carry")
        st.write("- Local permitting and entitlement delays")
        st.write("- Site-specific logistics, crane, and transportation variance")
        st.write("- Tax, insurance, legal, and ownership structure impacts")
        st.write("- Lease-up timing variation after delivery")

st.caption(
    "This tool is intended for preliminary feasibility review only and does not replace full underwriting, engineering, or project-specific cost analysis."
)

# --------------------------------------------------
# 10. Lead Capture Section
# --------------------------------------------------
# 문의 폼 섹션
st.markdown('<p class="section-title">Request a Feasibility Review</p>', unsafe_allow_html=True)

with st.form("contact_form"):
    c1, c2 = st.columns(2)

    with c1:
        full_name = st.text_input("Full Name")
        company_name = st.text_input("Company Name")
        email = st.text_input("Email Address")

    with c2:
        project_state = st.selectbox(
            "Project State",
            ["Louisiana", "Texas", "Florida", "Georgia", "Arizona", "Other"]
        )
        project_type = st.selectbox(
            "Project Type",
            ["Multifamily", "Townhome", "Workforce Housing", "Mixed-Use", "Other"]
        )
        est_units = st.number_input("Estimated Unit Count", min_value=1, value=100, step=1)

    project_brief = st.text_area("Project Brief")

    submitted = st.form_submit_button("Submit Request for Review")

if submitted:
    st.success("Thank you. Your request has been received. A feasibility review representative can follow up based on the information provided.")

# --------------------------------------------------
# 11. Brand Positioning Statement
# --------------------------------------------------
# 하단 브랜드 포지셔닝 문구
st.markdown("---")
st.markdown("""
<div class="positioning-box">
    “Asia PCE does not replace the developer, architect, or GC. We provide a precast concrete delivery system
    that helps existing builders deliver faster and more predictably.”
</div>
""", unsafe_allow_html=True)
