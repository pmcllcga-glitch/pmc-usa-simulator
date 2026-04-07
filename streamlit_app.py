import streamlit as st
import pandas as pd
from datetime import datetime
import plotly.graph_objects as go

# =========================
# PAGE CONFIG
# =========================
st.set_page_config(
    page_title="PMC | A New Standard for Residential Delivery",
    page_icon="PMC Logo.png",
    layout="wide"
)

# =========================
# CUSTOM CSS
# =========================
st.markdown("""
<style>
/* Global */
html, body, [class*="css"] {
    font-family: "Arial", sans-serif;
}
.stApp {
    background-color: #f5f6f8;
    color: #111827;
}

/* Container width */
.block-container {
    padding-top: 0rem;
    padding-bottom: 3rem;
    max-width: 1250px;
}

/* Top brand banner */
.hero-wrap {
    background: linear-gradient(135deg, #0f172a 0%, #1f2937 50%, #243447 100%);
    color: white;
    padding: 56px 48px;
    border-radius: 20px;
    position: relative;
    overflow: hidden;
    margin-top: 18px;
    margin-bottom: 28px;
    border: 1px solid rgba(255,255,255,0.08);
}

/* subtle blueprint / grid feel */
.hero-wrap:before {
    content: "";
    position: absolute;
    inset: 0;
    background-image:
        linear-gradient(rgba(255,255,255,0.05) 1px, transparent 1px),
        linear-gradient(90deg, rgba(255,255,255,0.05) 1px, transparent 1px);
    background-size: 42px 42px;
    pointer-events: none;
}

.hero-inner {
    position: relative;
    z-index: 2;
}

.eyebrow {
    text-transform: uppercase;
    letter-spacing: 1.8px;
    font-size: 12px;
    font-weight: 700;
    color: #cbd5e1;
    margin-bottom: 14px;
}

.hero-title {
    font-size: 44px;
    line-height: 1.1;
    font-weight: 700;
    margin-bottom: 16px;
    max-width: 760px;
}

.hero-subtitle {
    font-size: 18px;
    line-height: 1.7;
    color: #e5e7eb;
    max-width: 840px;
    margin-bottom: 22px;
}

.hero-note {
    font-size: 15px;
    line-height: 1.7;
    color: #cbd5e1;
    max-width: 860px;
}

.section-title {
    font-size: 28px;
    font-weight: 700;
    margin-top: 14px;
    margin-bottom: 6px;
    color: #111827;
}

.section-subtitle {
    font-size: 16px;
    line-height: 1.7;
    color: #4b5563;
    margin-bottom: 22px;
    max-width: 920px;
}

/* Cards */
.info-card {
    background: white;
    border: 1px solid #e5e7eb;
    border-radius: 18px;
    padding: 24px 22px;
    min-height: 190px;
    box-shadow: 0 2px 10px rgba(0,0,0,0.03);
    margin-bottom: 16px;
}

.info-card h4 {
    margin: 0 0 10px 0;
    font-size: 18px;
    color: #111827;
}

.info-card p {
    margin: 0;
    font-size: 15px;
    line-height: 1.7;
    color: #4b5563;
}

.kpi-card {
    background: white;
    border: 1px solid #e5e7eb;
    border-radius: 18px;
    padding: 22px 20px;
    box-shadow: 0 2px 10px rgba(0,0,0,0.03);
    min-height: 150px;
}

.kpi-title {
    font-size: 16px;
    font-weight: 700;
    color: #111827;
    margin-bottom: 8px;
}

.kpi-text {
    font-size: 14px;
    line-height: 1.7;
    color: #4b5563;
}

/* Callout */
.callout {
    background: #ffffff;
    border: 1px solid #dbe3ea;
    border-left: 5px solid #1f2937;
    border-radius: 16px;
    padding: 22px 22px;
    margin: 8px 0 22px 0;
    color: #374151;
    line-height: 1.75;
}

/* Divider spacing */
.spacer-xxs { height: 8px; }
.spacer-xs { height: 16px; }
.spacer-sm { height: 24px; }
.spacer-md { height: 36px; }

/* Small caption */
.caption {
    color: #6b7280;
    font-size: 13px;
    margin-top: 8px;
    line-height: 1.6;
}
</style>
""", unsafe_allow_html=True)

# =========================
# HELPER
# =========================
def card(title, body):
    st.markdown(
        f"""
        <div class="info-card">
            <h4>{title}</h4>
            <p>{body}</p>
        </div>
        """,
        unsafe_allow_html=True
    )

def kpi_card(title, body):
    st.markdown(
        f"""
        <div class="kpi-card">
            <div class="kpi-title">{title}</div>
            <div class="kpi-text">{body}</div>
        </div>
        """,
        unsafe_allow_html=True
    )

# =========================
# HERO
# =========================
st.markdown("""
<div class="hero-wrap">
  <div class="hero-inner">
    <div class="eyebrow">Engineered for Predictability. Built for Value.</div>
    <div class="hero-title">A New Standard for Residential Delivery.</div>
    <div class="hero-subtitle">
      PMC is a branded delivery platform that connects precision-manufactured construction systems
      with qualified U.S. execution partners.
    </div>
    <div class="hero-note">
      Designed to improve delivery speed, predictability, and capital efficiency across multifamily,
      townhome, workforce housing, and project-specific residential applications.
      <br><br>
      <strong>PMC is not a general contractor.</strong> PMC helps structure project delivery by aligning
      technical system access, project applicability, and localized execution capacity.
    </div>
  </div>
</div>
""", unsafe_allow_html=True)

col_cta1, col_cta2, col_cta3 = st.columns([1.1, 1.1, 4])
with col_cta1:
    st.button("Request a Feasibility Review", use_container_width=True)
with col_cta2:
    st.button("Explore the Delivery Model", use_container_width=True)

st.markdown('<div class="spacer-sm"></div>', unsafe_allow_html=True)

# =========================
# SECTION 1: STRATEGIC VALUE
# =========================
st.markdown('<div class="section-title">Strategic Value</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="section-subtitle">PMC is designed to help developers, execution partners, and stakeholders evaluate a more structured path to residential delivery.</div>',
    unsafe_allow_html=True
)

c1, c2, c3, c4 = st.columns(4)
with c1:
    kpi_card("Delivery Predictability", "A more structured pathway for aligning system design, execution sequence, and project coordination.")
with c2:
    kpi_card("Capital Efficiency", "Supports earlier evaluation of project fit, delivery assumptions, and deployment logic.")
with c3:
    kpi_card("Systemized Coordination", "Brings technical access, market framing, and execution planning into one platform-led structure.")
with c4:
    kpi_card("Scalable Local Execution", "Works through qualified U.S. execution partners rather than replacing them.")

st.markdown('<div class="spacer-md"></div>', unsafe_allow_html=True)

# =========================
# SECTION 2: SOLUTIONS
# =========================
st.markdown('<div class="section-title">Solutions</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="section-subtitle">PMC is focused on residential project types where delivery discipline, repeatability, and structured coordination can create strategic value.</div>',
    unsafe_allow_html=True
)

col1, col2, col3 = st.columns(3)
with col1:
    card(
        "Multifamily",
        "For apartment and rental housing projects where repeatability, schedule discipline, and system-driven coordination matter."
    )
with col2:
    card(
        "Townhome",
        "For projects requiring design consistency, controlled deployment logic, and a more structured path from plan to execution."
    )
with col3:
    card(
        "Workforce Housing",
        "For residential programs prioritizing speed, efficient replication, and scalable local delivery in support-oriented housing environments."
    )

st.markdown('<div class="spacer-md"></div>', unsafe_allow_html=True)

# =========================
# SECTION 3: HOW PMC WORKS
# =========================
st.markdown('<div class="section-title">How PMC Works</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="section-subtitle">PMC is structured as a delivery platform. The goal is not to replace local builders, but to create a more organized framework for applying precision-manufactured residential systems in the U.S. market.</div>',
    unsafe_allow_html=True
)

w1, w2, w3, w4, w5 = st.columns(5)
with w1:
    card("1. System Access", "PMC works to establish access to technical systems and cooperation frameworks that support project-level application.")
with w2:
    card("2. Project Fit Review", "Potential projects are screened for applicability, deployment logic, and alignment with delivery assumptions.")
with w3:
    card("3. Partner Alignment", "Qualified U.S. execution partners are aligned based on project type, location, and implementation needs.")
with w4:
    card("4. Delivery Coordination", "PMC helps frame the pathway between technical intent, project structure, and localized execution.")
with w5:
    card("5. Project-Level Application", "Each project is evaluated as a specific implementation case rather than a one-size-fits-all offering.")

st.markdown("""
<div class="callout">
<strong>Important positioning:</strong><br>
PMC is not presenting itself as a conventional general contractor.
PMC is designed to function as a branded delivery platform that helps connect technical system access
with project-specific execution capacity in the U.S.
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="spacer-md"></div>', unsafe_allow_html=True)

# =========================
# SECTION 4: FOR EXECUTION PARTNERS
# =========================
st.markdown('<div class="section-title">For Execution Partners</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="section-subtitle">PMC is intended to work with local U.S. execution partners, not against them.</div>',
    unsafe_allow_html=True
)

ep1, ep2 = st.columns(2)
with ep1:
    card(
        "What PMC Does",
        "PMC helps structure project opportunities by aligning system access, project framing, technical coordination, and outward-facing delivery logic."
    )
with ep2:
    card(
        "What Local Partners Do",
        "Local partners remain central to permitting interface, site execution, installation sequencing, subcontract management, and field delivery."
    )

st.markdown("""
<div class="callout">
<strong>Execution remains local.</strong><br>
PMC does not seek to replace local builders or field operators.
The platform is designed to support project structuring and coordination while preserving the role of qualified U.S. execution teams.
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="spacer-md"></div>', unsafe_allow_html=True)

# =========================
# SECTION 5: TECHNOLOGY FOUNDATION
# =========================
st.markdown('<div class="section-title">Technology Foundation</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="section-subtitle">PMC’s platform direction is supported by ongoing technical cooperation discussions around Full PC-based construction systems and related implementation support.</div>',
    unsafe_allow_html=True
)

t1, t2 = st.columns([1.2, 1])
with t1:
    card(
        "Technical Basis",
        "The platform is being developed around precision-manufactured construction system logic, including technical documentation, engineering support, code coordination, and implementation training frameworks."
    )
    st.markdown('<div class="caption">This section should support credibility without making PMC look like a simple overseas sales agent.</div>', unsafe_allow_html=True)
with t2:
    st.image("system_overview.png (2).png", use_container_width=True)
    st.markdown('<div class="caption">Illustrative system overview / coordination image</div>', unsafe_allow_html=True)

st.markdown('<div class="spacer-md"></div>', unsafe_allow_html=True)

# =========================
# SECTION 6: VISUAL ASSETS
# =========================
st.markdown('<div class="section-title">Technical Design & Visual Assets</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="section-subtitle">Visual references are used to support understanding of planning logic, assembly sequence, and residential end-state potential.</div>',
    unsafe_allow_html=True
)

img1, img2 = st.columns(2)
with img1:
    st.image("masterplan.png.png", use_container_width=True)
    st.markdown('<div class="caption"><strong>Master Planning Logic</strong><br>Illustrative planning and layout reference for repeatable residential deployment.</div>', unsafe_allow_html=True)

with img2:
    st.image("community_vibe.png.png", use_container_width=True)
    st.markdown('<div class="caption"><strong>Residential End-State Visualization</strong><br>Intended lifestyle and community positioning reference.</div>', unsafe_allow_html=True)

img3, img4 = st.columns(2)
with img3:
    st.image("precast_progression.png.png", use_container_width=True)
    st.markdown('<div class="caption"><strong>Assembly Sequence</strong><br>Indicative view of how structured deployment may progress.</div>', unsafe_allow_html=True)

with img4:
    st.image("mass_assembly.png.png", use_container_width=True)
    st.markdown('<div class="caption"><strong>Scalable Deployment</strong><br>Illustrative mass-assembly logic and execution pattern.</div>', unsafe_allow_html=True)

st.markdown('<div class="spacer-md"></div>', unsafe_allow_html=True)

# =========================
# SECTION 7: ROI SIMULATOR
# =========================
st.markdown('<div class="section-title">ROI Simulator</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="section-subtitle">This tool is intended for preliminary discussion only. It is not a proposal, guarantee, or final underwriting model.</div>',
    unsafe_allow_html=True
)

with st.expander("Open ROI Simulator", expanded=True):
    col_a, col_b, col_c = st.columns(3)
    with col_a:
        units = st.number_input("Estimated Unit Count", min_value=1, value=100, step=1)
        avg_rent = st.number_input("Avg Monthly Rent per Unit ($)", min_value=0, value=1800, step=50)
    with col_b:
        dev_cost = st.number_input("Estimated Development Cost ($)", min_value=0, value=18000000, step=100000)
        occ_rate = st.slider("Occupancy Rate (%)", 0, 100, 92)
    with col_c:
        op_margin = st.slider("Operating Margin (%)", 0, 100, 58)
        hold_years = st.slider("Hold Period (Years)", 1, 20, 5)

    annual_revenue = units * avg_rent * 12 * (occ_rate / 100)
    noi = annual_revenue * (op_margin / 100)
    total_noi = noi * hold_years
    simple_roi = (total_noi - dev_cost) / dev_cost * 100 if dev_cost > 0 else 0

    m1, m2, m3 = st.columns(3)
    m1.metric("Annual Revenue", f"${annual_revenue:,.0f}")
    m2.metric("Annual NOI", f"${noi:,.0f}")
    m3.metric("Simple ROI", f"{simple_roi:.1f}%")

    fig = go.Figure()
    fig.add_trace(go.Bar(x=["Development Cost", "Total NOI Over Hold"], y=[dev_cost, total_noi]))
    fig.update_layout(
        title="Preliminary Value Comparison",
        height=420,
        margin=dict(l=20, r=20, t=50, b=20)
    )
    st.plotly_chart(fig, use_container_width=True)

st.markdown('<div class="spacer-md"></div>', unsafe_allow_html=True)

# =========================
# SECTION 8: ASSUMPTIONS & EXCLUSIONS
# =========================
st.markdown('<div class="section-title">Model Assumptions & Exclusions</div>', unsafe_allow_html=True)
st.markdown("""
<div class="callout">
This website and any embedded calculator or visual content are provided for preliminary planning and discussion purposes only.
Nothing on this site should be interpreted as:
<ul>
<li>a binding construction offer,</li>
<li>a guaranteed project outcome,</li>
<li>final engineering advice,</li>
<li>code approval confirmation, or</li>
<li>an investment solicitation.</li>
</ul>
Project-specific technical review, pricing, execution structure, code analysis, and contractual allocation must be determined separately.
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="spacer-md"></div>', unsafe_allow_html=True)

# =========================
# SECTION 9: REQUEST FORM
# =========================
st.markdown('<div class="section-title">Request a Feasibility Review</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="section-subtitle">Use this form to start a preliminary discussion regarding project fit, delivery structure, and potential implementation pathways.</div>',
    unsafe_allow_html=True
)

with st.form("feasibility_form"):
    col_f1, col_f2 = st.columns(2)

    with col_f1:
        full_name = st.text_input("Full Name")
        company_name = st.text_input("Company Name")
        email = st.text_input("Email Address")
        project_state = st.text_input("Project State")
        project_type = st.selectbox(
            "Project Type",
            ["Multifamily", "Townhome", "Workforce Housing", "Industrial Support Housing", "Other"]
        )

    with col_f2:
        estimated_unit_count = st.number_input("Estimated Unit Count", min_value=0, step=1)
        target_start_date = st.date_input("Target Start Date")
        estimated_budget_usd = st.number_input("Estimated Budget (USD)", min_value=0, step=100000)
        project_brief = st.text_area("Project Brief", height=180)

    submitted = st.form_submit_button("Submit Review Request", use_container_width=True)

    if submitted:
        record = {
            "submitted_at_utc": datetime.utcnow().isoformat(),
            "full_name": full_name,
            "company_name": company_name,
            "email": email,
            "project_state": project_state,
            "project_type": project_type,
            "estimated_unit_count": estimated_unit_count,
            "target_start_date": str(target_start_date),
            "estimated_budget_usd": estimated_budget_usd,
            "project_brief": project_brief
        }

        # 기존 Google Sheets / CSV 저장 로직이 있으면 여기에 그대로 연결
        st.success("Thank you. Your feasibility review request has been recorded.")

        st.write("Submitted data preview:")
        st.dataframe(pd.DataFrame([record]), use_container_width=True)

st.markdown('<div class="spacer-md"></div>', unsafe_allow_html=True)

# =========================
# SECTION 10: CLOSING
# =========================
st.markdown("""
<div class="hero-wrap" style="padding: 40px 42px; margin-bottom: 10px;">
  <div class="hero-inner">
    <div class="eyebrow">Closing Position</div>
    <div class="hero-title" style="font-size:32px; max-width:900px;">
      Not a conventional contractor pitch. A structured platform for residential delivery.
    </div>
    <div class="hero-subtitle" style="font-size:17px; max-width:900px;">
      PMC helps developers, partners, and stakeholders evaluate a more organized path to applying precision-manufactured residential systems through qualified U.S. execution relationships.
    </div>
  </div>
</div>
""", unsafe_allow_html=True)
