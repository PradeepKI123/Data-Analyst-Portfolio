

--Retrieve the total number of admissions for each medical condition.

SELECT 
     medicalcondition,
	 count(*) as total_admissions
FROM
    health
GROUP BY 
   medicalcondition;
   
--Find the average billing amount for patients in each age group (e.g., 0-10, 11-20, etc.).
SELECT
      CASE
	      WHEN age between 0 AND 10 THEN '0-10'
		  WHEN age between 11 AND 20 THEN '11-20'
		  WHEN age between 21 AND 30 THEN '21-30'
		  WHEN age between 31 AND 40 THEN '31-40'
		  WHEN age between 41 AND 50 THEN '41-50'
		  WHEN age between 51 AND 60 THEN '51-60'
		  else 'greater than 60'
	   END AS Age_group,
	   AVG(billingamount) as average_billingamount
FROM
    health
GROUP BY
    Age_group
ORDER BY
    Age_group desc

--List the top 3 most common blood types among patients.
SELECT
     bloodtype as Blood_group,
     COUNT(*) as Number_of_patirnts
FROM
   health
GROUP BY
      Blood_group
ORDER BY
      Number_of_patirnts desc
LIMIT 3
 



--Find the 3 medical condition with the highest average billing amount.

SELECT
      medicalcondition,
	  avg(billingamount) as average_billingamount
from
    health
GROUP BY 
     medicalcondition
ORDER BY
     average_billingamount desc
LIMIT 3


--Retrieve the names of doctors who have treated patients in more than one hospital.

SELECT 
      doctor,
	  COUNT(DISTINCT hospital) as number_of_hospital
from 
    health
GROUP BY
    doctor
HAVING 
     COUNT(DISTINCT hospital)>1
LIMIT 10;

     
--Identify patients who have undergone both normal and abnormal tests.

SELECT
    name,
    COUNT(DISTINCT CASE WHEN testresults = 'Normal' THEN TestResults END) AS NormalTests,
    COUNT(DISTINCT CASE WHEN testresults = 'Abnormal' THEN TestResults END) AS AbnormalTests
FROM
    Health
WHERE
    testresults IN ('Normal', 'Abnormal')
GROUP BY
    name
HAVING
    COUNT(DISTINCT CASE WHEN testresults = 'Normal' THEN TestResults END) > 0
    AND COUNT(DISTINCT CASE WHEN testresults = 'Abnormal' THEN TestResults END) > 0
LIMIT 10

--List the hospitals where the majority of admissions are elective.

SELECT
    Hospital,
    COUNT(*) AS TotalAdmissions,
    SUM(CASE WHEN AdmissionType = 'Elective' THEN 1 ELSE 0 END) AS ElectiveAdmissions,
    ROUND((SUM(CASE WHEN AdmissionType='Elective' THEN 1 ELSE 0 END)*100.0)/COUNT(*))AS PercentageElectiveAdmissions
FROM
    Health  
GROUP BY
    Hospital
HAVING
    (SUM(CASE WHEN AdmissionType = 'Elective' THEN 1 ELSE 0 END) * 100.0) / COUNT(*) > 50
LIMIT 10

--Identify patients with the longest and shortest lengths of stay in the hospital.

(SELECT
    Name,
    Dateofadmission,
    DischargeDate,
    (DischargeDate - DateOfAdmission) AS LengthOfStay
FROM
    Health
ORDER BY
    LengthOfStay DESC
LIMIT 1)

UNION

(SELECT
    Name,
    DateOfAdmission,
    DischargeDate,
    (DischargeDate - DateOfAdmission) AS LengthOfStay
FROM
    Health
ORDER BY
    LengthOfStay ASC
LIMIT 1)

--Find the top 5 hospitals where the billing amount has increased the most compared to the previous year.
WITH BillingAmountChanges AS (
    SELECT
        Hospital,
        EXTRACT(YEAR FROM DateOfAdmission) AS AdmissionYear,
        SUM(BillingAmount) AS TotalBillingAmount
    FROM
        Health
    GROUP BY
        Hospital, EXTRACT(YEAR FROM DateOfAdmission)
)

SELECT
    Hospital,
    MAX(TotalBillingAmount) AS MaxBillingAmount,
    MIN(TotalBillingAmount) AS MinBillingAmount,
    MAX(TotalBillingAmount) - MIN(TotalBillingAmount) AS BillingAmountIncrease
FROM
    BillingAmountChanges
GROUP BY
    Hospital
ORDER BY
    BillingAmountIncrease DESC
LIMIT 5;

--List the medical conditions where the average age of patients is below the overall average age.

WITH AverageAgeByCondition AS (
    SELECT
        MedicalCondition,
        ROUND(AVG(Age)) AS AverageAge
    FROM
        Health
    GROUP BY
        MedicalCondition
)

SELECT
    MedicalCondition,
    AverageAge
FROM
    AverageAgeByCondition
WHERE
    AverageAge < (SELECT AVG(Age) FROM Health);



--Identify the patients with the highest and lowest billing amounts within their respective medical conditions.

WITH RankedBilling AS (
  SELECT
    Name,
    Medicalcondition,
    Billingamount,
    RANK() OVER (PARTITION BY Medicalcondition ORDER BY Billingamount DESC) AS Billing_Rank_Highest,
    RANK() OVER (PARTITION BY Medicalcondition ORDER BY Billingamount ASC) AS Billing_Rank_Lowest
  FROM
    Health
)
SELECT
  Name,
  Medicalcondition,
  Billingamount,
  'Highest' AS Billing_Rank_Type
FROM
  RankedBilling
WHERE
  Billing_Rank_Highest = 1

UNION

SELECT
  Name,
  Medicalcondition,
  Billingamount,
  'Lowest' AS Billing_Rank_Type
FROM
  RankedBilling
WHERE
  Billing_Rank_Lowest = 1;


--Find pairs of patients who share the same room number and calculate the average age of each pair.

SELECT
    P1.Name AS Patient1,
    P2.Name AS Patient2,
    P1.Roomnumber,
    ROUND(AVG((P1.Age + P2.Age) / 2))AS AverageAgeOfPair
FROM
   Health P1
JOIN
    Health P2 ON P1.Roomnumber = P2.Roomnumber AND P1.Name < P2.Name
GROUP BY
    P1.Name, P2.Name, P1.Roomnumber
ORDER BY
    P1.Roomnumber, P1.Name, P2.Name
LIMIT 10;


