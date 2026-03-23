import streamlit as st
from engine import RuleEngine
from ai import generate_ai_report

st.markdown("""
<style>
    .stButton button {
        background-color: #4CAF50;
        color: white;
        font-size: 16px;
    }
</style>
""", unsafe_allow_html=True)

st.set_page_config(page_title="AI Business Monitor", layout="wide")

st.title("📊 AI Business Health Monitor")

st.markdown("Enter your business data below:")

# --- INPUT SECTION ---
col1, col2, col3 = st.columns(3)

with col1:
    this_week_sales = st.number_input("This Week Sales", value=8000)
    last_week_sales = st.number_input("Last Week Sales", value=10000)
    expenses = st.number_input("Current Expenses", value=5000)

with col2:
    avg_expenses = st.number_input("Average Expenses", value=3500)
    inventory_days = st.number_input("Inventory Days", value=52)
    owner_approvals_pct = st.slider("Owner Approval %", 0, 100, 75)

with col3:
    top_bonus = st.number_input("Top Performer Bonus (%)", value=12)
    avg_bonus = st.number_input("Average Bonus (%)", value=8)
    pct_hitting_target = st.slider("% Hitting Targets", 0, 100, 25)

# --- BUILD DATA OBJECT ---
business_data = {
    "this_week_sales": this_week_sales,
    "last_week_sales": last_week_sales,
    "expenses": expenses,
    "avg_expenses": avg_expenses,
    "inventory_days": inventory_days,
    "owner_approvals_pct": owner_approvals_pct,
    "top_bonus": top_bonus,
    "avg_bonus": avg_bonus,
    "pct_hitting_target": pct_hitting_target
}

# --- RUN ANALYSIS ---
if st.button("Run Analysis 🚀"):

    engine = RuleEngine()
    flags = engine.evaluate(business_data)

    st.subheader("🚨 Detected Issues")

    if not flags:
        st.success("No major issues detected. Business looks healthy.")
    else:
        for f in flags:
            st.error(f"{f['name']} (Severity: {f['severity']})")
            st.caption(f["description"])
            st.json(f["details"])

    # --- AI REPORT ---
    st.subheader("🧠 AI Business Insights")

    with st.spinner("Analyzing business..."):
        report = generate_ai_report(business_data, flags)

    st.markdown("### 📋 Report")
    st.write(report)
