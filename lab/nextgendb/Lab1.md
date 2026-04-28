# Lab 1: PostgresSQL

## Step 1: Create Table

### Commands
```bash
CREATE TABLE Patients (
    PatientID     SERIAL PRIMARY KEY,
    Name          VARCHAR(100) NOT NULL,
    Age           INT,
    Gender        CHAR(1),
    AdmissionDate DATE,
    DoctorID      INT REFERENCES Doctors(DoctorID)
);

CREATE TABLE Doctors (
    DoctorID       SERIAL PRIMARY KEY,
    Name           VARCHAR(100) NOT NULL,
    Specialization VARCHAR(100),
    Experience     INT  -- years
);
```

## Step 2: Insert Values

### Commands
```bash
INSERT INTO Doctors (Name, Specialization, Experience) VALUES
('Dr. Arjun Mehta',   'Cardiology',    12),
('Dr. Priya Nair',    'Neurology',      8),
('Dr. Ravi Sharma',   'Cardiology',    15),
('Dr. Sunita Rao',    'Orthopedics',    5);

INSERT INTO Patients (Name, Age, Gender, AdmissionDate, DoctorID) VALUES
('Rahul Gupta',    45, 'M', '2024-06-15', 1),
('Ananya Singh',   30, 'F', '2024-06-15', 2),
('Vikram Patel',   60, 'M', '2024-05-20', 1),
('Meena Joshi',    25, 'F', '2024-07-01', 3),
('Suresh Kumar',   55, 'M', '2024-06-15', 4);
```

## Step 3: Fetch all Patient details

### Commands
```bash
SELECT * FROM Patients;
```

## Step 4: Patients admitted on 2024-06-15

### Commands
```bash
SELECT *
FROM Patients
WHERE AdmissionDate = '2024-06-15';
```

## Step 5: Patients by age group

### Commands
```bash
SELECT
    CASE
        WHEN Age < 18             THEN 'Minor (<18)'
        WHEN Age BETWEEN 18 AND 35 THEN 'Young Adult (18–35)'
        WHEN Age BETWEEN 36 AND 60 THEN 'Middle-Aged (36–60)'
        ELSE                           'Senior (60+)'
    END AS AgeGroup,
    COUNT(*) AS PatientCount
FROM Patients
GROUP BY AgeGroup
ORDER BY AgeGroup;
```

## Step 6: Update Patient Name (PatientID = 1)

### Commands
```bash
UPDATE Patients
SET Name = 'Rahul R. Gupta'
WHERE PatientID = 1;
```

## Step 7: Doctors by Specialization (Cardiology)

### Commands
```bash
SELECT *
FROM Doctors
WHERE Specialization = 'Cardiology';
```


## Step 8: Count Patients per doctor

### Commands
```bash
SELECT
    d.DoctorID,
    d.Name           AS DoctorName,
    COUNT(p.PatientID) AS TotalPatients
FROM Doctors d
LEFT JOIN Patients p ON d.DoctorID = p.DoctorID
GROUP BY d.DoctorID, d.Name
ORDER BY TotalPatients DESC;
```


## Step 9: Average experience of doctors

### Commands
```bash
SELECT ROUND(AVG(Experience), 2) AS AvgExperienceYears
FROM Doctors;
```