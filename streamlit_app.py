import os
import csv
from datetime import datetime

import streamlit as st
import plotly.graph_objects as go

# --------------------------------------------------
# 1. Page Setup
# --------------------------------------------------
st.set_page_config(
    page_title="PMC USA | Capital Efficiency Tool",
    layout="wide"
)

# --------------------------------------------------
# 2. File Paths
# --------------------------------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

logo_path = os.path.join(BASE_DIR, "PMC Logo.png")
community_img = os.path.join(BASE_DIR, "community_vibe.png.png")
masterplan_img = os.path.join(BASE_DIR, "masterplan.png.png")
system_img = os.path.join(BASE_DIR, "system_overview.png (2).png")
precast_img = os.path.join(BASE_DIR, "precast_progression.png.png")
assembly_img = os.path.join(BASE_DIR, "mass_assembly.png.png")

csv_path = os.path.join(BASE_DIR, "submissions.csv")

# --------------------------------------------------
# 3. CSV Save Function
# --------------------------------------------------
def save_submission_to_csv(data: dict, file_path: str) -> None:
    file_exists = os.path.exists(file_path)

    fieldnames = [
        "submitted_at_utc",
        "full_name",
        "company_name",
        "email",
        "project_state",
        "project_type",
        "estimated_unit_count",
        "project_brief",
    ]

    with open(file_path, mode="a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)

        if not file_exists:
            writer.writeheader()

        writer.writerow(data)

# --------------------------------------------------
# 4. Custom CSS
# --------------------------------------------------
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');

    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }

    .stApp {
        background: #020817;
        color: #e5e7eb;
    }

    section[data-testid="stSidebar"] {
        background: #071426;
    }

    .hero-box {
        background: linear-gradient(135deg, #071426 0%, #0a1730 100%);
        padding: 54px 52px;
        border-radius: 14px;
        border-left: 6px solid #2563eb;
        margin-top: 10px;
        margin-bottom: 20px;
    }

    .hero-eyebrow {
        font-size: 11px;
        text-transform: uppercase;
        letter-spacing: 4px;
        color: #60a5fa;
        margin-bottom: 18px;
        font-weight: 700;
    }

    .hero-title {
        font-size: 34px;
        font-weight: 800;
        line-height: 1.15;
        margin-bottom: 16px;
        color: #f8fafc;
    }

    .hero-copy {
        font-size: 17px;
        line-height: 1.8;
        color: rgba(255,255,255,0.82);
        max-width: 900px;
        font-weight: 400;
    }

    .kpi-card {
        background: rgba(255,255,255,0.04);
        border: 1px solid rgba(255,255,255,0.08);
        border-radius: 12px;
        padding: 18px 20px;
        min-height: 155px;
    }

    .kpi-label {
        font-size: 12px;
        text-transform: uppercase;
        letter-spacing: 1.5px;
        color: #93c5fd;
        margin-bottom: 8px;
        font-weight: 600;
    }

    .kpi-value {
        font-size: 28px;
        font-weight: 800;
        color: #f8fafc;
        line-height: 1.1;
        margin-bottom: 6px;
    }

    .kpi-sub {
        font-size: 13px;
        color: rgba(255,255,255,0.72);
        line-height: 1.5;
    }

    .section-title {
        font-size: 18px !important;
        font-weight: 700;
        color: #e5e7eb;
        margin: 42px 0 16px 0;
        text-transform: uppercase;
        letter-spacing: 1.5px;
        border-bottom: 1px solid rgba(255,255,255,0.08);
        padding-bottom: 10px;
    }

    .subtle-text {
        color: #94a3b8;
        font-size: 15px;
        line-height: 1.8;
    }

    .value-box {
        background: rgba(255,255,255,0.03);
        border: 1px solid rgba(255,255,255,0.08);
        border-radius: 12px;
        padding: 22px;
        height: 100%;
    }

    .value-box h4 {
        color: #f8fafc;
        margin-bottom: 10px;
        font-size: 18px;
    }

    .image-caption {
        color: #94a3b8;
        font-size: 13px;
        margin-top: 6px;
        margin-bottom: 22px;
    }

    .positioning-box {
        text-align: center;
        padding: 30px 20px;
        color: #94a3b8;
        font-style: italic;
        font-size: 15px;
    }
</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# 5. Hero Section
# --------------------------------------------------
st.markdown('<div class="hero-box">', unsafe_allow_html=True)

if os.path.exists(logo_path):
    st.image(logo_path, width=110)

st.markdown('<div class="hero-eyebrow">Strategic Investment Platform</div>', unsafe_allow_html=True)
st.markdown('<div class="hero-title">Build Faster. Deliver Earlier. Capture More Value.</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="hero-copy">'
    'Asia PCE is a precast concrete delivery system designed for multifamily development '
    'with stronger schedule control, greater predictability, and earlier revenue potential.'
    '</div>',
    unsafe_allow_html=True
)

st.markdown('</div>', unsafe_allow_html=True)

k1, k2, k3 = st.columns(3)

with k1:
    st.markdown("""
    <div class="kpi-card">
        <div class="kpi-label">Cost Efficiency</div>
        <div class="kpi-value">Up to 30%</div>
        <div class="kpi-sub">Potential reduction in total construction cost under upside scenario assumptions.</div>
    </div>
    """, unsafe_allow_html=True)

with k2:
    st.markdown("""
    <div class="kpi-card">
        <div class="kpi-label">Delivery Speed</div>
        <div class="kpi-value">Up to 7 Months</div>
        <div class="kpi-sub">Illustrative schedule acceleration compared with conventional delivery methods.</div>
    </div>
    """, unsafe_allow_html=True)

with k3:
    st.markdown("""
    <div class="kpi-card">
        <div class="kpi-label">Revenue Timing</div>
        <div class="kpi-value">Earlier Occupancy</div>
        <div class="kpi-sub">Faster completion may support earlier lease-up and revenue capture.</div>
    </div>
    """, unsafe_allow_html=True)

st.caption("Use the scenario-based ROI simulator below to test project economics.")

# --------------------------------------------------
# 6. About Section
# --------------------------------------------------
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
            A system-based delivery approach improves consistency across manufacturing, installation, and execution.
        </p>
    </div>
    """, unsafe_allow_html=True)

with col_about3:
    st.markdown("""
    <div class="value-box">
        <h4>Earlier Revenue Capture</h4>
        <p class="subtle-text">
            Faster delivery may enable earlier occupancy, lease-up, and revenue generation compared with conventional methods.
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
# 7. Visual Assets Section
# --------------------------------------------------
st.markdown('<p class="section-title">Technical Design & Visual Assets</p>', unsafe_allow_html=True)

with st.expander("Image Debug Check", expanded=False):
    st.write("Logo exists:", os.path.exists(logo_path))
    st.write("Community exists:", os.path.exists(community_img))
    st.write("Masterplan exists:", os.path.exists(masterplan_img))
    st.write("System exists:", os.path.exists(system_img))
    st.write("Precast exists:", os.path.exists(precast_img))
    st.write("Assembly exists:", os.path.exists(assembly_img))

if os.path.exists(community_img):
    st.image(community_img, use_container_width=True)
    st.markdown('<div class="image-caption">Community Lifestyle Rendering</div>', unsafe_allow_html=True)
else:
    st.warning("Community image not found.")

st.markdown("### Development Vision")
col1, col2 = st.columns(2)

with col1:
    if os.path.exists(masterplan_img):
        st.image(masterplan_img, use_container_width=True)
        st.markdown('<div class="image-caption">200-Unit Master Plan Overview</div>', unsafe_allow_html=True)
    else:
        st.warning("Master plan image not found.")

with col2:
    if os.path.exists(system_img):
        st.image(system_img, use_container_width=True)
        st.markdown('<div class="image-caption">System Overview: Foundation, Exterior, Interior, Final Delivery</div>', unsafe_allow_html=True)
    else:
        st.warning("System overview image not found.")

st.markdown("### Construction Execution")
col3, col4 = st.columns(2)

with col3:
    if os.path.exists(precast_img):
        st.image(precast_img, use_container_width=True)
        st.markdown('<div class="image-caption">Precast Structural Progression</div>', unsafe_allow_html=True)
    else:
        st.warning("Precast progression image not found.")

with col4:
    if os.path.exists(assembly_img):
        st.image(assembly_img, use_container_width=True)
        st.markdown('<div class="image-caption">Mass Assembly Capability</div>', unsafe_allow_html=True)
    else:
        st.warning("Mass assembly image not found.")

# --------------------------------------------------
# 8. Sidebar Inputs
# --------------------------------------------------
with st.sidebar:
    st.header("Project Inputs")

    total_units = st.number_input("Total Units", min_value=1, value=100, step=1)
    avg_monthly_rent = st.number_input("Average Monthly Rent per Unit (USD)", min_value=1, value=2500, step=100)
    baseline_cost_per_unit = st.number_input("Baseline Construction Cost per Unit (USD)", min_value=50000, value=150000, step=5000)
    conventional_duration = st.number_input("Conventional Construction Duration (Months)", min_value=1, value=18, step=1)

    st.markdown("---")
    st.markdown("### Delivery Structure")
    st.caption("Illustrative delivery model for presentation purposes")
    st.write("- EPC / Delivery Partner")
    st.write("- Asia PCE System Provider")
    st.write("- PMC USA Execution Platform")

# --------------------------------------------------
# 9. Scenario Definitions
# --------------------------------------------------
scenarios = {
    "Conservative": {"saving_pct": 10, "schedule_gain": 3},
    "Base Case": {"saving_pct": 20, "schedule_gain": 5},
    "Upside Case": {"saving_pct": 30, "schedule_gain": 7}
}

# --------------------------------------------------
# 10. ROI Simulator
# --------------------------------------------------
st.markdown('<p class="section-title">Scenario-Based ROI Simulator</p>', unsafe_allow_html=True)
st.markdown("""
<p class="subtle-text">
Adjust the project inputs in the sidebar to evaluate the potential financial impact of Asia PCE under
Conservative, Base Case, and Upside assumptions.
</p>
""", unsafe_allow_html=True)

tab1, tab2, tab3 = st.tabs(["Conservative", "Base Case", "Upside Case"])

def render_scenario(name, scenario):
    saving_pct = scenario["saving_pct"]
    schedule_gain = scenario["schedule_gain"]

    total_project_cost = total_units * baseline_cost_per_unit
    construction_savings = total_project_cost * (saving_pct / 100)
    early_revenue = total_units * avg_monthly_rent * schedule_gain
    total_advantage = construction_savings + early_revenue

    pce_duration = max(conventional_duration - schedule_gain, 1)
    pce_cost = total_project_cost - construction_savings

    col_a, col_b, col_c = st.columns(3)
    with col_a:
        st.metric("Construction Cost Savings", f"${construction_savings:,.0f}", f"{saving_pct}% vs. baseline")
    with col_b:
        st.metric("Earlier Revenue Capture", f"${early_revenue:,.0f}", f"{schedule_gain} months faster")
    with col_c:
        st.metric("Total Financial Advantage", f"${total_advantage:,.0f}", "Illustrative estimate")

    st.markdown(
        f"""
        **Executive Summary:** Under the **{name}** scenario, Asia PCE may reduce total project cost by
        **${construction_savings:,.0f}**, accelerate delivery by **{schedule_gain} months**, and generate
        approximately **${early_revenue:,.0f}** in earlier revenue capture.
        """
    )

    fig_cost = go.Figure(data=[
        go.Bar(
            name="Conventional",
            x=["Total Construction Cost"],
            y=[total_project_cost],
            text=[f"${total_project_cost:,.0f}"],
            textposition="outside"
        ),
        go.Bar(
            name="Asia PCE",
            x=["Total Construction Cost"],
            y=[pce_cost],
            text=[f"${pce_cost:,.0f}"],
            textposition="outside"
        )
    ])
    fig_cost.update_layout(
        barmode="group",
        height=380,
        margin=dict(l=20, r=20, t=30, b=20),
        yaxis_title="USD",
        legend_title="Method",
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(255,255,255,0.02)",
        font=dict(color="#e5e7eb")
    )
    st.plotly_chart(fig_cost, use_container_width=True)

    fig_schedule = go.Figure(data=[
        go.Bar(
            name="Conventional",
            x=["Construction Duration"],
            y=[conventional_duration],
            text=[f"{conventional_duration} mo"],
            textposition="outside"
        ),
        go.Bar(
            name="Asia PCE",
            x=["Construction Duration"],
            y=[pce_duration],
            text=[f"{pce_duration} mo"],
            textposition="outside"
        )
    ])
    fig_schedule.update_layout(
        barmode="group",
        height=380,
        margin=dict(l=20, r=20, t=30, b=20),
        yaxis_title="Months",
        legend_title="Method",
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(255,255,255,0.02)",
        font=dict(color="#e5e7eb")
    )
    st.plotly_chart(fig_schedule, use_container_width=True)

with tab1:
    render_scenario("Conservative", scenarios["Conservative"])
with tab2:
    render_scenario("Base Case", scenarios["Base Case"])
with tab3:
    render_scenario("Upside Case", scenarios["Upside Case"])

# --------------------------------------------------
# 11. Assumptions & Exclusions
# --------------------------------------------------
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
# 12. Lead Capture + CSV Save
# --------------------------------------------------
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
    if not full_name.strip() or not email.strip():
        st.error("Please provide at least Full Name and Email Address.")
    else:
        submission_data = {
            "submitted_at_utc": datetime.utcnow().isoformat(),
            "full_name": full_name.strip(),
            "company_name": company_name.strip(),
            "email": email.strip(),
            "project_state": project_state,
            "project_type": project_type,
            "estimated_unit_count": est_units,
            "project_brief": project_brief.strip(),
        }

        try:
            save_submission_to_csv(submission_data, csv_path)
            st.success("Thank you. Your request has been received and saved successfully.")
        except Exception as e:
            st.error(f"Submission could not be saved: {e}")

# --------------------------------------------------
# 13. Admin Preview
# --------------------------------------------------
with st.expander("Admin Preview: Saved Submissions", expanded=False):
    if os.path.exists(csv_path):
        try:
            with open(csv_path, "r", encoding="utf-8") as f:
                st.code(f.read())
        except Exception as e:
            st.error(f"Could not read saved submissions: {e}")
    else:
        st.caption("No submissions saved yet.")

# --------------------------------------------------
# 14. Brand Positioning
# --------------------------------------------------
st.markdown("---")
st.markdown("""
<div class="positioning-box">
    “Asia PCE does not replace the developer, architect, or GC. We provide a precast concrete delivery system
    that helps existing builders deliver faster and more predictably.”
</div>
""", unsafe_allow_html=True)
