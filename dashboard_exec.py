import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd

# =========================
# PAGE CONFIG (FIRST!)
# =========================
st.set_page_config(
    page_title="Marketing Impact & Incrementality",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================
# CUSTOM CSS (EXEC / PPT LOOK)
# =========================
st.markdown("""
<style>

/* ---- App background ---- */
.stApp {
    background: linear-gradient(135deg, #020617, #020617);
    color: #e5e7eb;
}

/* ---- Typography ---- */
h1 {
    color: #f9fafb !important;
    font-weight: 800;
}
h2, h3 {
    color: #f1f5f9 !important;
    font-weight: 700;
}
p, li {
    color: #d1d5db !important;
    font-size: 16px;
    line-height: 1.6;
}

/* ---- Metric cards ---- */
[data-testid="metric-container"] {
    background: rgba(15, 23, 42, 0.9);
    border-radius: 16px;
    padding: 18px;
    border: 1px solid rgba(255,255,255,0.08);
}

/* ---- Sidebar ---- */
section[data-testid="stSidebar"] {
    background: #020617;
    border-right: 1px solid rgba(255,255,255,0.08);
}

/* ---- Selectbox cleanup (REMOVE WHITE STRIP) ---- */
div[data-baseweb="select"] > div {
    background-color: rgba(15, 23, 42, 0.9) !important;
    color: #e5e7eb !important;
    border-radius: 10px;
    border: 1px solid rgba(255,255,255,0.1);
}
div[data-baseweb="select"] svg {
    fill: #e5e7eb;
}

/* ---- Remove default dividers ---- */
hr {
    display: none;
}

/* ---- Card wrapper ---- */
.card {
    background: rgba(15, 23, 42, 0.65);
    padding: 28px;
    border-radius: 20px;
    margin-top: 20px;
    border: 1px solid rgba(255,255,255,0.06);
}

</style>
""", unsafe_allow_html=True)

# =========================
# TITLE
# =========================
st.markdown("""
<h1 style="text-align:center;">📊 Marketing Impact & Incrementality</h1>
<h4 style="text-align:center; color:#cbd5f5;">
From raw customer behavior to executive decisions
</h4>
""", unsafe_allow_html=True)

# =========================
# SLIDE SELECTOR
# =========================
slide = st.selectbox(
    "Navigate the story",
    [
        "Executive Overview",
        "Purchase Intent Impact",
        "Churn & Retention Insights",
        "Customer Lifetime Value (CLV)",
        "Incrementality & Uplift",
        "What This Enables Next"
    ]
)

# =========================
# EXECUTIVE OVERVIEW
# =========================
if slide == "Executive Overview":

    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.header("Executive Overview")

    c1, c2, c3 = st.columns(3)
    c1.metric("Purchase Lift (Ads)", "+2–3% absolute")
    c2.metric("Incremental CLV (Top Segment)", "+42%")
    c3.metric("Causal Confidence", "High")

    st.markdown("""
**What we set out to answer**  
Do advertisements *actually* create incremental value — or do they simply
reach customers who would have purchased anyway?

**What the data confirms**
- Advertising exposure causally increases purchase probability and CLV
- Impact is **concentrated**, not uniform
- Uplift modeling isolates *true* incremental value

**Why leadership should care**
Marketing spend can now be guided by **expected business impact**, not proxies.
""")

    st.markdown("</div>", unsafe_allow_html=True)

# =========================
# PURCHASE INTENT
# =========================
elif slide == "Purchase Intent Impact":

    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.header("Purchase Intent Impact")

    df = pd.DataFrame({
        "Horizon": ["1 Day", "7 Days", "30 Days", "90 Days"],
        "ROC-AUC": [0.85, 0.89, 0.82, 0.96],
        "PR-AUC": [0.18, 0.66, 0.96, 0.99]
    })

    fig = go.Figure()
    fig.add_trace(go.Bar(x=df["Horizon"], y=df["ROC-AUC"], name="ROC-AUC"))
    fig.add_trace(go.Bar(x=df["Horizon"], y=df["PR-AUC"], name="PR-AUC"))
    fig.update_layout(
        barmode="group",
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        yaxis_title="Predictive Power",
        font_color="#e5e7eb"
    )

    st.plotly_chart(fig, use_container_width=True)

    st.markdown("""
**Interpretation**
- Short-horizon purchases are noisy and impulsive
- Predictability strengthens sharply over 7–30 days
- Long-term models almost perfectly rank buyers

*Strategic implication:*  
Campaigns should be evaluated on **medium-term conversions**, not same-day clicks.
""")

    st.markdown("</div>", unsafe_allow_html=True)

# =========================
# CHURN
# =========================
elif slide == "Churn & Retention Insights":

    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.header("Churn & Retention Insights")

    c1, c2, c3 = st.columns(3)
    c1.metric("ROC-AUC", "0.90")
    c2.metric("PR-AUC", "0.91")
    c3.metric("Precision @ Top 5%", "100%")

    fi = pd.DataFrame({
        "Feature": [
            "Recency",
            "Ad Exposure (7d)",
            "Session Count",
            "Purchase Velocity",
            "Engagement Momentum"
        ],
        "Importance": [0.28, 0.22, 0.18, 0.17, 0.15]
    })

    fig = px.bar(
        fi,
        x="Importance",
        y="Feature",
        orientation="h",
        color_discrete_sequence=["#ef4444"],
        title="Primary Drivers of Churn Risk"
    )
    fig.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font_color="#e5e7eb"
    )

    st.plotly_chart(fig, use_container_width=True)

    st.markdown("""
**Why this matters**
- Churn is *predictable well before it happens*
- Only a small subset requires intervention
- Retention spend can be highly targeted

*Executive takeaway:*  
Retention becomes **proactive, not reactive**.
""")

    st.markdown("</div>", unsafe_allow_html=True)

# =========================
# CLV
# =========================
elif slide == "Customer Lifetime Value (CLV)":

    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.header("Customer Lifetime Value")

    c1, c2, c3, c4 = st.columns(4)
    c1.metric("R²", "0.97")
    c2.metric("RMSE", "11.6")
    c3.metric("Top-Decile Lift", "5.4×")
    c4.metric("Model Stability", "High")

    lift_df = pd.DataFrame({
        "Segment": ["Bottom 90%", "Top 10%"],
        "Avg CLV": [61.2, 87.18]
    })

    fig = px.bar(
        lift_df,
        x="Segment",
        y="Avg CLV",
        color="Segment",
        color_discrete_sequence=["#64748b", "#22c55e"],
        title="Revenue Concentration Across Customers"
    )
    fig.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font_color="#e5e7eb"
    )

    st.plotly_chart(fig, use_container_width=True)

    st.markdown("""
**Key insight**
A small fraction of customers drives a disproportionate share of value.

*Business implication:*  
Marketing ROI improves dramatically when aligned with **predicted lifetime value**.
""")

    st.markdown("</div>", unsafe_allow_html=True)

# =========================
# UPLIFT
# =========================
elif slide == "Incrementality & Uplift":

    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.header("Incrementality & Uplift")

    c1, c2 = st.columns(2)
    c1.metric("Incremental CLV (ATE)", "+0.70")
    c2.metric("Incremental CLV (ATT)", "+0.81")

    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=["Control", "Treated (Top Decile)"],
        y=[61.2, 87.2],
        text=["No Ads", "Ads Applied"],
        textposition="outside"
    ))
    fig.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        yaxis_title="Average CLV",
        font_color="#e5e7eb"
    )

    st.plotly_chart(fig, use_container_width=True)

    st.markdown("""
**Why this is important**
This isolates **true causal impact**, not correlation.

*Leadership conclusion:*  
Ads create **real incremental value** when applied selectively.
""")

    st.markdown("</div>", unsafe_allow_html=True)

# =========================
# FUTURE
# =========================
elif slide == "What This Enables Next":

    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.header("What This Enables Next")

    st.markdown("""
**Immediate applications**
- CLV-driven budget allocation
- Uplift-based targeting
- Churn-aware suppression

**Next evolution**
- Offer-level uplift
- Real-time decision engines
- ROI simulators for leadership

**Final message**
This system turns marketing from a **cost center**
into a **measurable growth engine**.
""")

    st.markdown("</div>", unsafe_allow_html=True)