-- 02 DATA VALIDATION QUERIES
SELECT 'Total Records' AS Check, COUNT(*) AS Value FROM patients_master_clean;

SELECT 'Age Range' AS Check, MIN(Age) AS Min_Age, MAX(Age) AS Max_Age, AVG(Age) AS Avg_Age 
FROM patients_master_clean;

SELECT 'Attendance Stats' AS Check, 
    ROUND(AVG(Attendance_Rate_Fixed)*100,2) AS Avg_Attendance_Pct,
    COUNT(CASE WHEN Attendance_Rate_Fixed = 0 THEN 1 END) AS Zero_Attendance
FROM patients_master_clean;

SELECT 'Case Status Distribution' AS Check, Case_Status, COUNT(*) AS Count
FROM patients_master_clean 
GROUP BY Case_Status;
