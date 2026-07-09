import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Tourism Industry Analytics Dashboard", layout="wide")

@st.cache_data
def load_data():
    return pd.read_csv("../data/cleaned/cleaned_tourism_data.csv")

df = load_data()

st.title("🌍 Tourism Industry Analytics Dashboard")
st.caption("Visitor Trends, Seasonal Demand, Economic Impact, and Travel Pattern Analysis")

# --- Sidebar filters ---
st.sidebar.header("Filters")
countries = st.sidebar.multiselect("Country", sorted(df['Country'].unique()), default=None)
years = st.sidebar.multiselect("Year", sorted(df['Year'].unique()), default=None)
seasons = st.sidebar.multiselect("Season", sorted(df['Season'].unique()), default=None)

filtered = df.copy()
if countries:
    filtered = filtered[filtered['Country'].isin(countries)]
if years:
    filtered = filtered[filtered['Year'].isin(years)]
if seasons:
    filtered = filtered[filtered['Season'].isin(seasons)]

# --- KPIs ---
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Tourists", f"{int(filtered['Number_of_Tourists'].sum()):,}")
col2.metric("Total Revenue", f"${filtered['Tourism_Revenue_USD'].sum():,.0f}")
col3.metric("Avg Hotel Occupancy", f"{filtered['Hotel_Occupancy_Rate'].mean():.1f}%")
col4.metric("Avg Satisfaction", f"{filtered['Tourist_Satisfaction_Score'].mean():.1f}/10")

st.divider()

# --- Row 1 ---
c1, c2 = st.columns(2)
with c1:
    rev_by_country = filtered.groupby('Country')['Tourism_Revenue_USD'].sum().sort_values(ascending=False).reset_index()
    fig = px.bar(rev_by_country, x='Country', y='Tourism_Revenue_USD', title="Tourism Revenue by Country")
    st.plotly_chart(fig, use_container_width=True)

with c2:
    monthly = filtered.groupby('Month')['Number_of_Tourists'].mean().reset_index()
    fig = px.line(monthly, x='Month', y='Number_of_Tourists', markers=True, title="Monthly Tourism Trend")
    st.plotly_chart(fig, use_container_width=True)

# --- Row 2 ---
c3, c4 = st.columns(2)
with c3:
    purpose = filtered['Purpose_of_Visit'].value_counts().reset_index()
    purpose.columns = ['Purpose_of_Visit', 'count']
    fig = px.pie(purpose, names='Purpose_of_Visit', values='count', title="Purpose of Visit")
    st.plotly_chart(fig, use_container_width=True)

with c4:
    seasonal = filtered.groupby('Season')['Tourism_Revenue_USD'].mean().reindex(['Winter','Spring','Summer','Autumn']).reset_index()
    fig = px.bar(seasonal, x='Season', y='Tourism_Revenue_USD', title="Seasonal Tourism Revenue")
    st.plotly_chart(fig, use_container_width=True)

# --- Row 3 ---
c5, c6 = st.columns(2)
with c5:
    fig = px.scatter(filtered, x='Hotel_Rating', y='Tourism_Revenue_USD', title="Hotel Rating vs Tourism Revenue")
    st.plotly_chart(fig, use_container_width=True)

with c6:
    gdp = filtered.groupby('Country')['Contribution_to_GDP_Percent'].mean().sort_values(ascending=False).reset_index()
    fig = px.bar(gdp, x='Country', y='Contribution_to_GDP_Percent', title="GDP Contribution by Country")
    st.plotly_chart(fig, use_container_width=True)

st.divider()
st.subheader("Filtered Data")
st.dataframe(filtered, use_container_width=True)