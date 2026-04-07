
import os
from datetime import datetime
from pathlib import Path

import pandas as pd
import plotly.graph_objects as go
import streamlit as st

# Optional Google Sheets support
try:
    import gspread
    from google.oauth2.service_account import Credentials
except Exception:
    gspread = None
    Credentials = None

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
/* =========================================================
   GLOBAL
   ========================================================= */
html, body, [class*="css"] {
    font-family: "Arial", sans-serif;
}
.stApp {
    background-color: #f4f5f7;
    color: #111827;
}

/* Wider page, less side whitespace */
.block-container {
    padding-top: 0rem;
    padding-bottom: 3.5rem;
    max-width: 1640px;
    padding-left: 1.25rem;
    padding-right: 1.25rem;
}

/* =========================================================
   HERO
   ========================================================= */
.hero-wrap {
    background: linear-gradient(135deg, #0f172a 0%, #1a2433 45%, #263a54 100%);
    color: white;
    padding: 68px 56px;
    border-radius: 22px;
    position: relative;
    overflow: hidden;
    margin-top: 16px;
    margin-bottom: 30px;
    border: 1px solid rgba(255,255,255,0.08);
}
.hero-wrap:before {
    content: "";
    position: absolute;
    inset: 0;
    background-image:
        linear-gradient(rgba(255,255,255,0.05) 1px, transparent 1px),
        linear-gradient(90deg, rgba(255,255,255,0.05) 1px, transparent 1px);
    background-size: 40px 40px;
    pointer-events: none;
}
.hero-inner {
    position: relative;
    z-index: 2;
}
.eyebrow {
    text-transform: uppercase;
    letter-spacing: 2.1px;
    font-size: 13px;
    font-weight: 700;
    color: #cbd5e1;
    margin-bottom: 16px;
}
.hero-title {
    font-size: 52px;
    line-height: 1.08;
    font-weight: 800;
    margin-bottom: 18px;
    max-width: 860px;
}
.hero-subtitle {
    font-size: 21px;
    line-height: 1.75;
    color: #edf2f7;
    max-width: 980px;
    margin-bottom: 22px;
}
.hero-note {
    font-size: 17px;
    line-height: 1.85;
    color: #d9e2ec;
    max-width: 1040px;
}

/* =========================================================
   TYPOGRAPHY / SECTIONS
   ========================================================= */
.section-title {
    font-size: 34px;
    font-weight: 800;
    margin-top: 14px;
    margin-bottom: 8px;
    color: #111827;
}
.section-subtitle {
    font-size: 18px;
    line-height: 1.8;
    color: #4b5563;
    margin-bottom: 24px;
    max-width: 1080px;
}
.caption {
    color: #6b7280;
    font-size: 15px;
    margin-top: 10px;
    line-height: 1.7;
}
.spacer-xxs { height: 8px; }
.spacer-xs { height: 16px; }
.spacer-sm { height: 26px; }
.spacer-md { height: 42px; }

/* =========================================================
   CARDS
   ========================================================= */
.info-card {
    background: white;
    border: 1px solid #e5e7eb;
    border-radius: 20px;
    padding: 28px 24px;
    min-height: 210px;
    box-shadow: 0 4px 14px rgba(15, 23, 42, 0.04);
    margin-bottom: 16px;
}
.info-card h4 {
    margin: 0 0 12px 0;
    font-size: 21px;
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
    box-shadow: 0 4px 14px rgba(15, 23, 42, 0.04);
    min-height: 180px;
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
    border-left: 5px solid #1f2937;
    border-radius: 18px;
    padding: 24px 24px;
    margin: 10px 0 24px 0;
    color: #374151;
    line-height: 1.9;
    font-size: 17px;
}

/* =========================================================
   INPUTS / LABELS
   ========================================================= */
label, .stTextInput label, .stNumberInput label, .stDateInput label, .stTextArea label, .stSelectbox label {
    color: #111827 !important;
    font-weight: 700 !important;
    opacity: 1 !important;
}
div[data-testid="stWidgetLabel"] label p {
    color: #111827 !important;
    font-weight: 700 !important;
    opacity: 1 !important;
    font-size: 16px !important;
}
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
    border-radius: 12px !important;
}
div[data-baseweb="select"] > div {
    background-color: #232634 !important;
    border: 1px solid #3b4252 !important;
    border-radius: 12px !important;
    color: #ffffff !important;
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
.stButton > button,
div[data-testid="stFormSubmitButton"] button {
    background: linear-gradient(90deg, #0b1220 0%, #111827 100%);
    color: white !important;
    border-radius: 12px !important;
    border: 1px solid #111827 !important;
    min-height: 52px;
    font-weight: 700;
    font-size: 16px;
}
.stButton > button:hover,
div[data-testid="stFormSubmitButton"] button:hover {
    border: 1px solid #0f172a !important;
    color: white !important;
}

/* Divider helper */
.soft-divider {
    border-top: 1px solid #e5e7eb;
    margin: 8px 0 0 0;
}

/* Images */
img {
    border-radius: 16px;
}
</style>
""", unsafe_allow_html=True)

# =========================================================
# HELPERS
# =========================================================
ASSET_DIR = Path(".")

def asset_exists(name: str) -> bool:
    return Path(name).exists()

def safe_image(path: str, caption: str | None = None, width_container: bool = True):
    if asset_exists(path):
        st.image(path, use_container_width=width_container)
        if caption:
            st.markdown(f'<div class="caption">{caption}</div>', unsafe_allow_html=True)
    else:
        st.warning(f"Missing image: {path}")

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

# =========================================================
# DATA SAVE HELPERS
# =========================================================
CSV_BACKUP_PATH = Path("pmc_feasibility_requests_backup.csv")

def get_gsheet_client():
    if gspread is None or Credentials is None:
        return None
    try:
        if "gcp_service_account" in st.secrets:
            service_account_info = dict(st.secrets["gcp_service_account"])
            scopes = [
                "https://www.googleapis.com/auth/spreadsheets",
                "https://www.googleapis.com/auth/drive",
            ]
            credentials = Credentials.from_service_account_info(
                service_account_info, scopes=scopes
            )
            return gspread.authorize(credentials)
    except Exception:
        return None
    return None

def append_to_google_sheet(record: dict) -> tuple[bool, str]:
    try:
        client = get_gsheet_client()
        if client is None:
            return False, "Google Sheets client not configured"

        sheet_name = None
        worksheet_name = None

        if "google_sheets" in st.secrets:
            sheet_name = st.secrets["google_sheets"].get("spreadsheet_name")
            worksheet_name = st.secrets["google_sheets"].get("worksheet_name", "Sheet1")

        if not sheet_name:
            return False, "Spreadsheet name not found in secrets"

        sh = client.open(sheet_name)
        ws = sh.worksheet(worksheet_name)

        headers = [
            "submitted_at_utc",
            "full_name",
            "company_name",
            "email",
            "project_state",
            "project_type",
            "estimated_unit_count",
            "target_start_date",
            "estimated_budget_usd",
            "project_brief",
        ]

        existing_headers = ws.row_values(1)
        if existing_headers != headers:
            if ws.row_count == 0 or not any(existing_headers):
                ws.append_row(headers)
            elif existing_headers != headers:
                # Keep append compatible even if headers differ
                pass

        ws.append_row([record.get(h, "") for h in headers], value_input_option="USER_ENTERED")
        return True, "Saved to Google Sheets"
    except Exception as e:
        return False, f"Google Sheets save failed: {e}"

def append_to_csv_backup(record: dict) -> tuple[bool, str]:
    try:
        df_new = pd.DataFrame([record])
        if CSV_BACKUP_PATH.exists():
            df_existing = pd.read_csv(CSV_BACKUP_PATH)
            df_all = pd.concat([df_existing, df_new], ignore_index=True)
        else:
            df_all = df_new
        df_all.to_csv(CSV_BACKUP_PATH, index=False)
        return True, f"Saved to local CSV backup: {CSV_BACKUP_PATH.name}"
    except Exception as e:
        return False, f"CSV backup failed: {e}"

# =========================================================
# HERO SECTION
# =========================================================
logo_col, hero_col = st.columns([1.1, 14])
with logo_col:
    if asset_exists("PMC Logo.png"):
        st.image("PMC Logo.png", width=110)

with hero_col:
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
          <strong>PMC is not a general contractor.</strong>
          PMC helps structure project delivery by aligning technical system access, project applicability,
          and localized execution capacity.
        </div>
      </div>
    </div>
    """, unsafe_allow_html=True)

cta1, cta2, _ = st.columns([1.25, 1.25, 5])
with cta1:
    st.button("Request a Feasibility Review", use_container_width=True)
with cta2:
    st.button("Explore the Delivery Model", use_container_width=True)

st.markdown('<div class="spacer-md"></div>', unsafe_allow_html=True)

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
    kpi_card(
        "Delivery Predictability",
        "A more structured pathway for aligning system design, execution sequence, and project coordination."
    )
with k2:
    kpi_card(
        "Capital Efficiency",
        "Supports earlier evaluation of project fit, delivery assumptions, and deployment logic."
    )
with k3:
    kpi_card(
        "Systemized Coordination",
        "Brings technical access, market framing, and execution planning into one platform-led structure."
    )
with k4:
    kpi_card(
        "Scalable Local Execution",
        "Works through qualified U.S. execution partners rather than replacing them."
    )

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
    card(
        "Multifamily",
        "For apartment and rental housing projects where repeatability, schedule discipline, and system-driven coordination matter."
    )
with s2:
    card(
        "Townhome",
        "For projects requiring design consistency, controlled deployment logic, and a more structured path from plan to execution."
    )
with s3:
    card(
        "Workforce Housing",
        "For residential programs prioritizing speed, efficient replication, and scalable local delivery in support-oriented housing environments."
    )

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

# =========================================================
# TECHNOLOGY FOUNDATION
# =========================================================
st.markdown('<div class="section-title">Technology Foundation</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="section-subtitle">PMC’s platform direction is supported by ongoing technical cooperation discussions around Full PC-based construction systems and related implementation support.</div>',
    unsafe_allow_html=True
)

# make image clearly larger
t1, t2 = st.columns([0.85, 1.35])
with t1:
    card(
        "Technical Basis",
        "The platform is being developed around precision-manufactured construction system logic, including technical documentation, engineering support, code coordination, and implementation training frameworks."
    )
    st.markdown(
        '<div class="caption">This section supports technical credibility without positioning PMC as a simple overseas sales agent.</div>',
        unsafe_allow_html=True
    )
with t2:
    safe_image(
        "system_overview.png (2).png",
        "<strong>Illustrative system overview</strong><br>Coordination image showing structured system logic and project-level implementation framing."
    )

st.markdown('<div class="spacer-md"></div>', unsafe_allow_html=True)

# =========================================================
# VISUAL ASSETS
# =========================================================
st.markdown('<div class="section-title">Technical Design & Visual Assets</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="section-subtitle">Visual references are used to support understanding of planning logic, assembly sequence, and residential end-state potential.</div>',
    unsafe_allow_html=True
)

img1, img2 = st.columns([1.05, 1.05])
with img1:
    safe_image(
        "masterplan.png.png",
        "<strong>Master Planning Logic</strong><br>Illustrative planning and layout reference for repeatable residential deployment."
    )
with img2:
    safe_image(
        "community_vibe.png.png",
        "<strong>Residential End-State Visualization</strong><br>Intended lifestyle and community positioning reference."
    )

img3, img4 = st.columns([1.05, 1.05])
with img3:
    safe_image(
        "precast_progression.png.png",
        "<strong>Assembly Sequence</strong><br>Indicative view of how structured deployment may progress."
    )
with img4:
    safe_image(
        "mass_assembly.png.png",
        "<strong>Scalable Deployment</strong><br>Illustrative mass-assembly logic and execution pattern."
    )

st.markdown('<div class="spacer-md"></div>', unsafe_allow_html=True)

# =========================================================
# EXPANDED SYSTEM REFERENCES
# =========================================================
st.markdown('<div class="section-title">Expanded System References</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="section-subtitle">Additional reference visuals highlight modular connection logic, stack stability, integrated product planning, and interior productization pathways.</div>',
    unsafe_allow_html=True
)

ex1, ex2 = st.columns([1.2, 1.2])
with ex1:
    safe_image(
        "withpc_page_9.png",
        "<strong>Modular Connection Reference</strong><br>Illustrative exploded view showing connection logic, load transfer pathways, tolerance coordination, and simplified MEP linkage."
    )
with ex2:
    safe_image(
        "withpc_page_11.png",
        "<strong>Stacking & Load Stability Reference</strong><br>Illustrative example of direct structural load path and stacked module stability."
    )

ex3, ex4 = st.columns([1.2, 1.2])
with ex3:
    safe_image(
        "withpc_page_16.png",
        "<strong>Integrated Product Planning</strong><br>Illustrative unit planning view showing structure, wet zones, interior fit, and productized integration logic."
    )
with ex4:
    safe_image(
        "withpc_page_18.png",
        "<strong>Interior Productization Reference</strong><br>Interior realization image showing how a system can become a higher-value finished housing product."
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
        height=450,
        margin=dict(l=20, r=20, t=54, b=20)
    )
    st.plotly_chart(fig, use_container_width=True)

st.markdown('<div class="spacer-md"></div>', unsafe_allow_html=True)

# =========================================================
# MODEL ASSUMPTIONS & EXCLUSIONS
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
# REQUEST FORM
# =========================================================
st.markdown('<div class="section-title">Request a Feasibility Review</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="section-subtitle">Use this form to start a preliminary discussion regarding project fit, delivery structure, and potential implementation pathways.</div>',
    unsafe_allow_html=True
)

with st.form("feasibility_form"):
    f1, f2 = st.columns([1.15, 1.15])

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
            height=190
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
            "project_brief": project_brief,
        }

        gs_ok, gs_msg = append_to_google_sheet(record)
        csv_ok, csv_msg = append_to_csv_backup(record)

        if gs_ok:
            st.success("Thank you. Your feasibility review request has been recorded in Google Sheets.")
        elif csv_ok:
            st.success("Thank you. Your feasibility review request has been recorded in local backup.")
        else:
            st.warning("Submission captured, but storage may need to be checked.")

        with st.expander("Storage details", expanded=False):
            st.write({"google_sheets": gs_msg, "csv_backup": csv_msg})

        st.write("Submitted data preview:")
        st.dataframe(pd.DataFrame([record]), use_container_width=True)

st.markdown('<div class="spacer-md"></div>', unsafe_allow_html=True)

# =========================================================
# CLOSING SECTION
# =========================================================
st.markdown("""
<div class="hero-wrap" style="padding: 44px 44px; margin-bottom: 10px;">
  <div class="hero-inner">
    <div class="eyebrow">Closing Position</div>
    <div class="hero-title" style="font-size:38px; max-width:980px;">
      Not a conventional contractor pitch. A structured platform for residential delivery.
    </div>
    <div class="hero-subtitle" style="font-size:20px; max-width:1040px;">
      PMC helps developers, partners, and stakeholders evaluate a more organized path to applying
      precision-manufactured residential systems through qualified U.S. execution relationships.
    </div>
  </div>
</div>
""", unsafe_allow_html=True)
