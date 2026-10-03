# attr_app.py - Streamlit Employee Attrition Insight Dashboard
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Page configuration
st.set_page_config(page_title="Employee Attrition Executive Insight Report", layout="wide")

# Title and Overarching Insight Header
st.title("📊 Employee Attrition Executive Insight Report")
st.markdown("---")

# Three-line Overarching Insight Summary
st.markdown("""
### 🌐 Executive Summary
1. **Primary Driver:** Working mandatory overtime emerges as the single largest behavioral catalyst for employee turnover across all job levels.
2. **Vulnerable Segments:** Junior employees (`Job Level 1`) in lower monthly income brackets exhibit disproportionately higher attrition rates.
3. **Strategic Action:** Management must institute proactive workload balancing, review compensation benchmarks for entry tiers, and introduce targeted retention programs.
""")
st.markdown("---")

# Load Dataset
@st.cache_data
def load_data():
    return pd.read_csv("DA314_S10_EmployeeAttrition_Cleaned_Data_Practice.csv")

try:
    df = load_data()
except Exception as e:
    st.error(f"Error loading dataset: {e}")
    st.stop()

# Layout: Two columns for charts and tailored insights
col1, col2 = st.columns(2)

with col1:
    st.subheader("1. Attrition Rate by OverTime")
    fig, ax = plt.subplots(figsize=(6, 4))
    sns.countplot(data=df, x='OverTime', hue='Attrition', palette='Set1', ax=ax)
    ax.set_title("Impact of OverTime on Attrition")
    st.pyplot(fig)
    st.markdown("**Tailored Insight:** Employees working mandatory overtime show significantly higher turnover proportions due to fatigue and burnout.")

with col2:
    st.subheader("2. Monthly Income Distribution")
    fig, ax = plt.subplots(figsize=(6, 4))
    sns.boxplot(data=df, x='Attrition', y='MonthlyIncome', palette='pastel', ax=ax)
    ax.set_title("Monthly Income vs Attrition")
    st.pyplot(fig)
    st.markdown("**Tailored Insight:** Departed employees cluster heavily at the lower end of the monthly income brackets, confirming pay dissatisfaction.")

st.markdown("---")

col3, col4 = st.columns(2)

with col3:
    st.subheader("3. Job Level Vulnerability")
    fig, ax = plt.subplots(figsize=(6, 4))
    sns.countplot(data=df, x='JobLevel', hue='Attrition', palette='coolwarm', ax=ax)
    ax.set_title("Job Level Count by Attrition")
    st.pyplot(fig)
    st.markdown("**Tailored Insight:** Junior staff at Job Level 1 represent the highest proportion of organizational turnover.")

with col4:
    st.subheader("4. Department-wise Attrition")
    fig, ax = plt.subplots(figsize=(6, 4))
    sns.countplot(data=df, x='Department', hue='Attrition', palette='Set2', ax=ax)
    ax.set_title("Attrition Across Departments")
    plt.xticks(rotation=45, ha='right')
    st.pyplot(fig)
    st.markdown("**Tailored Insight:** Research & Development and Sales departments experience the highest absolute volume of departures.")

st.markdown("---")

# Additional Summary Insights
st.subheader("📋 Comprehensive Summary Takeaways")
st.markdown("""
* **OverTime Burnout:** Working mandatory overtime emerges as the single largest behavioral catalyst for employee turnover.
* **Junior-Level Vulnerability:** Entry-level positions (`Job Level 1`) exhibit disproportionately higher attrition rates.
* **Strategic Recommendation:** Management must institute proactive workload balancing and entry-tier compensation reviews.
""")

st.success("Dashboard successfully loaded and ready for stakeholder dissemination!")