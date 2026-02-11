import pandas as pd
import numpy as np
from pathlib import Path

# ----------------------------
# LOAD RAW DATA
# ----------------------------
input_path = Path('Dataset/RawData/Mental_Health_Patients_Dataset_3000.xlsx')
df = pd.read_excel(input_path)

print("RAW DATA LOADED: Shape =", df.shape)
print("\nFirst 5 rows:")
print(df.head())

# ----------------------------
# STANDARDIZE COLUMNS
# ----------------------------
df.columns = [
    'Patient_ID', 'Patient_Name', 'Age', 'Gender', 'City', 
    'Registration_Date', 'Program_Type', 'Therapy_Type', 
    'Total_Sessions_Assigned', 'Sessions_Attended', 
    'Attendance_Rate', 'Provider_Name', 'Case_Status', 
    'Risk_Level', 'Satisfaction_Score'
]

# ----------------------------
# DATA CLEANING
# ----------------------------
print("\n=== CLEANING STARTED ===")

# 1. Fix Attendance Rate (remove % symbol, convert to decimal)
df['Attendance_Rate'] = df['Attendance_Rate'].astype(str).str.replace('%', '', regex=False).str.strip()
df['Attendance_Rate'] = pd.to_numeric(df['Attendance_Rate'], errors='coerce') / 100

# 2. Standardize Case Status
df['Case_Status'] = df['Case_Status'].astype(str).str.strip().str.title()
df['Case_Status'] = df['Case_Status'].replace({
    'Inprogress': 'In Progress', 'Activecase': 'Active'
})

# 3. Standardize Gender
df['Gender'] = df['Gender'].astype(str).str.strip().str.title()
df['Gender'] = df['Gender'].replace({'Othergender': 'Other', 'F': 'Female', 'M': 'Male'})

# 4. Fix City names
df['City'] = df['City'].astype(str).str.strip().str.title()

# 5. Convert dates
df['Registration_Date'] = pd.to_datetime(df['Registration_Date'], errors='coerce')

# 6. Remove null rows (Age, Sessions critical)
df_clean = df.dropna(subset=['Age', 'Total_Sessions_Assigned', 'Sessions_Attended'])

# 7. Fix negative sessions (data error)
df_clean.loc[df_clean['Sessions_Attended'] > df_clean['Total_Sessions_Assigned'], 
             'Sessions_Attended'] = df_clean['Total_Sessions_Assigned']

# 8. Recalculate attendance if invalid
df_clean['Attendance_Rate_Fixed'] = df_clean['Sessions_Attended'] / df_clean['Total_Sessions_Assigned']

# ----------------------------
# CLEANING SUMMARY
# ----------------------------
print("\nCLEANING SUMMARY:")
print(f"Rows before: {len(df)}, after: {len(df_clean)}")
print(f"Missing Age: {df['Age'].isna().sum()}, Sessions: {df['Sessions_Attended'].isna().sum()}")

# ----------------------------
# SAVE CLEAN DATA
# ----------------------------
output_dir = Path('Dataset/CleanedData')
output_dir.mkdir(parents=True, exist_ok=True)  # create folder if not exists

output_path = output_dir / 'patients_master_clean.csv'
df_clean.to_csv(output_path, index=False)
print(f"\n✅ CLEAN DATA SAVED: {output_path}")

# ----------------------------
# QUICK STATS FOR VALIDATION
# ----------------------------
print("\n📊 CLEAN DATA STATS:")
print(f"Total Patients: {len(df_clean)}")
print(f"Avg Age: {df_clean['Age'].mean():.1f}")
print(f"Avg Attendance: {df_clean['Attendance_Rate_Fixed'].mean():.1%}")
print(f"Case Status: {df_clean['Case_Status'].value_counts().to_dict()}")
