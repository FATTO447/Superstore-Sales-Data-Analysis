import streamlit as st

st.set_page_config(page_title="Strategic Insights", layout="wide")

st.title("💡 Strategic Insights & Decision Support")
st.markdown("""
**🎯 Data-Driven Decision Framework (Executive Summary):**
This dashboard translates complex data patterns into actionable business strategies for upper management. By connecting shipping logistics, customer segments, and product profitability, these insights aim to eliminate revenue leakage and optimize future margins.
""")

st.divider()

# ─── SECTION 1: SHIP MODE & SEGMENT ───
st.header("1️⃣ Logistics & Customer Segment Optimization")

col1, col2 = st.columns([1, 1])

with col1:
    st.info("### 🔍 Key Findings (What the Data Says):")
    st.markdown("""
    * **Dominant Force:** The **Consumer** segment is the primary revenue driver, generating the highest sales volume and transaction count (over 2,500 orders).
    * **Shipping Preferences:** Individual consumers heavily favor **Standard Class** and **Second Class** shipping over expedited modes.
    * **Business Interpretation:** Retail consumers pay for shipping out of pocket, indicating high **Cost Sensitivity**. Conversely, corporate clients prioritize speed and reliability, showing lower sensitivity to premium shipping fees.
    """)

with col2:
    st.success("### 🛠️ Actionable Strategic Decisions:")
    st.markdown("""
    1. **Optimize Economic Shipping Freight:** Renegotiate long-term contracts with regional carriers for *Standard Class* shipping to lower per-unit logistical costs, directly expanding consumer profit margins.
    2. **Targeted B2B Premium Campaigns:** Since the **Corporate** segment is less price-sensitive, launch dedicated marketing campaigns promoting premium delivery (*First Class* or *Same Day*) to increase high-margin service adoption.
    """)

st.divider()

# ─── SECTION 2: LOSS PRODUCTS ───
st.header("2️⃣ Risk Management & Profit Loss Mitigation")

col3, col4 = st.columns([1, 1])

with col3:
    st.warning("### 🔍 Key Findings (What the Data Says):")
    st.markdown("""
    * **The Sales vs. Profit Trap:** Advanced analysis revealed a critical vulnerability: multiple high-revenue products generating thousands in sales are actually yielding a **Negative Net Profit**.
    * **Primary Root Cause:** This financial leakage is driven by **Aggressive, Uncalculated Discounting** strategies or high logistical weight-costs absorbed entirely by the store.
    """)

with col4:
    st.success("### 🛠️ Actionable Strategic Decisions:")
    st.markdown("""
    1. **Enforce Strict Discount Caps:** Establish a hard ceiling for discounts on historically unprofitable sub-categories (e.g., capping promotional discounts at 15% maximum) to protect core margins.
    2. **Revise Freight Allocation:** Eliminate automated free shipping eligibility for heavy or bulky loss-making items, transferring a portion of the logistical cost to the end consumer.
    3. **Supplier Procurement Review:** Renegotiate wholesale acquisition costs with the manufacturers of the *Top 10 Loss Products*. If margins cannot be salvaged, phase out these items to stop capital hemorrhaging.
    """)

st.divider()

# ─── SECTION 3: SUMMARY MATRIX ───
st.header("📋 Strategic Action Matrix")
st.markdown("A quick-reference architectural guide mapping operational vulnerabilities to data-driven corporate actions:")

# Matrix representation using structured business phrasing
decision_matrix = {
    "Analytical Domain": [
        "Shipping Logistics", 
        "Customer Segments", 
        "Product Engineering", 
        "Profit Optimization"
    ],
    "Identified Vulnerability": [
        "Escalating costs within expedited shipping fulfillment.", 
        "Underutilized corporate revenue in premium shipping tiers.", 
        "High-revenue products yielding negative net margins.", 
        "Profit leakage stemming from unchecked promotional discounts."
    ],
    "Data-Driven Corporate Action": [
        "Secure long-term, fixed-rate economic freight agreements.", 
        "Deploy targeted B2B loyalty programs emphasizing priority shipping.", 
        "Execute immediate repricing strategies or inventory liquidation.", 
        "Implement algorithmic discount caps tied strictly to basket size."
    ]
}

st.table(decision_matrix)

st.balloons()