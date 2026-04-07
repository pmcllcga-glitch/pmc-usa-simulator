import streamlit as st
import pandas as pd
from datetime import datetime
import plotly.graph_objects as go
import os

# =========================================================
# PAGE CONFIG
# =========================================================
st.set_page_config(
    page_title="PMC | A New Standard for Residential Delivery",
    page_icon="PMC Logo.png",
    layout="wide"
)

# =========================================================
# CUSTOM CSS
# =========================================================
st.markdown("""
<style>
html, body, [class*="css"] {
    font-family: Arial, sans-serif;
}
.stApp {
    background-color: #f5f6f8;
    color: #111827;
}
.block-container {
    padding-top: 0rem;
    padding-bottom: 3rem;
    max-width: 1640px;
    padding-left: 1rem;
    padding-right: 1rem;
}

/* Hero */
.hero-wrap {
    background: linear-gradient(135deg, #09111f 0%, #13233b 45%, #223a5b 100%);
    color: white;
    padding: 62px 56px;
    border-radius: 24px;
    position: relative;
    overflow: hidden;
    margin-top: 10px;
    margin-bottom: 24px;
    border: 1px solid rgba(255,255,255,0.08);
}
.hero-wrap:before {
    content: "";
    position: absolute;
    inset: 0;
    background-image:
        linear-gradient(rgba(255,255,255,0.05) 1px, transparent 1px),
        linear-gradient(90deg, rgba(255,255,255,0.05) 1px, transparent 1px);
    background-size: 46px 46px;
    pointer-events: none;
}
.hero-inner {
    position: relative;
    z-index: 2;
}
.eyebrow {
    text-transform: uppercase;
    letter-spacing: 2px;
    font-size: 13px;
    font-weight: 700;
    color: #dbe5f3;
    margin-bottom: 14px;
}
.hero-title {
    font-size: 60px;
    line-height: 1.06;
    font-weight: 800;
    margin-bottom: 18px;
    max-width: 980px;
}
.hero-subtitle {
    font-size: 22px;
    line-height: 1.7;
    color: #eef4fb;
    max-width: 1120px;
    margin-bottom: 24px;
    font-weight: 500;
}
.hero-note {
    font-size: 18px;
    line-height: 1.85;
    color: #dbe5f3;
    max-width: 1220px;
}

/* Typography */
.section-title {
    font-size: 36px;
    font-weight: 800;
    margin-top: 16px;
    margin-bottom: 8px;
    color: #111827;
}
.section-subtitle {
    font-size: 20px;
    line-height: 1.8;
    color: #4b5563;
    margin-bottom: 24px;
    max-width: 1180px;
}
.caption {
    color: #5f6b7a;
    font-size: 15px;
    margin-top: 10px;
    line-height: 1.7;
}
.spacer-sm { height: 24px; }
.spacer-md { height: 40px; }

/* Cards */
.info-card {
    background: white;
    border: 1px solid #e5e7eb;
    border-radius: 20px;
    padding: 28px 24px;
    min-height: 210px;
    box-shadow: 0 2px 12px rgba(0,0,0,0.03);
    margin-bottom: 16px;
}
.info-card h4 {
    margin: 0 0 12px 0;
    font-size: 22px;
    color: #111827;
}
.info-card p {
    margin: 0;
    font-size: 17px;
    line-height: 1.85;
    color: #4b5563;
}
.kpi-card {
    background: white;
    border: 1px solid #e5e7eb;
    border-radius: 20px;
    padding: 24px 22px;
    box-shadow: 0 2px 12px rgba(0,0,0,0.03);
    min-height: 172px;
}
.kpi-title {
    font-size: 20px;
    font-weight: 800;
    color: #111827;
    margin-bottom: 10px;
}
.kpi-text {
    font-size: 16px;
    line-height: 1.8;
    color: #4b5563;
}
.callout {
    background: #ffffff;
    border: 1px solid #dbe3ea;
    border-left: 6px solid #1f2937;
    border-radius: 18px;
    padding: 24px 24px;
    margin: 10px 0 24px 0;
    color: #374151;
    line-height: 1.9;
    font-size: 17px;
}

/* Labels */
label, .stTextInput label, .stNumberInput label, .stDateInput label, .stTextArea label, .stSelectbox label {
    color: #111827 !important;
    font-weight: 700 !important;
    opacity: 1 !important;
    font-size: 16px !important;
}
div[data-testid="stWidgetLabel"] label p {
    color: #111827 !important;
    font-weight: 700 !important;
    opacity: 1 !important;
    font-size: 16px !important;
}

/* Inputs */
.stTextInput input,
.stNumberInput input,
.stDateInput input,
.stTextArea textarea {
    color: #ffffff !important;
    background-color: #232634 !important;
    border: 1px solid #3b4252 !important;
    font-size: 16px !important;
}
div[data-baseweb="input"] > div,
div[data-baseweb="textarea"] > div {
    background-color: #232634 !important;
    border: 1px solid #3b4252 !important;
    border-radius: 14px !important;
}
div[data-baseweb="select"] > div {
    background-color: #232634 !important;
    border: 1px solid #3b4252 !important;
    border-radius: 14px !important;
    color: #ffffff !important;
    font-size: 16px !important;
}
div[data-baseweb="select"] span {
    color: #ffffff !important;
    font-size: 16px !important;
}
.stTextInput input::placeholder,
.stTextArea textarea::placeholder {
    color: #cbd5e1 !important;
    opacity: 1 !important;
}
.stDateInput input {
    color: #ffffff !important;
}
.stNumberInput button {
    color: #ffffff !important;
}

/* Buttons */
.stButton > button,
div[data-testid="stFormSubmitButton"] button {
    background: linear-gradient(90deg, #09111f 0%, #111827 100%);
    color: white !important;
    border-radius: 14px !important;
    border: 1px solid #111827 !important;
    height: 52px;
    font-weight: 700;
    font-size: 16px;
}
.stButton > button:hover,
div[data-testid="stFormSubmitButton"] button:hover {
    border: 1px solid #0f172a !important;
    color: white !important;
}

img {
    border-radius: 14px;
}
</style>
""", unsafe_allow_html=True)

# =========================================================
# HELPERS
# =========================================================
def card(title: str, body: str):
    st.markdown(
        f"""
        <div class="info-card">
            <h4>{title}</h4>
            <p>{body}</p>
        </div>
        """,
        unsafe_allow_html=True
    )

def kpi_card(title: str, body: str):
    st.markdown(
        f"""
        <div class="kpi-card">
            <div class="kpi-title">{title}</div>
            <div class="kpi-text">{body}</div>
        </div>
        """,
        unsafe_allow_html=True
    )

def safe_image(path, caption=None):
    if os.path.exists(path):
        st.image(path, use_container_width=True)
        if caption:
            st.markdown(f'<div class="caption">{caption}</div>', unsafe_allow_html=True)
    else:
        st.warning(f"Image not found: {path}")

# =========================================================
# HERO
# =========================================================
logo_col, hero_col = st.columns([0.10, 0.90], gap="medium")

with logo_col:
    if os.path.exists("PMC Logo.png"):
        st.image("PMC Logo.png", width=120)

with hero_col:
    st.markdown("""
    <div class="hero-wrap" style="margin-top:0;">
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
          <strong>PMC is not a general contractor.</strong>
          PMC helps structure project delivery by aligning technical system access, project applicability,
          and localized execution capacity.
        </div>
      </div>
    </div>
    """, unsafe_allow_html=True)

cta1, cta2, _ = st.columns([1.3, 1.3, 5])
with cta1:
    st.button("Request a Feasibility Review", use_container_width=True)
with cta2:
    st.button("Explore the Delivery Model", use_container_width=True)

st.markdown('<div class="spacer-sm"></div>', unsafe_allow_html=True)

# =========================================================
# STRATEGIC VALUE
# =========================================================
st.markdown('<div class="section-title">Strategic Value</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="section-subtitle">PMC is designed to help developers, execution partners, and stakeholders evaluate a more structured path to residential delivery.</div>',
    unsafe_allow_html=True
)

k1, k2, k3, k4 = st.columns(4)
with k1:
    kpi_card("Delivery Predictability", "A more structured pathway for aligning system design, execution sequence, and project coordination.")
with k2:
    kpi_card("Capital Efficiency", "Supports earlier evaluation of project fit, delivery assumptions, and deployment logic.")
with k3:
    kpi_card("Systemized Coordination", "Brings technical access, market framing, and execution planning into one platform-led structure.")
with k4:
    kpi_card("Scalable Local Execution", "Works through qualified U.S. execution partners rather than replacing them.")

st.markdown('<div class="spacer-md"></div>', unsafe_allow_html=True)

# =========================================================
# SOLUTIONS
# =========================================================
st.markdown('<div class="section-title">Solutions</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="section-subtitle">PMC is focused on residential project types where delivery discipline, repeatability, and structured coordination can create strategic value.</div>',
    unsafe_allow_html=True
)

s1, s2, s3 = st.columns(3)
with s1:
    card("Multifamily", "For apartment and rental housing projects where repeatability, schedule discipline, and system-driven coordination matter.")
with s2:
    card("Townhome", "For projects requiring design consistency, controlled deployment logic, and a more structured path from plan to execution.")
with s3:
    card("Workforce Housing", "For residential programs prioritizing speed, efficient replication, and scalable local delivery in support-oriented housing environments.")

st.markdown('<div class="spacer-md"></div>', unsafe_allow_html=True)

# =========================================================
# HOW PMC WORKS
# =========================================================
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

# =========================================================
# FOR EXECUTION PARTNERS
# =========================================================
st.markdown('<div class="section-title">For Execution Partners</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="section-subtitle">PMC is intended to work with local U.S. execution partners, not against them.</div>',
    unsafe_allow_html=True
)

ep1, ep2 = st.columns(2)
with ep1:
    card("What PMC Does", "PMC helps structure project opportunities by aligning system access, project framing, technical coordination, and outward-facing delivery logic.")
with ep2:
    card("What Local Partners Do", "Local partners remain central to permitting interface, site execution, installation sequencing, subcontract management, and field delivery.")

st.markdown("""
<div class="callout">
<strong>Execution remains local.</strong><br>
PMC does not seek to replace local builders or field operators.
The platform is designed to support project structuring and coordination while preserving the role of qualified U.S. execution teams.
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="spacer-md"></div>', unsafe_allow_html=True)

# =========================================================
# TECHNOLOGY FOUNDATION
# =========================================================
st.markdown('<div class="section-title">Technology Foundation</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="section-subtitle">PMC’s platform direction is supported by precision-manufactured construction logic, system coordination, modular planning, and productized residential delivery potential.</div>',
    unsafe_allow_html=True
)

t1, t2 = st.columns([0.9, 1.3], gap="large")
with t1:
    card(
        "Technical Basis",
        "The platform is being developed around precision-manufactured construction systems, including technical documentation, engineering support, modular coordination, code alignment, and implementation training frameworks."
    )
    st.markdown(
        '<div class="caption">This section should reinforce credibility without making PMC appear to be a simple overseas sales agent.</div>',
        unsafe_allow_html=True
    )
with t2:
    safe_image(
        "system_overview.png (2).png",
        "<strong>System Overview</strong><br>Illustrative technical coordination reference for system application and delivery logic."
    )

st.markdown('<div class="spacer-md"></div>', unsafe_allow_html=True)

# =========================================================
# ORIGINAL VISUAL ASSETS
# =========================================================
st.markdown('<div class="section-title">Technical Design & Visual Assets</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="section-subtitle">These visuals support planning logic, deployment sequence, and residential end-state positioning.</div>',
    unsafe_allow_html=True
)

img1, img2 = st.columns(2)
with img1:
    safe_image(
        "masterplan.png.png",
        "<strong>Master Planning Logic</strong><br>Illustrative planning and layout reference for repeatable residential deployment."
    )
with img2:
    safe_image(
        "community_vibe.png.png",
        "<strong>Residential End-State Visualization</strong><br>Conceptual view of community positioning and lifestyle outcome."
    )

img3, img4 = st.columns(2)
with img3:
    safe_image(
        "precast_progression.png.png",
        "<strong>Assembly Sequence</strong><br>Indicative visual reference for staged implementation and sequencing."
    )
with img4:
    safe_image(
        "mass_assembly.png.png",
        "<strong>Scalable Deployment</strong><br>Illustrative reference for expanded field deployment and repeatable execution."
    )

st.markdown('<div class="spacer-md"></div>', unsafe_allow_html=True)

# =========================================================
# NEW IMAGE
# =========================================================
st.markdown('<div class="section-title">Precast Modular Construction Showcase</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="section-subtitle">A visual reference illustrating precast modular assembly logic, controlled factory coordination, and scalable system-based residential delivery potential.</div>',
    unsafe_allow_html=True
)

safe_image(
    "Precast modular construction showcase.png",
    "<strong>Precast Modular Construction Showcase</strong><br>Illustrative reference showing precast modular assembly logic, productized unit formation, and factory-based quality control."
)

st.markdown('<div class="spacer-md"></div>', unsafe_allow_html=True)

# =========================================================
# ROI SIMULATOR
# =========================================================
st.markdown('<div class="section-title">ROI Simulator</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="section-subtitle">This tool is intended for preliminary discussion only. It is not a proposal, guarantee, or final underwriting model.</div>',
    unsafe_allow_html=True
)

with st.expander("Open ROI Simulator", expanded=True):
    r1, r2, r3 = st.columns(3)

    with r1:
        units = st.number_input("Estimated Unit Count", min_value=1, value=100, step=1)
        avg_rent = st.number_input("Avg Monthly Rent per Unit ($)", min_value=0, value=1800, step=50)

    with r2:
        dev_cost = st.number_input("Estimated Development Cost ($)", min_value=0, value=18000000, step=100000)
        occ_rate = st.slider("Occupancy Rate (%)", 0, 100, 92)

    with r3:
        op_margin = st.slider("Operating Margin (%)", 0, 100, 58)
        hold_years = st.slider("Hold Period (Years)", 1, 20, 5)

    annual_revenue = units * avg_rent * 12 * (occ_rate / 100)
    noi = annual_revenue * (op_margin / 100)
    total_noi = noi * hold_years
    simple_roi = ((total_noi - dev_cost) / dev_cost * 100) if dev_cost > 0 else 0

    m1, m2, m3 = st.columns(3)
    with m1:
        st.metric("Annual Revenue", f"${annual_revenue:,.0f}")
    with m2:
        st.metric("Annual NOI", f"${noi:,.0f}")
    with m3:
        st.metric("Simple ROI", f"{simple_roi:.1f}%")

    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=["Development Cost", "Total NOI Over Hold"],
        y=[dev_cost, total_noi]
    ))
    fig.update_layout(
        title="Preliminary Value Comparison",
        height=460,
        margin=dict(l=20, r=20, t=50, b=20)
    )
    st.plotly_chart(fig, use_container_width=True)

st.markdown('<div class="spacer-md"></div>', unsafe_allow_html=True)

# =========================================================
# MODEL ASSUMPTIONS
# =========================================================
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

# =========================================================
# FORM
# =========================================================
st.markdown('<div class="section-title">Request a Feasibility Review</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="section-subtitle">Use this form to start a preliminary discussion regarding project fit, delivery structure, and potential implementation pathways.</div>',
    unsafe_allow_html=True
)

with st.form("feasibility_form"):
    f1, f2 = st.columns(2)

    with f1:
        full_name = st.text_input("Full Name", placeholder="Enter your full name")
        company_name = st.text_input("Company Name", placeholder="Enter your company name")
        email = st.text_input("Email Address", placeholder="name@company.com")
        project_state = st.text_input("Project State", placeholder="e.g. Georgia, Texas, Florida")
        project_type = st.selectbox(
            "Project Type",
            ["Multifamily", "Townhome", "Workforce Housing", "Industrial Support Housing", "Other"]
        )

    with f2:
        estimated_unit_count = st.number_input("Estimated Unit Count", min_value=0, step=1)
        target_start_date = st.date_input("Target Start Date")
        estimated_budget_usd = st.number_input("Estimated Budget (USD)", min_value=0, step=100000)
        project_brief = st.text_area(
            "Project Brief",
            placeholder="Briefly describe the project, target use, timeline, and delivery goals.",
            height=180
        )

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

        # 기존 Google Sheets 저장 / CSV 백업 로직 넣는 자리
        st.success("Thank you. Your feasibility review request has been recorded.")
        st.dataframe(pd.DataFrame([record]), use_container_width=True)

st.markdown('<div class="spacer-md"></div>', unsafe_allow_html=True)

# =========================================================
# CLOSING
# =========================================================
st.markdown("""
<div class="hero-wrap" style="padding: 42px 46px; margin-bottom: 10px;">
  <div class="hero-inner">
    <div class="eyebrow">Closing Position</div>
    <div class="hero-title" style="font-size:40px; max-width:1000px;">
      Not a conventional contractor pitch. A structured platform for residential delivery.
    </div>
    <div class="hero-subtitle" style="font-size:22px; max-width:1100px;">
      PMC helps developers, partners, and stakeholders evaluate a more organized path to applying
      precision-manufactured residential systems through qualified U.S. execution relationships.
    </div>
  </div>
</div>
""", unsafe_allow_html=True)
