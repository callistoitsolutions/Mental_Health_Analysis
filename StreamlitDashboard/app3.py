import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(layout="wide", page_title="Zimbabwe Mental Health Analysis")

# Sample data generation matching dashboard visuals
@st.cache_data
def load_data():
    np.random.seed(42)
    dates = pd.date_range('2023-01-01', periods=10, freq='M').strftime('%Y-%m')
    age_groups = ['18-25', '26-35', '36-45', '46+']
    genders = ['Male', 'Female']
    statuses = ['Single', 'Married', 'Divorced']
    diagnoses = ['Anxiety', 'Depression', 'PTSD', 'Other']
    helps = ['Counseling', 'Medication', 'Therapy', 'None']
    occupations = ['Employed', 'Unemployed', 'Student']
   
    n = 250
    data = {
        'Date': np.random.choice(dates, n),
        'Age_Group': np.random.choice(age_groups, n),
        'Gender': np.random.choice(genders, n, p=[0.4, 0.6]),
        'Status': np.random.choice(statuses, n),
        'Diagnosis': np.random.choice(diagnoses, n),
        'Help': np.random.choice(helps, n),
        'Occupation': np.random.choice(occupations, n)
    }
    return pd.DataFrame(data)

df = load_data()

## Sidebar Filters
st.sidebar.header("🔧 Filters")
gender_filter = st.sidebar.multiselect("Gender", ['Male', 'Female'], default=['Male', 'Female'])
age_filter = st.sidebar.multiselect("Age Group", df['Age_Group'].unique(), default=df['Age_Group'].unique())
status_filter = st.sidebar.multiselect("Status", df['Status'].unique(), default=df['Status'].unique())

filtered_df = df[
    df['Gender'].isin(gender_filter) &
    df['Age_Group'].isin(age_filter) &
    df['Status'].isin(status_filter)
]

## Main Dashboard
st.title("🏥 Zimbabwe Mental Health Analysis")
st.markdown("---")

## Top Row: Metrics & Charts [file:2]
col1, col2, col3, col4 = st.columns([1.5, 3, 3, 1.5])

with col1:
    st.metric("Total Responses", len(filtered_df))

with col2:
    gender_counts = filtered_df['Gender'].value_counts()
    fig_gender = px.pie(gender_counts, values=gender_counts.values, names=gender_counts.index,
                        color_discrete_sequence=['#636EFA', '#EF553B'], title="Gender")
    st.plotly_chart(fig_gender, use_container_width=True)

with col3:
    age_counts = filtered_df['Age_Group'].value_counts()
    fig_age = px.bar(x=age_counts.index, y=age_counts.values, title="Age Groups",
                     color=age_counts.index, color_discrete_sequence=px.colors.qualitative.Set3)
    st.plotly_chart(fig_age, use_container_width=True)

## Middle Row: Stacked Bar & Status [file:2]
col5, col6 = st.columns(2)

with col5:
    pivot_age_diag = filtered_df.groupby(['Age_Group', 'Diagnosis']).size().unstack(fill_value=0)
    fig_stacked = px.bar(pivot_age_diag, barmode='stack', title="Diagnosis by Age Group")
    st.plotly_chart(fig_stacked, use_container_width=True)

with col6:
    status_counts = filtered_df['Status'].value_counts()
    fig_status = px.pie(status_counts, values=status_counts.values, names=status_counts.index,
                        color_discrete_sequence=['#FF7F0E', '#2CA02C', '#D62728'], title="Status")
    st.plotly_chart(fig_status, use_container_width=True)

## Bottom Row: Line & Horizontal Bar [file:2]
col7, col8 = st.columns(2)

with col7:
    date_counts = filtered_df.groupby('Date').size().reset_index()
    fig_line = px.line(date_counts, x='Date', y=0, title="Total Responses by Date",
                       markers=True, color_discrete_sequence=['red'])
    st.plotly_chart(fig_line, use_container_width=True)

with col8:
    occ_counts = filtered_df['Occupation'].value_counts()
    fig_occ = px.bar(x=occ_counts.values, y=occ_counts.index, orientation='h',
                     title="Occupation", color=occ_counts.index)
    st.plotly_chart(fig_occ, use_container_width=True)