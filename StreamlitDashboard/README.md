# 🧠 Mental Health Analytics Dashboard

A comprehensive Streamlit web application for analyzing mental health provider data, patient demographics, therapy outcomes, and provider performance.

## 📊 Features

- **Patient Demographics Analysis**: Gender, age distribution, geographic insights
- **Therapy Analytics**: Session tracking, completion rates, therapy type performance
- **Psychiatric Care Monitoring**: Risk level assessment, treatment success metrics
- **Substance Use Treatment**: Recovery progress tracking, program effectiveness
- **Provider Performance**: Workload analysis, quality metrics, burnout detection
- **Appointment Analytics**: No-show rates, peak scheduling patterns


 csv_path = Path(__file__).parent.parent / 'Dataset' / 'CleanedData' / 'patients_master_clean.csv'
## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Installation

1. **Clone or download this repository**

2. **Install dependencies:**
```bash
pip install -r requirements.txt
```

3. **Prepare your data:**
   - Place `patients_master_clean.csv` in the `data/` folder
   - Ensure the CSV has these columns:
     - Patient_ID, Patient_Name, Age, Gender, City
     - Registration_Date, Program_Type, Therapy_Type
     - Total_Sessions_Assigned, Sessions_Attended
     - Attendance_Rate, Provider_Name, Case_Status
     - Risk_Level, Satisfaction_Score

4. **Run the dashboard:**
```bash
streamlit run app.py
```

5. **Open your browser** to: `http://localhost:8501`

## 📁 Project Structure

```
MentalHealthStreamlitDashboard/
├── app.py                          # Main dashboard application
├── requirements.txt                # Python dependencies
├── data/
│   └── patients_master_clean.csv   # Patient data (3000+ records)
├── README.md                       # This file
└── .streamlit/
    └── config.toml                 # Streamlit configuration (optional)
```

## 📈 Dashboard Tabs

### 1. 📊 Patient Demographics
- Gender distribution pie chart
- Age group analysis
- Top cities by patient count
- Monthly registration trends

### 2. 🩺 Therapy Analytics
- Therapy type performance by status
- Average sessions by therapy type
- Completion rate analysis

### 3. 🏥 Psychiatric Care
- High-risk patient tracking
- Treatment success rates
- Risk level distribution

### 4. 💊 Substance Use Treatment
- Recovery progress monitoring
- Program completion rates
- Therapy effectiveness comparison

### 5. 👨‍⚕️ Provider Performance
- Patient load analysis
- Performance matrix (load vs quality)
- Provider ranking table

### 6. 📅 Appointments
- No-show rate tracking
- Monthly appointment heatmap
- City-wise attendance analysis

## 🔍 Using Filters

**Sidebar filters allow you to:**
- Select specific program types
- Filter by city (top 10 cities)
- Choose case status
- Filter by risk level

All charts update automatically based on your selections.

## 💾 Exporting Data

**Available export options:**
- 📥 Excel Report (includes summary sheet)
- 📊 Filtered CSV Data

Both exports include only the filtered data based on your current selections.

## 🎯 Key Metrics

The dashboard tracks these critical KPIs:
- **Total Patients**: Current patient count
- **Average Age**: Mean age of patients
- **Attendance Rate**: Session attendance percentage
- **Dropout Rate**: Percentage of dropped cases

## 🛠️ Customization

To customize the dashboard:

1. **Change colors**: Modify the color schemes in Plotly chart functions
2. **Add new metrics**: Create new calculations in the appropriate tab sections
3. **Modify filters**: Edit the sidebar filter options in the code

## 📱 Deployment

### Deploy to Streamlit Cloud (Free):

1. Push code to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect your repository
4. Deploy in 60 seconds!

### Local Network Sharing:

```bash
streamlit run app.py --server.address 0.0.0.0
```

Access from other devices: `http://YOUR_IP:8501`

## 🐛 Troubleshooting

**Issue**: "FileNotFoundError: data/patients_master_clean.csv"
- **Solution**: Ensure CSV file is in the `data/` folder

**Issue**: Charts not showing data
- **Solution**: Check that CSV columns match expected names

**Issue**: "ModuleNotFoundError"
- **Solution**: Run `pip install -r requirements.txt` again

## 📊 Sample Data Stats

Expected baseline metrics:
- Total Patients: ~3000
- Average Age: ~47 years
- Attendance Rate: ~52%
- Dropout Rate: ~28%

## 🤝 Contributing

To improve this dashboard:
1. Fork the repository
2. Create your feature branch
3. Submit a pull request

## 📝 License

This project is for educational/analytical purposes.

## 📧 Support

For issues or questions:
- Review this README
- Check Streamlit documentation: [docs.streamlit.io](https://docs.streamlit.io)
- Verify your data file format

## 🎓 Credits

Built with:
- Streamlit (Web framework)
- Plotly (Interactive charts)
- Pandas (Data processing)

---

**Last Updated**: January 2026
**Version**: 1.0.0