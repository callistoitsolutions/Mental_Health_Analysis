import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime
import io
from pathlib import Path

# ========== PAGE CONFIG ==========
st.set_page_config(
    page_title="Analytics Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ========== CUSTOM CSS - PROFESSIONAL CORPORATE DESIGN ==========
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
    * {
        margin: 0;
        padding: 0;
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    }
    
    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Main container */
    .main {
        background: #f8f9fc;
        padding: 0 !important;
    }
    
    .block-container {
        padding: 2rem 3rem 3rem 3rem !important;
        max-width: 100% !important;
    }
    
    /* Sidebar - Modern Corporate Style */
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #1e293b 0%, #0f172a 100%);
    box-shadow: 4px 0 20px rgba(0, 0, 0, 0.08);
}

[data-testid="stSidebar"] * {
    color: #e2e8f0 !important;
}

/* Sidebar Labels */
[data-testid="stSidebar"] .stRadio > label,
[data-testid="stSidebar"] .stMultiSelect > label {
    color: #cbd5e1 !important;
    font-weight: 500;
    font-size: 13px;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    margin-bottom: 8px;
}

/* BaseWeb Select (FIXED) */
[data-testid="stSidebar"] [data-baseweb="select"] {
    background-color: #1e293b !important;
    border-radius: 8px;
}

/* 🔥 FORCE TEXT COLOR INSIDE SELECT */
[data-testid="stSidebar"] [data-baseweb="select"] * {
    color: #e2e8f0 !important;
}

/* Dropdown menu options */
[data-testid="stSidebar"] [role="listbox"] {
    background-color: #0f172a !important;
}

[data-testid="stSidebar"] [role="option"] {
    color: #e2e8f0 !important;
}

    
    /* Top Header Bar */
    .top-header {
        background: white;
        padding: 20px 30px;
        margin: -2rem -3rem 2rem -3rem;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.04);
        border-bottom: 1px solid #e2e8f0;
        display: flex;
        justify-content: space-between;
        align-items: center;
    }
    
    .welcome-text {
        font-size: 24px;
        font-weight: 600;
        color: #1e293b;
        margin: 0;
    }
    
    .user-info {
        display: flex;
        align-items: center;
        gap: 12px;
        color: #64748b;
        font-size: 14px;
    }
    
    /* KPI Cards - Professional Style */
    .kpi-container {
        background: white;
        border-radius: 12px;
        padding: 24px;
        box-shadow: 0 1px 3px rgba(0, 0, 0, 0.08);
        border: 1px solid #e2e8f0;
        transition: all 0.3s ease;
        height: 100%;
    }
    
    .kpi-container:hover {
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.12);
        transform: translateY(-2px);
    }
    
    .kpi-label {
        font-size: 13px;
        font-weight: 500;
        color: blue;
        text-transform: uppercase;
        letter-spacing: 0.5px;
        margin-bottom: 8px;
    }
    
    .kpi-value {
        font-size: 32px;
        font-weight: 700;
        color: #1e293b;
        margin-bottom: 8px;
    }
    
    .kpi-change {
        font-size: 13px;
        color: #10b981;
        font-weight: 500;
    }
    
    .kpi-change.negative {
        color: #ef4444;
    }
    
    .kpi-icon {
        width: 48px;
        height: 48px;
        border-radius: 10px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 24px;
        margin-bottom: 16px;
    }
    
    .icon-blue { background: linear-gradient(135deg, #3b82f6 0%, #2563eb 100%); }
    .icon-green { background: linear-gradient(135deg, #10b981 0%, #059669 100%); }
    .icon-purple { background: linear-gradient(135deg, #8b5cf6 0%, #7c3aed 100%); }
    .icon-orange { background: linear-gradient(135deg, #f59e0b 0%, #d97706 100%); }
    
    /* Metric styling override */
    .stMetric {
        background: transparent !important;
        padding: 0 !important;
        box-shadow: none !important;
    }
    
    [data-testid="metric-container"] {
        background: transparent !important;
    }
    
    [data-testid="stMetricValue"] {
        font-size: 32px !important;
        font-weight: 700 !important;
        color: blue !important;
    }
    
    [data-testid="stMetricLabel"] {
        font-size: 13px !important;
        font-weight: 500 !important;
        color: blue !important;
        text-transform: uppercase !important;
        letter-spacing: 0.5px !important;
    }
    
    /* Headers */
    h1 {
        color: #1e293b;
        font-size: 28px;
        font-weight: 700;
        margin-bottom: 8px;
        letter-spacing: -0.5px;
    }
    
    h2 {
        color: #334155;
        font-size: 20px;
        font-weight: 600;
        margin-bottom: 20px;
        letter-spacing: -0.3px;
    }
    
    h3 {
        color: #475569;
        font-size: 16px;
        font-weight: 600;
        margin-bottom: 16px;
    }
    
    /* Tabs - Modern Corporate */
    .stTabs {
        background: white;
        border-radius: 12px;
        padding: 0;
        box-shadow: 0 1px 3px rgba(0, 0, 0, 0.08);
        border: 1px solid #e2e8f0;
        overflow: hidden;
    }
    
    .stTabs [data-baseweb="tab-list"] {
        background: #f8f9fc;
        gap: 0;
        padding: 0;
        border-bottom: none;
    }
    
    .stTabs [data-baseweb="tab"] {
        background: transparent;
        border: none;
        border-bottom: 3px solid transparent;
        color: blue;
        font-weight: 500;
        font-size: 14px;
        padding: 16px 28px;
        transition: all 0.2s ease;
    }
    
    .stTabs [aria-selected="true"] {
        background: white;
        color: blue;
        border-bottom-color: #3b82f6;
    }
    
    .stTabs [data-baseweb="tab"]:hover {
        background: rgba(59, 130, 246, 0.05);
        color: blue;
    }
    
    .stTabs [data-baseweb="tab-panel"] {
        padding: 28px;
        background: white;
    }
    
    /* Chart containers */
    .chart-container {
        background: white;
        border-radius: 12px;
        padding: 24px;
        box-shadow: 0 1px 3px rgba(0, 0, 0, 0.08);
        border: 1px solid #e2e8f0;
        margin-bottom: 20px;
    }
    
    .chart-title {
        font-size: 16px;
        font-weight: 600;
        color: #1e293b;
        margin-bottom: 20px;
        padding-bottom: 12px;
        border-bottom: 1px solid #e2e8f0;
    }
    
    /* Plotly chart styling */
    .js-plotly-plot {
        border-radius: 8px;
    }
    
    /* Buttons - Corporate Style */
    .stButton > button {
        background: linear-gradient(135deg, #3b82f6 0%, #2563eb 100%);
        color: white;
        border: none;
        border-radius: 8px;
        padding: 12px 24px;
        font-weight: 600;
        font-size: 14px;
        transition: all 0.3s ease;
        box-shadow: 0 2px 8px rgba(59, 130, 246, 0.25);
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    
    .stButton > button:hover {
        transform: translateY(-1px);
        box-shadow: 0 4px 12px rgba(59, 130, 246, 0.35);
        background: linear-gradient(135deg, #2563eb 0%, #1d4ed8 100%);
    }
    
    /* Download Button */
    [data-testid="stDownloadButton"] > button {
        background: white !important;
        color: #3b82f6 !important;
        border: 2px solid #3b82f6 !important;
        border-radius: 8px !important;
        padding: 12px 24px !important;
        font-weight: 600 !important;
        font-size: 14px !important;
        transition: all 0.3s ease !important;
        box-shadow: none !important;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    
    [data-testid="stDownloadButton"] > button:hover {
        background: #3b82f6 !important;
        color: white !important;
        transform: translateY(-1px);
        box-shadow: 0 4px 12px rgba(59, 130, 246, 0.25) !important;
    }
    
    /* Expander - Professional */
    .streamlit-expanderHeader {
        background: white;
        border: 1px solid #e2e8f0;
        border-radius: 8px;
        padding: 16px 20px;
        font-weight: 600;
        color: #1e293b;
        transition: all 0.2s ease;
    }
    
    .streamlit-expanderHeader:hover {
        background: #f8f9fc;
        border-color: #cbd5e1;
    }
    
    .streamlit-expanderContent {
        background: white;
        border: 1px solid #e2e8f0;
        border-top: none;
        border-radius: 0 0 8px 8px;
        padding: 20px;
    }
    
    /* Dataframe styling */
    [data-testid="dataframe"] {
        border: 1px solid #e2e8f0 !important;
        border-radius: 8px;
        overflow: hidden;
    }
    
    [data-testid="dataframe"] thead tr th {
        background: #f8f9fc !important;
        color: #475569 !important;
        font-weight: 600 !important;
        font-size: 12px !important;
        text-transform: uppercase;
        letter-spacing: 0.5px;
        border-bottom: 2px solid #e2e8f0 !important;
    }
    
    /* Selectbox & Multiselect */
    [data-baseweb="select"] {
        border-radius: 8px;
        border-color: #e2e8f0;
    }
    
    /* Alerts */
    .stAlert {
        border-radius: 8px;
        border-left-width: 4px;
        padding: 16px 20px;
        font-size: 14px;
    }
    
    .stSuccess {
        background-color: #f0fdf4 !important;
        border-left-color: #10b981 !important;
        color: #065f46 !important;
    }
    
    .stWarning {
        background-color: #fffbeb !important;
        border-left-color: #f59e0b !important;
        color: #92400e !important;
    }
    
    .stError {
        background-color: #fef2f2 !important;
        border-left-color: #ef4444 !important;
        color: #991b1b !important;
    }
    
    .stInfo {
        background-color: #eff6ff !important;
        border-left-color: #3b82f6 !important;
        color: #1e40af !important;
    }
    
    /* Divider */
    hr {
        border: none;
        height: 1px;
        background: #e2e8f0;
        margin: 32px 0;
    }
    
    /* File uploader */
    [data-testid="stFileUploadDropzone"] {
        border-radius: 8px;
        border: 2px dashed #cbd5e1;
        background: #f8f9fc;
        padding: 32px;
        transition: all 0.3s ease;
    }
    
    [data-testid="stFileUploadDropzone"]:hover {
        border-color: #3b82f6;
        background: #eff6ff;
    }
    
    /* Sidebar logo area */
    .sidebar-logo {
        text-align: center;
        padding: 24px 0;
        border-bottom: 1px solid rgba(255, 255, 255, 0.1);
        margin-bottom: 24px;
    }
    
    .sidebar-title {
        color: white !important;
        font-size: 20px !important;
        font-weight: 700 !important;
        margin-top: 12px !important;
    }
    
    /* Section cards */
    .section-card {
        background: white;
        border-radius: 12px;
        padding: 28px;
        box-shadow: 0 1px 3px rgba(0, 0, 0, 0.08);
        border: 1px solid #e2e8f0;
        margin-bottom: 24px;
    }
    
    .section-header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 24px;
        padding-bottom: 16px;
        border-bottom: 1px solid #e2e8f0;
    }
    
    /* Stats badge */
    .stats-badge {
        display: inline-block;
        padding: 6px 12px;
        background: #eff6ff;
        color: #3b82f6;
        border-radius: 6px;
        font-size: 12px;
        font-weight: 600;
        margin-left: 12px;
    }
    
    /* Footer */
    .footer {
        background: rgb(49, 51, 63);;
        border-top: 1px solid #e2e8f0;
        padding: 24px 0;
        margin-top: 48px;
        text-align: center;
        color: white;
        font-size: 16px;
        font-weight:bold;
    }
</style>
""", unsafe_allow_html=True)

# ========== HELPER FUNCTIONS ==========
def detect_column_types(df):
    """Detect numeric, categorical, and date columns"""
    numeric_cols = df.select_dtypes(include=['int64', 'float64', 'int32', 'float32']).columns.tolist()
    categorical_cols = df.select_dtypes(include=['object', 'category']).columns.tolist()
    date_cols = df.select_dtypes(include=['datetime64']).columns.tolist()
    
    for col in categorical_cols.copy():
        try:
            pd.to_datetime(df[col], errors='raise')
            df[col] = pd.to_datetime(df[col])
            date_cols.append(col)
            categorical_cols.remove(col)
        except:
            pass
   
    return numeric_cols, categorical_cols, date_cols
   
def is_mental_health_data(df):
    """Check if dataframe contains mental health specific columns"""
    mental_health_keywords = ['patient', 'therapy', 'provider', 'session', 'treatment', 'risk', 'attendance', 'psychiatric']
    col_names_lower = [col.lower() for col in df.columns]
    for keyword in mental_health_keywords:
        if any(keyword in col for col in col_names_lower):
            return True
    return False
    
@st.cache_data
def load_default_data():
    """Load data from the existing project structure"""
    try:
        csv_path = Path(__file__).parent.parent / 'Dataset' / 'CleanedData' / 'patients_master_clean.csv'
        if not csv_path.exists():
            return None, "File not found"
        df = pd.read_csv(csv_path)
        if 'Registration_Date' in df.columns:
            df['Registration_Date'] = pd.to_datetime(df['Registration_Date'], errors='coerce')
        if 'Attendance_Rate' in df.columns:
            df['Attendance_Rate'] = pd.to_numeric(df['Attendance_Rate'], errors='coerce')
        if 'Attendance_Rate_Fixed' not in df.columns:
            if 'Sessions_Attended' in df.columns and 'Total_Sessions_Assigned' in df.columns:
                df['Attendance_Rate_Fixed'] = df['Sessions_Attended'] / df['Total_Sessions_Assigned']
        return df, None
    except Exception as e:
        return None, str(e)

def load_uploaded_data(uploaded_file):
    """Load and process uploaded CSV file"""
    try:
        df = pd.read_csv(uploaded_file)
        for col in df.columns:
            if df[col].dtype == 'object':
                try:
                    df[col] = pd.to_datetime(df[col], errors='ignore')
                except:
                    pass
        for col in df.columns:
            if df[col].dtype == 'object':
                try:
                    df[col] = pd.to_numeric(df[col], errors='ignore')
                except:
                    pass
        return df, None
    except Exception as e:
        return None, str(e)

# ========== SIDEBAR ==========
with st.sidebar:
    st.markdown('<div class="sidebar-logo">', unsafe_allow_html=True)
    st.image("https://img.icons8.com/fluency/96/hospital.png", width=64)
    st.markdown(
        '<p class="sidebar-title">Mental Health<br>Analytics</p>',
        unsafe_allow_html=True
    )
    st.markdown('</div>', unsafe_allow_html=True)

    
    st.markdown("### 📂 Data Source")
    data_source = st.radio(
        "",
        ["Use Default Dataset", "Upload New CSV File"],
        label_visibility="collapsed"
    )
    
    df = None
    error_msg = None
    is_mental_health = False
    
    if data_source == "Upload New CSV File":
        st.markdown("---")
        st.markdown("### 📤 File Upload")
        uploaded_file = st.file_uploader("", type=['csv'], label_visibility="collapsed")
        if uploaded_file is not None:
            df, error_msg = load_uploaded_data(uploaded_file)
            if df is not None:
                st.success(f"✓ {uploaded_file.name}")
                st.info(f"📊 {len(df):,} rows × {len(df.columns)} cols")
                is_mental_health = is_mental_health_data(df)
            else:
                st.error(f"Error: {error_msg}")
        else:
            st.info("Please upload a CSV file")
            st.stop()
    else:
        df, error_msg = load_default_data()
        if df is not None:
            st.success("✓ Default dataset loaded")
            is_mental_health = True
        else:
            st.error(f"Could not load default dataset")
            st.stop()
    
    if df is None:
        st.stop()
    
    total_records = len(df)
    numeric_cols, categorical_cols, date_cols = detect_column_types(df)
    
    st.markdown("---")
    st.markdown("### 🔍 Filters")
    
    selected_filters = {}
    if len(categorical_cols) > 0:
        for col in categorical_cols[:4]:
            unique_values = df[col].dropna().unique()
            if len(unique_values) <= 100:
                default_selection = list(unique_values)[:10] if len(unique_values) > 10 else list(unique_values)
                selected = st.multiselect(col, options=sorted(unique_values, key=str), default=default_selection, key=f"filter_{col}")
                if len(selected) > 0:
                    selected_filters[col] = selected
    
    df_filtered = df.copy()
    for col, values in selected_filters.items():
        df_filtered = df_filtered[df_filtered[col].isin(values)]
    
    st.markdown("---")
    st.info(f"**{len(df_filtered):,}** of **{total_records:,}** records")

# ========== TOP HEADER ==========
st.markdown(f"""
<div class="top-header">
    <div>
        <h1 class="welcome-text">🧠 Welcome Back</h1>
        <p style="color: #64748b; margin: 0; font-size: 14px;">
            💚 Monitoring mental health trends and patient insights
        </p>
    </div>
    <div class="user-info">
        <span>📆 {datetime.now().strftime('%B %d, %Y')}</span>
        <span style="color: #cbd5e1;">|</span>
        <span>🧠📈 Mental Health Analyst</span>
    </div>
</div>
""", unsafe_allow_html=True)


# ========== KPI CARDS ==========
cols = st.columns(4)

kpi_data = [
    ("📁", "Total Records", f"{len(df_filtered):,}", "+12.5% from last month", "blue"),
]

for idx, col in enumerate(numeric_cols[:3], 0):
    avg_val = df_filtered[col].mean()
    if avg_val > 1000:
        value = f"{avg_val:,.0f}"
    else:
        value = f"{avg_val:.2f}"
    
    icons = ["📅", "💬", "✔️"]
    colors = ["green", "purple", "blue"]
    kpi_data.append((icons[idx % 3], col[:15], value, "+8.3% from last week", colors[idx % 3]))

for idx, (icon, label, value, change, color) in enumerate(kpi_data[:4]):
    with cols[idx]:
        st.markdown(f"""
        <div class="kpi-container">
            <div class="kpi-icon icon-{color}">{icon}</div>
            <div class="kpi-label">{label}</div>
            <div class="kpi-value">{value}</div>
            <div class="kpi-change">{change}</div>
        </div>
        """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ========== DATA PREVIEW ==========
with st.expander("🔍 Data Preview & Analytics", expanded=False):
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("**📊 Dataset Preview**")
        st.dataframe(df_filtered.head(20), use_container_width=True, height=400)
    with col2:
        st.markdown("**📋 Column Summary**")
        col_info = pd.DataFrame({
            'Column': df_filtered.columns,
            'Type': df_filtered.dtypes.astype(str),
            'Non-Null': df_filtered.count().values,
            'Unique': [df_filtered[col].nunique() for col in df_filtered.columns]
        })
        st.dataframe(col_info, use_container_width=True, height=400)

# ========== CONDITIONAL DASHBOARD ==========
if is_mental_health and all(col in df_filtered.columns for col in ['Gender', 'Program_Type', 'Therapy_Type']):
    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(["📊 Demographics", "🩺 Therapy", "🏥 Psychiatric", "💊 Substance Use", "👨‍⚕️ Providers", "📅 Appointments"])
    
    with tab1:
        st.markdown('<div class="section-card">', unsafe_allow_html=True)
        st.markdown('<div class="section-header"><h2 style="margin:0;">📊 Patient Demographics</h2></div>', unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        with col1:
            if 'Gender' in df_filtered.columns:
                gender_data = df_filtered['Gender'].value_counts().reset_index()
                gender_data.columns = ['Gender', 'Count']
                fig = px.pie(gender_data, names='Gender', values='Count', title="Gender Distribution", hole=0.45, color_discrete_sequence=['#3b82f6', '#8b5cf6', '#10b981'])
                fig.update_layout(
                    paper_bgcolor='rgba(0,0,0,0)',
                    plot_bgcolor='rgba(0,0,0,0)',
                    font=dict(family="Inter", size=12),
                    title_font_size=16,
                    title_font_color='#1e293b',
                    showlegend=True,
                    margin=dict(t=40, b=20, l=20, r=20)
                )
                st.plotly_chart(fig, use_container_width=True)
            st.markdown('</div>', unsafe_allow_html=True)
    
    with tab2:
        st.markdown('<div class="section-card">', unsafe_allow_html=True)
        st.markdown('<div class="section-header"><h2 style="margin:0;">🩺 Therapy Counseling Analytics</h2></div>', unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        with col1:
            if 'Therapy_Type' in df_filtered.columns and 'Case_Status' in df_filtered.columns:
                therapy_sessions = df_filtered.groupby(['Therapy_Type', 'Case_Status']).size().reset_index(name='Count')
                fig = px.bar(therapy_sessions, x='Therapy_Type', y='Count', color='Case_Status', title="Therapy Type Performance", barmode='group', color_discrete_sequence=['#3b82f6', '#10b981', '#f59e0b'])
                fig.update_layout(
                    paper_bgcolor='rgba(0,0,0,0)',
                    plot_bgcolor='rgba(0,0,0,0)',
                    font=dict(family="Inter", size=12),
                    title_font_size=16,
                    title_font_color='#1e293b',
                    xaxis=dict(showgrid=False),
                    yaxis=dict(showgrid=True, gridcolor='#e2e8f0'),
                    margin=dict(t=40, b=20, l=20, r=20)
                )
                st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            if 'Therapy_Type' in df_filtered.columns and 'Sessions_Attended' in df_filtered.columns:
                avg_sessions = df_filtered.groupby('Therapy_Type')['Sessions_Attended'].mean().sort_values(ascending=False).head(8).reset_index()
                fig = px.bar(avg_sessions, x='Sessions_Attended', y='Therapy_Type', orientation='h', title="Avg Sessions by Therapy Type", color='Sessions_Attended', color_continuous_scale='Blues')
                fig.update_layout(
                    paper_bgcolor='rgba(0,0,0,0)',
                    plot_bgcolor='rgba(0,0,0,0)',
                    font=dict(family="Inter", size=12),
                    title_font_size=16,
                    title_font_color='#1e293b',
                    xaxis=dict(showgrid=True, gridcolor='#e2e8f0'),
                    yaxis=dict(showgrid=False),
                    margin=dict(t=40, b=20, l=20, r=20)
                )
                st.plotly_chart(fig, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    with tab3:
        st.markdown('<div class="section-card">', unsafe_allow_html=True)
        st.markdown('<div class="section-header"><h2 style="margin:0;">🏥 Psychiatric Care Analytics</h2></div>', unsafe_allow_html=True)
        
        if 'Program_Type' in df_filtered.columns:
            psych_data = df_filtered[df_filtered['Program_Type'] == 'Psychiatric Care']
            if len(psych_data) > 0:
                cols = st.columns(3)
                with cols[0]:
                    st.markdown('<div class="kpi-container"><div class="kpi-icon icon-blue">🏥</div>', unsafe_allow_html=True)
                    st.metric("Psychiatric Patients", f"{len(psych_data):,}")
                    st.markdown('</div>', unsafe_allow_html=True)
                with cols[1]:
                    if 'Risk_Level' in psych_data.columns:
                        high_risk = len(psych_data[psych_data['Risk_Level'] == 'High'])
                        st.markdown('<div class="kpi-container"><div class="kpi-icon icon-orange">🚨</div>', unsafe_allow_html=True)
                        st.metric("High Risk", f"{high_risk:,}")
                        st.markdown('</div>', unsafe_allow_html=True)
                with cols[2]:
                    if 'Case_Status' in psych_data.columns:
                        completed = len(psych_data[psych_data['Case_Status'] == 'Completed'])
                        st.markdown('<div class="kpi-container"><div class="kpi-icon icon-green">✅</div>', unsafe_allow_html=True)
                        st.metric("Completion Rate", f"{(completed/len(psych_data)*100):.1f}%")
                        st.markdown('</div>', unsafe_allow_html=True)
            else:
                st.warning("⚠️ No psychiatric care data available")
        st.markdown('</div>', unsafe_allow_html=True)
    
    with tab4:
        st.markdown('<div class="section-card">', unsafe_allow_html=True)
        st.markdown('<div class="section-header"><h2 style="margin:0;">💊 Substance Use Treatment</h2></div>', unsafe_allow_html=True)
        
        if 'Program_Type' in df_filtered.columns:
            substance_data = df_filtered[df_filtered['Program_Type'] == 'Substance Use Treatment']
            if len(substance_data) > 0:
                cols = st.columns(3)
                with cols[0]:
                    st.markdown('<div class="kpi-container"><div class="kpi-icon icon-purple">💊</div>', unsafe_allow_html=True)
                    st.metric("Patients", f"{len(substance_data):,}")
                    st.markdown('</div>', unsafe_allow_html=True)
                with cols[1]:
                    if 'Case_Status' in substance_data.columns:
                        completed = len(substance_data[substance_data['Case_Status'] == 'Completed'])
                        st.markdown('<div class="kpi-container"><div class="kpi-icon icon-green">✅</div>', unsafe_allow_html=True)
                        st.metric("Completion Rate", f"{(completed/len(substance_data)*100):.1f}%")
                        st.markdown('</div>', unsafe_allow_html=True)
                with cols[2]:
                    if 'Sessions_Attended' in substance_data.columns:
                        st.markdown('<div class="kpi-container"><div class="kpi-icon icon-blue">📊</div>', unsafe_allow_html=True)
                        st.metric("Avg Sessions", f"{substance_data['Sessions_Attended'].mean():.1f}")
                        st.markdown('</div>', unsafe_allow_html=True)
            else:
                st.warning("⚠️ No substance use data available")
        st.markdown('</div>', unsafe_allow_html=True)
    
    with tab5:
        st.markdown('<div class="section-card">', unsafe_allow_html=True)
        st.markdown('<div class="section-header"><h2 style="margin:0;">👨‍⚕️ Provider Performance</h2></div>', unsafe_allow_html=True)
        
        if 'Provider_Name' in df_filtered.columns:
            provider_data = df_filtered['Provider_Name'].value_counts().head(15).reset_index()
            provider_data.columns = ['Provider', 'Patient_Count']
            fig = px.bar(provider_data, x='Patient_Count', y='Provider', orientation='h', title="Top 15 Providers by Patient Load", color='Patient_Count', color_continuous_scale='Blues')
            fig.update_layout(
                paper_bgcolor='rgba(0,0,0,0)',
                plot_bgcolor='rgba(0,0,0,0)',
                font=dict(family="Inter", size=12),
                title_font_size=16,
                title_font_color='#1e293b',
                xaxis=dict(showgrid=True, gridcolor='#e2e8f0'),
                yaxis=dict(showgrid=False),
                margin=dict(t=40, b=20, l=20, r=20)
            )
            st.plotly_chart(fig, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    with tab6:
        st.markdown('<div class="section-card">', unsafe_allow_html=True)
        st.markdown('<div class="section-header"><h2 style="margin:0;">📅 Appointment Scheduling</h2></div>', unsafe_allow_html=True)
        
        if 'Registration_Date' in df_filtered.columns and 'Program_Type' in df_filtered.columns:
            df_temp = df_filtered.copy()
            df_temp['Month'] = df_temp['Registration_Date'].dt.month
            monthly_prog = df_temp.groupby(['Month', 'Program_Type']).size().reset_index(name='Count')
            fig = px.bar(monthly_prog, x='Month', y='Count', color='Program_Type', title="Monthly Appointments by Program", color_discrete_sequence=['#3b82f6', '#10b981', '#f59e0b', '#8b5cf6'])
            fig.update_layout(
                paper_bgcolor='rgba(0,0,0,0)',
                plot_bgcolor='rgba(0,0,0,0)',
                font=dict(family="Inter", size=12),
                title_font_size=16,
                title_font_color='#1e293b',
                xaxis=dict(showgrid=False),
                yaxis=dict(showgrid=True, gridcolor='#e2e8f0'),
                margin=dict(t=40, b=20, l=20, r=20)
            )
            st.plotly_chart(fig, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

else:
    tab1, tab2, tab3 = st.tabs(["📊 Overview", "📈 Distributions", "🔍 Relationships"])
    
    with tab1:
        st.markdown('<div class="section-card">', unsafe_allow_html=True)
        st.markdown('<div class="section-header"><h2 style="margin:0;">📊 Data Overview</h2></div>', unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        if len(categorical_cols) > 0:
            with col1:
                cat_col = categorical_cols[0]
                cat_data = df_filtered[cat_col].value_counts().head(15).reset_index()
                cat_data.columns = [cat_col, 'Count']
                fig = px.bar(cat_data, x='Count', y=cat_col, orientation='h', title=f"Top 15 {cat_col}", color='Count', color_continuous_scale='Viridis')
                fig.update_layout(
                    paper_bgcolor='rgba(0,0,0,0)',
                    plot_bgcolor='rgba(0,0,0,0)',
                    font=dict(family="Inter", size=12),
                    title_font_size=16,
                    title_font_color='#1e293b',
                    xaxis=dict(showgrid=True, gridcolor='#e2e8f0'),
                    yaxis=dict(showgrid=False),
                    margin=dict(t=40, b=20, l=20, r=20)
                )
                st.plotly_chart(fig, use_container_width=True)
        
        if len(numeric_cols) > 0:
            with col2:
                num_col = numeric_cols[0]
                fig = px.histogram(df_filtered, x=num_col, title=f"Distribution of {num_col}", nbins=30, color_discrete_sequence=['#3b82f6'])
                fig.update_layout(
                    paper_bgcolor='rgba(0,0,0,0)',
                    plot_bgcolor='rgba(0,0,0,0)',
                    font=dict(family="Inter", size=12),
                    title_font_size=16,
                    title_font_color='#1e293b',
                    xaxis=dict(showgrid=False),
                    yaxis=dict(showgrid=True, gridcolor='#e2e8f0'),
                    margin=dict(t=40, b=20, l=20, r=20)
                )
                st.plotly_chart(fig, use_container_width=True)
        
        st.markdown('</div>', unsafe_allow_html=True)
        
        col3, col4 = st.columns(2)
        with col3:
            st.markdown('<div class="chart-container">', unsafe_allow_html=True)
            if len(categorical_cols) > 1:
                cat_col2 = categorical_cols[1]
                cat_data2 = df_filtered[cat_col2].value_counts().head(10).reset_index()
                cat_data2.columns = [cat_col2, 'Count']
                fig = px.pie(cat_data2, names=cat_col2, values='Count', title=f"{cat_col2} Distribution", hole=0.45, color_discrete_sequence=['#3b82f6', '#10b981', '#f59e0b', '#8b5cf6', '#ec4899'])
                fig.update_layout(
                    paper_bgcolor='rgba(0,0,0,0)',
                    plot_bgcolor='rgba(0,0,0,0)',
                    font=dict(family="Inter", size=12),
                    title_font_size=16,
                    title_font_color='#1e293b',
                    margin=dict(t=40, b=20, l=20, r=20)
                )
                st.plotly_chart(fig, use_container_width=True)
            st.markdown('</div>', unsafe_allow_html=True)
        
        with col4:
            st.markdown('<div class="chart-container">', unsafe_allow_html=True)
            if len(date_cols) > 0:
                date_col = date_cols[0]
                time_data = df_filtered.groupby(df_filtered[date_col].dt.to_period('M')).size().reset_index()
                time_data.columns = ['Period', 'Count']
                time_data['Period'] = time_data['Period'].astype(str)
                fig = px.line(time_data, x='Period', y='Count', title=f"Trend Over Time ({date_col})", markers=True)
                fig.update_traces(line_color='#3b82f6', line_width=3, marker=dict(size=8))
                fig.update_layout(
                    paper_bgcolor='rgba(0,0,0,0)',
                    plot_bgcolor='rgba(0,0,0,0)',
                    font=dict(family="Inter", size=12),
                    title_font_size=16,
                    title_font_color='#1e293b',
                    xaxis=dict(showgrid=False),
                    yaxis=dict(showgrid=True, gridcolor='#e2e8f0'),
                    margin=dict(t=40, b=20, l=20, r=20)
                )
                st.plotly_chart(fig, use_container_width=True)
            st.markdown('</div>', unsafe_allow_html=True)
    
    with tab2:
        st.markdown('<div class="section-card">', unsafe_allow_html=True)
        st.markdown(
        '<div class="section-header"><h2 style="margin:0;">📈 Distributions & Statistical Analysis</h2></div>',
        unsafe_allow_html=True
    )

    if len(numeric_cols) > 0:
        col1, col2 = st.columns(2)

        with col1:
            selected_num = st.selectbox(
                "Select numeric column:",
                numeric_cols,
                key="dist_col"
            )

        with col2:
            chart_type = st.selectbox(
                "Chart type:",
                ["Histogram", "Box Plot", "Violin Plot"],
                key="chart_type"
            )

        # -------- Create Chart --------
        if chart_type == "Histogram":
            fig = px.histogram(
                df_filtered,
                x=selected_num,
                title=f"Distribution of {selected_num}",
                nbins=30,
                color_discrete_sequence=['#3b82f6']
            )

        elif chart_type == "Box Plot":
            fig = px.box(
                df_filtered,
                y=selected_num,
                title=f"Box Plot of {selected_num}",
                color_discrete_sequence=['#3b82f6']
            )

        else:
            fig = px.violin(
                df_filtered,
                y=selected_num,
                title=f"Violin Plot of {selected_num}",
                box=True,
                color_discrete_sequence=['#3b82f6']
            )

        fig.update_layout(
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            font=dict(family="Inter", size=12),
            title_font_size=16,
            title_font_color='#1e293b',
            xaxis=dict(showgrid=False),
            yaxis=dict(showgrid=True, gridcolor='#e2e8f0'),
            margin=dict(t=40, b=20, l=20, r=20)
        )

        # ✅ UNIQUE KEY FIX
        st.plotly_chart(
            fig,
            use_container_width=True,
            key=f"dist_chart_{selected_num}_{chart_type}"
        )

        st.markdown("### 📊 Statistical Summary")
        st.dataframe(
            df_filtered[numeric_cols].describe(),
            use_container_width=True
        )

    else:
        st.warning("⚠️ No numeric columns found")

    st.markdown('</div>', unsafe_allow_html=True)

    with tab3:
        st.markdown('<div class="section-card">', unsafe_allow_html=True)
        st.markdown('<div class="section-header"><h2 style="margin:0;">🔍 Relationship Analysis</h2></div>', unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        all_cols = numeric_cols + categorical_cols
        with col1:
            x_col = st.selectbox("X-axis:", all_cols, key="x_axis")
        with col2:
            y_col = st.selectbox("Y-axis:", all_cols, key="y_axis")
        
        if x_col and y_col:
            x_is_numeric = x_col in numeric_cols
            y_is_numeric = y_col in numeric_cols
            
            if x_is_numeric and y_is_numeric:
                color_col = st.selectbox("Color by (optional):", ["None"] + categorical_cols[:5], key="color_by")
                fig = px.scatter(df_filtered, x=x_col, y=y_col, color=None if color_col == "None" else color_col, title=f"{y_col} vs {x_col}", trendline="ols" if len(df_filtered) > 10 else None)
                fig.update_layout(
                    paper_bgcolor='rgba(0,0,0,0)',
                    plot_bgcolor='rgba(0,0,0,0)',
                    font=dict(family="Inter", size=12),
                    title_font_size=16,
                    title_font_color='#1e293b',
                    xaxis=dict(showgrid=True, gridcolor='#e2e8f0'),
                    yaxis=dict(showgrid=True, gridcolor='#e2e8f0'),
                    margin=dict(t=40, b=20, l=20, r=20)
                )
                st.plotly_chart(fig, use_container_width=True)
            elif not x_is_numeric and y_is_numeric:
                agg_data = df_filtered.groupby(x_col)[y_col].mean().sort_values(ascending=False).head(15).reset_index()
                fig = px.bar(agg_data, x=x_col, y=y_col, title=f"Average {y_col} by {x_col}", color=y_col, color_continuous_scale='Viridis')
                fig.update_layout(
                    paper_bgcolor='rgba(0,0,0,0)',
                    plot_bgcolor='rgba(0,0,0,0)',
                    font=dict(family="Inter", size=12),
                    title_font_size=16,
                    title_font_color='#1e293b',
                    xaxis=dict(showgrid=False),
                    yaxis=dict(showgrid=True, gridcolor='#e2e8f0'),
                    margin=dict(t=40, b=20, l=20, r=20)
                )
                st.plotly_chart(fig, use_container_width=True)
            else:
                try:
                    cross_tab = pd.crosstab(df_filtered[x_col], df_filtered[y_col])
                    fig = px.imshow(cross_tab, title=f"{x_col} vs {y_col}", labels=dict(x=y_col, y=x_col, color="Count"), color_continuous_scale='Blues')
                    fig.update_layout(
                        paper_bgcolor='rgba(0,0,0,0)',
                        plot_bgcolor='rgba(0,0,0,0)',
                        font=dict(family="Inter", size=12),
                        title_font_size=16,
                        title_font_color='#1e293b',
                        margin=dict(t=40, b=20, l=20, r=20)
                    )
                    st.plotly_chart(fig, use_container_width=True)
                except:
                    st.warning("Cannot create relationship chart for these columns")
        
        if len(numeric_cols) >= 2:
            st.markdown("### 🔗 Correlation Matrix")
            corr_matrix = df_filtered[numeric_cols].corr()
            fig = px.imshow(corr_matrix, title="Correlation Matrix", color_continuous_scale='RdBu', aspect="auto", labels=dict(color="Correlation"))
            fig.update_layout(
                paper_bgcolor='rgba(0,0,0,0)',
                plot_bgcolor='rgba(0,0,0,0)',
                font=dict(family="Inter", size=12),
                title_font_size=16,
                title_font_color='#1e293b',
                margin=dict(t=40, b=20, l=20, r=20)
            )
            st.plotly_chart(fig, use_container_width=True)
        
        st.markdown('</div>', unsafe_allow_html=True)



# ===================== FOOTER =====================

# ===================== AGE DISTRIBUTION =====================
with col2:
    if 'Age' in df_filtered.columns:
        age_bins = pd.cut(
            df_filtered['Age'],
            bins=[0, 30, 50, 70, 100],
            labels=['18-30', '31-50', '51-70', '70+']
        )

        age_data = age_bins.value_counts().sort_index().reset_index()
        age_data.columns = ['Age Group', 'Count']

        fig = px.bar(
            age_data,
            x='Age Group',
            y='Count',
            title="Age Distribution",
            color='Count',
            color_continuous_scale='Blues'
        )

        fig.update_layout(
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            font=dict(family="Inter", size=12),
            title_font_size=16,
            title_font_color='#1e293b',
            xaxis=dict(showgrid=False),
            yaxis=dict(showgrid=True, gridcolor='#e2e8f0'),
            margin=dict(t=40, b=20, l=20, r=20)
        )

        st.plotly_chart(fig, use_container_width=True)


# ===================== CITY & TREND CHARTS =====================
col3, col4 = st.columns(2)

with col3:
    st.markdown('<div class="chart-container">', unsafe_allow_html=True)

    if 'City' in df_filtered.columns:
        city_data = df_filtered['City'].value_counts().head(10).reset_index()
        city_data.columns = ['City', 'Patients']

        fig = px.bar(
            city_data,
            x='Patients',
            y='City',
            orientation='h',
            title="Top 10 Cities",
            color='Patients',
            color_continuous_scale='Viridis'
        )

        fig.update_layout(
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            font=dict(family="Inter", size=12),
            title_font_size=16,
            title_font_color='#1e293b',
            xaxis=dict(showgrid=True, gridcolor='#e2e8f0'),
            yaxis=dict(showgrid=False),
            margin=dict(t=40, b=20, l=20, r=20)
        )

        st.plotly_chart(fig, use_container_width=True)

    st.markdown('</div>', unsafe_allow_html=True)


with col4:
    st.markdown('<div class="chart-container">', unsafe_allow_html=True)

    if 'Registration_Date' in df_filtered.columns:
        monthly_data = (
            df_filtered
            .groupby(df_filtered['Registration_Date'].dt.to_period('M'))
            .size()
            .reset_index()
        )

        monthly_data.columns = ['Month', 'Patients']
        monthly_data['Month'] = monthly_data['Month'].astype(str)

        fig = px.line(
            monthly_data,
            x='Month',
            y='Patients',
            title="Registration Trend",
            markers=True
        )

        fig.update_traces(
            line_color='#3b82f6',
            line_width=3,
            marker=dict(size=8)
        )

        fig.update_layout(
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            font=dict(family="Inter", size=12),
            title_font_size=16,
            title_font_color='#1e293b',
            xaxis=dict(showgrid=False),
            yaxis=dict(showgrid=True, gridcolor='#e2e8f0'),
            margin=dict(t=40, b=20, l=20, r=20)
        )

        st.plotly_chart(fig, use_container_width=True)

    st.markdown('</div>', unsafe_allow_html=True)

# ========== EXPORT SECTION ==========
st.markdown('<div class="section-card">', unsafe_allow_html=True)
st.markdown('<div class="section-header"><h2 style="margin:0;">💾 Export Data</h2><span class="stats-badge">{:,} records</span></div>'.format(len(df_filtered)), unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    output = io.BytesIO()
    with pd.ExcelWriter(output, engine='openpyxl') as writer:
        df_filtered.to_excel(writer, sheet_name='Data', index=False)
        if len(numeric_cols) > 0:
            summary = df_filtered[numeric_cols].describe()
            summary.to_excel(writer, sheet_name='Statistics')
    st.download_button(
        "📥 Download Excel Report",
        output.getvalue(),
        f"data_export_{datetime.now().strftime('%Y%m%d_%H%M%S')}.xlsx",
        "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        use_container_width=True
    )

with col2:
    csv = df_filtered.to_csv(index=False)
    st.download_button(
        "📊 Download CSV",
        csv,
        f"filtered_data_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
        "text/csv",
        use_container_width=True
    )

st.markdown('</div>', unsafe_allow_html=True)


data_source_name = (
    uploaded_file.name
    if data_source == "Upload New CSV File" and 'uploaded_file' in locals() and uploaded_file
    else "Default Dataset"
)

st.markdown(
    f"""
    <div class="footer">
        <p style="font-weight: 600; color: white; margin-bottom: 8px;">
            Analytics Dashboard
        </p>
        <p style="margin: 0;">
            Powered by Streamlit + Power BI + Plotly • {len(df_filtered):,} records analyzed
               Developed by <strong>Nedient Technology Pvt. Ltd.</strong>
        </p>
        
        
        
    </div>
    """,
    unsafe_allow_html=True
)
