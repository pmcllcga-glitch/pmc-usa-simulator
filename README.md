import streamlit as st
import plotly.graph_objects as go

# --------------------------------------------------
# 1. Page configuration
# --------------------------------------------------
# 페이지 기본 설정
st.set_page_config(
    page_title="Asia PCE Investment Return Simulator",
    layout="wide"
)

# --------------------------------------------------
# 2. Header
# --------------------------------------------------
# 상단 제목 및 설명
st.title("Asia PCE Investment Return Simulator")
st.markdown(
    """
    # PMC USA Investment Simulator
### Powered by Asia PCE Full PC Technology

This simulator provides real-time ROI analysis for multifamily residential projects 
utilizing Asia PCE's advanced Precast Concrete construction methods.
    """
)

# --------------------------------------------------
# 3. Sidebar inputs
# --------------------------------------------------
# 좌측 사이드바 입력 항목
st.sidebar.header("Project Inputs")

land_size = st.sidebar.number_input(
    "Site Area (pyeong)",
    min_value=100,
    value=1000,
    step=100
)

total_units = st.sidebar.number_input(
    "Total Residential Units",
    min_value=1,
    value=100,
    step=1
)

avg_rent = st.sidebar.slider(
    "Estimated Monthly Rent per Unit (USD)",
    min_value=500,
    max_value=5000,
    value=1200,
    step=50
)

st.sidebar.markdown("---")
st.sidebar.header("Construction Assumptions")

wood_cost_per_unit = st.sidebar.number_input(
    "Conventional Wood Construction Cost per Unit (USD)",
    min_value=50000,
    value=150000,
    step=5000
)

pce_cost_reduction_pct = st.sidebar.slider(
    "Asia PCE Cost Reduction vs. Wood (%)",
    min_value=0,
    max_value=50,
    value=20,
    step=1
)

wood_duration = st.sidebar.number_input(
    "Wood Construction Duration (Months)",
    min_value=1,
    value=12,
    step=1
)

pce_duration = st.sidebar.number_input(
    "Asia PCE Construction Duration (Months)",
    min_value=1,
    value=7,
    step=1
)

# --------------------------------------------------
# 4. Validation
# --------------------------------------------------
# 입력값 검증
if total_units <= 0:
    st.error("Total Residential Units must be greater than zero.")
    st.stop()

if pce_duration > wood_duration:
    st.warning(
        "The Asia PCE construction duration is currently set longer than conventional wood construction. "
        "Please confirm whether this assumption is intentional."
    )

# --------------------------------------------------
# 5. Core calculations
# --------------------------------------------------
# 핵심 계산 로직
pce_cost_per_unit = wood_cost_per_unit * (1 - pce_cost_reduction_pct / 100)

total_wood_cost = wood_cost_per_unit * total_units
total_pce_cost = pce_cost_per_unit * total_units
construction_savings = total_wood_cost - total_pce_cost

duration_difference = wood_duration - pce_duration
early_revenue_benefit = total_units * avg_rent * max(duration_difference, 0)

total_financial_advantage = construction_savings + early_revenue_benefit

# 참고용 밀도 계산
land_size_sqft = land_size * 35.5832  # 1평 = 약 35.5832 sqft
site_area_acres = land_size_sqft / 43560 if land_size_sqft > 0 else 0
units_per_acre = total_units / site_area_acres if site_area_acres > 0 else 0

# --------------------------------------------------
# 6. Executive summary metrics
# --------------------------------------------------
# 투자자용 핵심 KPI 표시
st.subheader("Executive Summary")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Construction Cost Savings", f"${construction_savings:,.0f}")
col2.metric("Schedule Acceleration", f"{max(duration_difference, 0)} months")
col3.metric("Early Revenue Benefit", f"${early_revenue_benefit:,.0f}")
col4.metric("Total Financial Advantage", f"${total_financial_advantage:,.0f}")

# --------------------------------------------------
# 7. Project overview section
# --------------------------------------------------
# 프로젝트 개요 정보
st.subheader("Project Overview")

info_col1, info_col2, info_col3 = st.columns(3)
info_col1.info(f"**Site Area:** {land_size:,.0f} pyeong")
info_col2.info(f"**Total Units:** {total_units:,.0f}")
info_col3.info(f"**Estimated Monthly Rent / Unit:** ${avg_rent:,.0f}")

density_col1, density_col2 = st.columns(2)
density_col1.caption(f"Approximate Site Area: {site_area_acres:,.2f} acres")
density_col2.caption(f"Development Density: {units_per_acre:,.2f} units per acre")

# --------------------------------------------------
# 8. Cost comparison chart
# --------------------------------------------------
# 공사비 비교 차트
st.subheader("Construction Cost Comparison")

fig_cost = go.Figure()

fig_cost.add_trace(
    go.Bar(
        name="Conventional Wood",
        x=["Total Project Cost"],
        y=[total_wood_cost],
        text=[f"${total_wood_cost:,.0f}"],
        textposition="outside"
    )
)

fig_cost.add_trace(
    go.Bar(
        name="Asia PCE",
        x=["Total Project Cost"],
        y=[total_pce_cost],
        text=[f"${total_pce_cost:,.0f}"],
        textposition="outside"
    )
)

fig_cost.update_layout(
    barmode="group",
    height=450,
    yaxis_title="USD",
    xaxis_title="Metric",
    legend_title="Construction Method",
    margin=dict(l=20, r=20, t=40, b=20)
)

st.plotly_chart(fig_cost, use_container_width=True)

# --------------------------------------------------
# 9. Schedule comparison chart
# --------------------------------------------------
# 공기 비교 차트
st.subheader("Construction Schedule Comparison")

fig_schedule = go.Figure()

fig_schedule.add_trace(
    go.Bar(
        name="Conventional Wood",
        x=["Construction Duration"],
        y=[wood_duration],
        text=[f"{wood_duration} months"],
        textposition="outside"
    )
)

fig_schedule.add_trace(
    go.Bar(
        name="Asia PCE",
        x=["Construction Duration"],
        y=[pce_duration],
        text=[f"{pce_duration} months"],
        textposition="outside"
    )
)

fig_schedule.update_layout(
    barmode="group",
    height=450,
    yaxis_title="Months",
    xaxis_title="Metric",
    legend_title="Construction Method",
    margin=dict(l=20, r=20, t=40, b=20)
)

st.plotly_chart(fig_schedule, use_container_width=True)

# --------------------------------------------------
# 10. Financial impact breakdown
# --------------------------------------------------
# 상세 재무효과 설명
st.subheader("Financial Impact Breakdown")

st.markdown(
    f"""
    - **Total Cost - Conventional Wood:** ${total_wood_cost:,.0f}  
    - **Total Cost - Asia PCE:** ${total_pce_cost:,.0f}  
    - **Direct Construction Savings:** ${construction_savings:,.0f}  
    - **Schedule Advantage:** {max(duration_difference, 0)} months  
    - **Early Revenue Benefit from Faster Delivery:** ${early_revenue_benefit:,.0f}  
    - **Total Estimated Financial Advantage:** ${total_financial_advantage:,.0f}  
    """
)

# --------------------------------------------------
# 11. Investment conclusion
# --------------------------------------------------
# 투자자 관점 결론 문구
st.subheader("Investment Conclusion")

st.success(
    f"Based on the current assumptions, adopting the Asia PCE system may generate an estimated "
    f"**${total_financial_advantage:,.0f}** in combined cost savings and early revenue benefit "
    f"compared with conventional wood-frame construction."
)

# --------------------------------------------------
# 12. Disclaimer
# --------------------------------------------------
# 면책 및 참고사항
st.caption(
    "Disclaimer: This simulator is intended for preliminary feasibility review only. "
    "Actual project economics may vary depending on structural design, logistics, crane costs, "
    "installation labor, financing terms, permitting conditions, local code requirements, and market demand."
)
