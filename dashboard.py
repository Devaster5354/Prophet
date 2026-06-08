import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# =====================
# PAGE CONFIG
# =====================
st.set_page_config(
    page_title="ML System Diagnostics – Marketing Models",
    layout="wide"
)

st.title("🔬 ML System Diagnostics – Marketing Models")
st.caption("Engineering-facing view of predictive & causal modeling stack")

section = st.selectbox(
    "Select module",
    [
        "System Overview",
        "Purchase Likelihood Models",
        "Churn Model",
        "CLV Model",
        "Uplift Models (T / S / X Learners)",
        "Failure Modes & Next Steps"
    ]
)

# =====================
# SYSTEM OVERVIEW
# =====================
if section == "System Overview":

    st.header("System Overview")

    st.markdown(
        """
        **Dataset**
        - ~66k customer-anchor rows
        - Event-aggregated behavioral features
        - Time-respecting targets (no lookahead)

        **Model Families**
        - Binary classification (purchase, churn)
        - Regression (CLV)
        - Meta-learning (uplift / ITE)

        **Validation**
        - Time-safe splits
        - K-fold OOF for CLV
        - Top-k metrics for targeting relevance

        **Key Design Choices**
        - PR-AUC over accuracy for imbalance
        - Top-decile metrics for business realism
        - Separate predictive vs causal modeling
        """
    )

import plotly.graph_objects as go

# =====================
# PURCHASE MODELS
# =====================
if section == "Purchase Likelihood Models":

    st.header("Purchase Likelihood Models")

    df = pd.DataFrame({
        "Horizon": ["1d", "7d", "30d", "90d"],
        "ROC-AUC": [0.8506, 0.8941, 0.8172, 0.9586],
        "PR-AUC": [0.1830, 0.6627, 0.9569, 0.9982],
        "Precision@Top5%": [0.224, 0.8062, None, None]
    })

    st.subheader("Core Metrics")
    st.dataframe(df, use_container_width=True)

    # ---- FIXED PLOT ----
    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=df["Horizon"],
            y=df["ROC-AUC"],
            mode="lines+markers",
            name="ROC-AUC",
            line=dict(width=3)
        )
    )

    fig.add_trace(
        go.Scatter(
            x=df["Horizon"],
            y=df["PR-AUC"],
            mode="lines+markers",
            name="PR-AUC",
            line=dict(width=3)
        )
    )

    fig.update_layout(
        title="Metric Behavior Across Prediction Horizons",
        xaxis_title="Prediction Horizon",
        yaxis_title="Score",
        yaxis=dict(range=[0, 1]),
        template="plotly_white",
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
    )

    st.plotly_chart(fig, use_container_width=True)

    st.markdown(
        """
        **Engineering Interpretation**
        - 1-day horizon is severely imbalanced → low PR-AUC expected
        - Predictive signal increases with time horizon
        - 30d & 90d models are ranking-strong (PR-AUC > 0.95)
        - Top-5% precision validates use in targeting pipelines
        """
    )


# =====================
# CHURN MODEL
# =====================
elif section == "Churn Model":

    st.header("Churn Model (30-Day)")

    col1, col2, col3 = st.columns(3)
    col1.metric("ROC-AUC", "0.898")
    col2.metric("PR-AUC", "0.911")
    col3.metric("Precision@Top5%", "1.00")

    st.markdown(
        """
        **Observations**
        - Balanced positive/negative classes (~50%)
        - Strong separability using engagement decay
        - Precision@Top5% = 1.0 implies near-perfect prioritization

        **Model Use**
        - Ranking churn risk
        - Trigger-based retention systems
        - Campaign suppression logic
        """
    )

# =====================
# CLV MODEL
# =====================
elif section == "CLV Model":

    st.header("Customer Lifetime Value Model")

    col1, col2, col3 = st.columns(3)
    col1.metric("R² (Stacked)", "0.97")
    col2.metric("RMSE", "11.64")
    col3.metric("Top-Decile Lift", "5.41x")

    fig = go.Figure()
    fig.add_bar(
        x=["Bottom 90%", "Top 10%"],
        y=[1, 5.41]
    )

    fig.update_layout(
        title="CLV Concentration (Lift)",
        yaxis_title="Relative Value"
    )

    st.plotly_chart(fig, use_container_width=True)

    st.markdown(
        """
        **Architecture**
        - Base learners: LightGBM + CatBoost
        - Meta-learner: Ridge
        - OOF stacking prevents leakage

        **Interpretation**
        - Revenue distribution is heavy-tailed
        - Model captures non-linear spend dynamics well
        """
    )

# =====================
# UPLIFT MODELS
# =====================
elif section == "Uplift Models (T / S / X Learners)":

    st.header("Uplift / Incrementality Models")

    df = pd.DataFrame({
        "Method": ["T-Learner", "S-Learner", "X-Learner"],
        "ATE (CLV)": [0.9683, 0.0000, 0.7011],
        "ATT (CLV)": [-0.7501, 0.0000, 0.8120]
    })

    st.subheader("Causal Effect Estimates")
    st.dataframe(df, use_container_width=True)

    fig = go.Figure()
    fig.add_bar(x=df["Method"], y=df["ATE (CLV)"], name="ATE")
    fig.add_bar(x=df["Method"], y=df["ATT (CLV)"], name="ATT")

    fig.update_layout(
        title="Causal Effect Comparison",
        barmode="group"
    )

    st.plotly_chart(fig, use_container_width=True)

    st.markdown(
        """
        **Engineering Interpretation**
        - S-Learner collapses due to dominant treatment feature
        - T-Learner unstable under imbalance
        - X-Learner best bias-variance trade-off

        **Policy Proxy**
        - Top-decile CLV: Treated ≈ 87 vs Control ≈ 61
        """
    )

# =====================
# FAILURE MODES
# =====================
elif section == "Failure Modes & Next Steps":

    st.header("Failure Modes & Next Steps")

    st.markdown(
        """
        **Known Limitations**
        - Short-horizon purchase labels are noisy
        - S-Learner underfits in high-capacity models
        - Uplift assumes no hidden confounders

        **Engineering Improvements**
        - Calibrated probability outputs
        - Time-series models (RNN / TCN)
        - Doubly-robust estimators
        - Online A/B integration

        **Production Considerations**
        - Batch scoring cadence
        - Feature freshness
        - Model drift monitoring
        """
    )
