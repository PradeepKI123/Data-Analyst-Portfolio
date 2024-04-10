CREATE TABLE Employee_office_survey (
    emp_id INT ,
    off_cde VARCHAR(10),
    rated_year INT,
    rating FLOAT
);


CREATE TABLE HR_Employee (
    EmployeeID INT PRIMARY KEY,
    JoiningYear INT,
    Age INT,
    BusinessTravel VARCHAR(50),
    DailyRate INT,
    Department VARCHAR(50),
    DistanceFromHome INT,
    EducationField VARCHAR(50),
    EmployeeCount INT,
    EmployeeNumber INT,
    EnvironmentSatisfaction INT,
    Gender VARCHAR(10),
    HourlyRate INT,
    JobInvolvement INT,
    JobSatisfaction INT,
    MaritalStatus VARCHAR(20),
    MonthlyIncome INT,
    MonthlyRate INT,
    NumCompaniesWorked INT,
    Over18 VARCHAR(5),
    OverTime VARCHAR(5),
    PercentSalaryHike INT,
    PerformanceRating INT,
    RelationshipSatisfaction INT,
    StandardHours INT,
    StockOptionLevel INT,
    TotalWorkingYears INT,
    TrainingTimesLastYear INT,
    WorkLifeBalance INT,
    YearsAtCompany INT,
    YearsInCurrentRole INT,
    YearsSinceLastPromotion INT,
    YearsWithCurrManager INT,
    Attrition VARCHAR(5),
    LeavingYear INT,
    Reason VARCHAR(100),
    RelievingStatus VARCHAR(50),
    office_code VARCHAR(10),
    JobLevel_updated VARCHAR(2)
);


CREATE TABLE Job_position_structure (
    Department VARCHAR(50),
    JobLevel VARCHAR(10),
    JobRole VARCHAR(50),
    PRIMARY KEY (Department, JobLevel)
);

CREATE TABLE Office_code (
    office_code VARCHAR(10),
    city VARCHAR(50),
    province VARCHAR(50),
    country VARCHAR(50)
);

select * from employee_office_survey
select * from hr_employee
select * from job_position_structure
select * from office_code


--1.Find the average age of employees who left the organization in each department.
SELECT
       department,
	   ROUND(AVG(age)) as Average_age
FROM
    hr_employee
GROUP BY
    department
	
	
--2. List the top 5 departments with the highest average job satisfaction among employees who have 
--not received a promotion in the last 3 years.


SELECT Department, 
       ROUND(AVG(JobSatisfaction),2) AS AvgJobSatisfaction
FROM
     HR_Employee
WHERE
     YearsSinceLastPromotion > 3
GROUP BY
     Department
ORDER BY 
     AvgJobSatisfaction DESC
LIMIT 5;


--3. Determine the percentage of employees who left the organization due to various reasons.

SELECT 
    Reason,
    ROUND(100.0 * COUNT(*) / (SELECT COUNT(*) FROM HR_Employee WHERE Attrition = 'Yes'),2) AS Percentage
FROM 
    HR_Employee
WHERE 
    Attrition = 'Yes'
GROUP BY 
    Reason
ORDER BY 
    Percentage DESC;

--4. Find the three office location with the highest average distance from home for employees who work overtime

SELECT 
    oc.city,
    oc.province,
    oc.country,
    ROUND(AVG(e.DistanceFromHome),2) AS AvgDistanceFromHome
FROM 
    HR_Employee e
INNER JOIN 
    Office_code oc ON e.office_code = oc.office_code
WHERE 
    e.OverTime = 'Yes'
GROUP BY 
    oc.city,
    oc.province,
    oc.country
ORDER BY 
    AvgDistanceFromHome DESC
LIMIT 3;


--5.Find the employees with the highest monthly income in each department.

WITH RankedEmployees AS (
    SELECT 
        EmployeeID,
        Department,
        MonthlyIncome,
        ROW_NUMBER() OVER (PARTITION BY Department ORDER BY MonthlyIncome DESC) AS Rank
    FROM 
        HR_Employee
)
SELECT 
    EmployeeID,
    Department,
    MonthlyIncome
FROM 
    RankedEmployees
WHERE 
    Rank <= 1;


--6. Which department has the highest and lowest attrition rates?

SELECT
    Department,
    COUNT(CASE WHEN Attrition = 'Yes' THEN 1 END) AS Attrition_Count,
    COUNT(*) AS Total_Count,
    (100 * COUNT(CASE WHEN Attrition = 'Yes' THEN 1 END) / COUNT(*))  AS Attrition_Rate
FROM
    HR_Employee
GROUP BY
    Department
ORDER BY
    Attrition_Rate DESC;
	

--7. Do married employees have a lower attrition rate compared to single or divorced employees?

SELECT
    MaritalStatus,
    COUNT(CASE WHEN Attrition = 'Yes' THEN 1 END) AS Attrition_Count,
    COUNT(*) AS Total_Count,
    (COUNT(CASE WHEN Attrition = 'Yes' THEN 1 END) * 100 / COUNT(*))  AS Attrition_Rate
FROM
    HR_Employee
GROUP BY
    MaritalStatus
ORDER BY 
   Attrition_Rate DESC;


--8.Identify the top three office locations with the highest average performance ratings for employees who joined the organization 
--in the past three years.
WITH Employee_Performance AS (
    SELECT
        e.emp_id,
        e.off_cde,
        e.rated_year,
        e.rating,
        ROW_NUMBER() OVER (PARTITION BY e.emp_id ORDER BY e.rated_year DESC) AS row_num
    FROM
        Employee_office_survey e
    WHERE
        e.rated_year BETWEEN 2020 AND 2022 
)
SELECT
    oc.city,
    oc.province,
    oc.country,
    ROUND(AVG(ep.rating)::numeric,2) AS avg_performance_rating
FROM
    Office_code oc
JOIN
    Employee_Performance ep ON oc.office_code = ep.off_cde
WHERE
    ep.row_num = 1 
GROUP BY
    oc.city,
    oc.province,
    oc.country
ORDER BY
    avg_performance_rating DESC
LIMIT 3;


--9. What is the average monthly income of employees, grouped by their job level, within each department?


SELECT 
    department,
	ROUND(AVG(CASE WHEN joblevel_updated = 'L1' THEN monthlyincome ELSE 0 END ),2) AS Joblevel_L1,
	ROUND(AVG(CASE WHEN joblevel_updated = 'L2' THEN monthlyincome ELSE 0 END ),2)AS Joblevel_L2,
	ROUND(AVG(CASE WHEN joblevel_updated = 'L3' THEN monthlyincome ELSE 0 END ),2) AS Joblevel_L3,
	ROUND(AVG(CASE WHEN joblevel_updated = 'L4' THEN monthlyincome ELSE 0 END ),2) AS Joblevel_L4,
	ROUND(AVG(CASE WHEN joblevel_updated = 'L5' THEN monthlyincome ELSE 0 END ),2) AS Joblevel_L5,
	ROUND(AVG(CASE WHEN joblevel_updated = 'L6' THEN monthlyincome ELSE 0 END ),2) AS Joblevel_L6,
	ROUND(AVG(CASE WHEN joblevel_updated = 'L7' THEN monthlyincome ELSE 0 END ),2) AS Joblevel_L7
FROM 
   Hr_employee
GROUP BY
   department
   
   
--10. How many employees hold a degree different city, categorized by their education field

SELECT 
   oc.city,
   oc.country,
   COUNT(CASE WHEN hr.educationfield = 'Diploma' THEN 1 ELSE 0 END ) AS Diploma,
   COUNT(CASE WHEN hr.educationfield = 'Doctorate' THEN 1 ELSE 0 END ) AS Doctorate,
   COUNT(CASE WHEN hr.educationfield = 'Bachelors' THEN 1 ELSE 0 END ) AS Bachelors,
   COUNT(CASE WHEN hr.educationfield = 'Masters' THEN 1 ELSE 0 END ) AS Masters
FROM
   HR_employee hr
INNER JOIN
   office_code oc ON hr.office_code = oc.office_code
GROUP BY
   oc.city,
   oc.country
ORDER BY
   oc.country ASC
  

