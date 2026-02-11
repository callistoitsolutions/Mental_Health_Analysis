SELECT 'Total_Patients' AS KPI, COUNT(DISTINCT Patient_ID) AS Value FROM patients_master_clean;

SELECT 'New_vs_Returning' AS KPI, 
    COUNT(CASE WHEN Registration_Date > '2024-01-01' THEN 1 END) AS New_Patients,
    COUNT(CASE WHEN Registration_Date <= '2024-01-01' THEN 1 END) AS Returning_Patients
FROM patients_master_clean;

SELECT 'Avg_Session_Attendance' AS KPI, ROUND(AVG(Sessions_Attended)*1.0/AVG(Total_Sessions_Assigned)*100,2) AS Pct
FROM patients_master_clean;

SELECT 'Dropout_Rate' AS KPI, 
    ROUND(COUNT(CASE WHEN Case_Status = 'Dropped' THEN 1 END)*100.0/COUNT(*),2) AS Pct
FROM patients_master_clean;

-- PROVIDER KPIs
SELECT 'Sessions_Per_Provider' AS KPI, Provider_Name, COUNT(*) AS Sessions, 
    ROUND(AVG(Attendance_Rate_Fixed)*100,2) AS Avg_Attendance
FROM patients_master_clean 
GROUP BY Provider_Name 
ORDER BY Sessions DESC LIMIT 10;

-- OPERATIONAL KPIs
SELECT 'No_Show_Rate' AS KPI, 
    ROUND(COUNT(CASE WHEN Attendance_Rate_Fixed < 0.25 THEN 1 END)*100.0/COUNT(*),2) AS Pct
FROM patients_master_clean;
