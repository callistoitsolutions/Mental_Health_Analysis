USE mentalhealthanalytics;

-- Standardize status formats
UPDATE patients_master_clean 
SET Case_Status = 'In Progress' 
WHERE Case_Status LIKE '%inprogress%' OR Case_Status LIKE '%active%';

UPDATE patients_master_clean 
SET Gender = 'Other' 
WHERE Gender NOT IN ('Male', 'Female');

-- Remove outliers (Age > 100 or < 0)
DELETE FROM patients_master_clean 
WHERE Age > 100 OR Age < 0;

-- Fix attendance rates > 100%
UPDATE patients_master_clean 
SET Attendance_Rate_Fixed = 1.0 
WHERE Attendance_Rate_Fixed > 1.0;

