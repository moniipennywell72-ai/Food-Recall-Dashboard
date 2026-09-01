import pandas as pd
import plotly.express as px
import streamlit as st

from analysis import classify_priority
from data_loader import load_fda_data

st.set_page_config(
    page_title="FDA Food Recall Dashboard",
    page_icon="🧪",
    layout="wide",
)

st.title("FDA Food Recall Dashboard")


df = load_fda_data()
if df.empty:
    st.warning("No recall data was returned from the FDA API.")
    st.stop()


df["Priority"] = df["classification"].apply(classify_priority)


# Overview metrics
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Recalls", len(df))
col2.metric("Critical Recalls", int((df["classification"] == "Class I").sum()))
col3.metric("Ongoing Recalls", int((df["status"] == "Ongoing").sum()))
col4.metric("Affected Firms", int(df["recalling_firm"].nunique()))

st.subheader("Recall Classification")
classification_chart = px.pie(df, names="classification", title="Recall Class Distribution")
st.plotly_chart(classification_chart, use_container_width=True)


# Tabs for additional views


tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "Overview",
    "Trends",
    "Contamination Types",
    "Geographic Impact",
    "Firm Analysis",
])

with tab1:
    st.header("Dashboard Overview")
    st.dataframe(df.head(10), use_container_width=True)

with tab2:
    st.header("Recall Trends")
    monthly_trend = (
        df.groupby(df["recall_initiation_date"].dt.to_period("M")).size().reset_index(name="Count")
    )
    monthly_trend["Month"] = monthly_trend["recall_initiation_date"].astype(str)
    trend_chart = px.line(monthly_trend, x="Month", y="Count", markers=True, title="Monthly Recall Trend")
    st.plotly_chart(trend_chart, use_container_width=True)

with tab3:
    st.header("Contamination Types")
    top_reasons = df["reason_for_recall"].value_counts().head(15).reset_index()
    top_reasons.columns = ["Reason", "Count"]
    reason_chart = px.bar(top_reasons, x="Count", y="Reason", orientation="h", title="Top Recall Causes")
    st.plotly_chart(reason_chart, use_container_width=True)
    st.dataframe(top_reasons, use_container_width=True)

with tab4:
    st.header("Geographic Impact")
    location_counts = df["country"].value_counts().head(10).reset_index()
    location_counts.columns = ["Country", "Count"]
    geo_chart = px.bar(location_counts, x="Count", y="Country", orientation="h", title="Recall Distribution by Country")
    st.plotly_chart(geo_chart, use_container_width=True)

with tab5:
    st.header("Firm Analysis")
    firm_counts = df["recalling_firm"].value_counts().head(10).reset_index()
    firm_counts.columns = ["Firm", "Count"]
    firm_chart = px.bar(firm_counts, x="Count", y="Firm", orientation="h", title="Top Recalling Firms")
    st.plotly_chart(firm_chart, use_container_width=True)
