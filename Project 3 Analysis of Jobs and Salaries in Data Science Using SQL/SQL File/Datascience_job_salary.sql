CREATE TABLE Job (
	ID  INT primary KEY,
    work_year INT NOT NULL,
    job_title VARCHAR(255) NOT NULL,
    job_category VARCHAR(255),
    salary_currency VARCHAR(3) NOT NULL,
    salary DECIMAL(10, 2) NOT NULL,
    salary_in_usd DECIMAL(10, 2) NOT NULL,
    employee_residence VARCHAR(255) NOT NULL,
    experience_level VARCHAR(20) NOT NULL,
    employment_type VARCHAR(20) NOT NULL,
    work_setting VARCHAR(20) NOT NULL,
    company_location VARCHAR(255) NOT NULL,
    company_size VARCHAR(1) NOT NULL
);

SELECT * FROM Job;

-----checking for null value in each columns---------
SELECT
    COUNT(*) AS total_records,
    SUM(CASE WHEN work_year IS NULL THEN 1 ELSE 0 END) AS null_work_year,
    SUM(CASE WHEN job_title IS NULL THEN 1 ELSE 0 END) AS null_job_title,
    SUM(CASE WHEN job_category IS NULL THEN 1 ELSE 0 END) AS null_job_category,
    SUM(CASE WHEN salary_currency IS NULL THEN 1 ELSE 0 END) AS null_salary_currency,
    SUM(CASE WHEN salary IS NULL THEN 1 ELSE 0 END) AS null_salary,
    SUM(CASE WHEN salary_in_usd IS NULL THEN 1 ELSE 0 END) AS null_salary_in_usd,
    SUM(CASE WHEN employee_residence IS NULL THEN 1 ELSE 0 END) AS null_employee_residence,
    SUM(CASE WHEN experience_level IS NULL THEN 1 ELSE 0 END) AS null_experience_level,
    SUM(CASE WHEN employment_type IS NULL THEN 1 ELSE 0 END) AS null_employment_type,
    SUM(CASE WHEN work_setting IS NULL THEN 1 ELSE 0 END) AS null_work_setting,
    SUM(CASE WHEN company_location IS NULL THEN 1 ELSE 0 END) AS null_company_location,
    SUM(CASE WHEN company_size IS NULL THEN 1 ELSE 0 END) AS null_company_size
FROM job;


----1.	Find the average salary for each job category.-----------

SELECT 
      job_category,  
	   round(avg(salary),2) as average_salary, 
	   round(avg(salary_in_usd),2) as average_salary_in_usd
FROM 
     job
group by 
     job_category
order by 
     average_salary,average_salary_in_usd ;



-----2. Identify the top 5 countries with the highest average salary.-----------

SELECT 
      company_location, salary_currency, 
      round(avg(salary),2) as avg_salary , 
      round(avg(salary_in_usd),2) as avg_salary_in_usd
FROM
      job
group by 
       company_location, salary_currency
order by  
       avg_salary,avg_salary_in_usd
limit 5


------3. Retrieve the job title with the highest salary in each country.--------

With t1 as ( 
            SELECT job_title,salary,company_location,
	        ROW_NUMBER() OVER(partition by company_location order by salary DESC) as rank
	        FROM job)
SELECT 
       job_title,
       salary,
       company_location as country
FROM  t1
WHERE rank=1;

------4.Identify the top 3 job categories with the highest total salary in USD-------


SELECT 
       job_category,
       SUM(salary_in_usd) as Total_salary_usd
FROM
       job
GROUP BY   
       job_category
ORDER BY 
       Total_salary_usd desc
LIMIT 3;

--------5. Find the top 3 company location with the highest average salary for remote jobs-----------

SELECT 
      company_location,round(avg(salary),2) as avarage_salary
from  
      job
where 
      work_setting='Remote'
group by 
      company_location
order by   
      avarage_salary
limit 3



--6. Display a list of all job category and the total number of employees in each category in USA.
SELECT
    job_category,
	count(*) as Total_no_employee
FROM	 
      job
WHERE 
     company_location='United States'
Group by 
     job_category
ORDER BY
     total_no_employee DESC



----7. Find the highest salary job in each company_size in United States .------

WITH t1 AS (
	SELECT job_title,salary_in_usd,
       case
	   when company_size ='L' then 'Large'
	   when company_size='M'  then 'Medium'
	   else 'Small'
	   END AS company_size
FROM job
WHERE company_location='United States'),
     t2 as (
           select job_title,company_size,salary_in_usd,
	       DENSE_RANK() over(partition by company_size order by salary_in_usd) as rank
	       from t1
           )
SELECT company_size,job_title,salary_in_usd
from t2
where rank=1



--------8. Find the job title with the highest salary in each experience level category.--------

with t1 as (
	       SELECT job_title,salary_in_usd,experience_level,
           dense_rank() over( partition by experience_level order by salary_in_usd desc) as rank
           FROM job)
SELECT 
       experience_level,job_title, salary_in_usd
from   t1
where rank=1


----9.Find employee_id who work in Data Analyst job and have a higher salary than the average salary in different countries.
  
with t1 as (
	       SELECT * FROM job
           WHERE job_title='Data Analyst'),
     t2 as (
		  SELECT id as employee_id,salary,company_location,
          dense_rank()over(partition by company_location order by salary) as rank
          FROM t1
           WHERE salary > (select avg(salary) from t1))
SELECT  
      employee_id,salary,company_location
FROM t2
WHERE rank = 1


--10.Identify the job category with the highest average salary-to-experience ratio in India.----
 
With t1 as(
	  SELECT 
	       job_category,
	       round(avg(salary_in_usd)/COUNT(DISTINCT experience_level ),2) AS avg_salary_to_experience_ratio
	   FROM
	       Job
	   WHERE 
	       Company_location='India'
	   Group By 
	       job_category )
SELECT
      job_category, avg_salary_to_experience_ratio
FROM t1
ORDER BY avg_salary_to_experience_ratio DESC;
 
 
 
---11.List any 5 pairs of employees who have the same job category with a salary difference of less than $5,000.--

SELECT DISTINCT(j1.id,j2.id) as pairs_of_employee,
      j1.id as employee1_id,
	  j1.job_category,
	  j1.salary_in_usd as salary1,
	  j2.id as employee2_id,
	  j2.salary_in_usd as salary2
FROM 
    job j1
JOIN
    job j2
ON 
   j1.job_category=j2.job_category
   AND j1.id < j2.id
   AND ABS(j1.salary_in_usd-j2.salary_in_usd) < 5000
LIMIT 5	 



--  12.What is the average salary in USD for each job title within the 'Data Analysis' job category, and how does it compare to the overall average salary in USD across all job titles?

WITH DataAnalysisAvg AS (
    SELECT
        job_title,
        round(AVG(salary_in_usd),2) AS avg_salary_data_analysis
    FROM
        job
    WHERE
        job_category='Data Analysis'
    GROUP BY
        job_title),
		
OverallAvg AS (
    SELECT
        round(AVG(salary_in_usd),2) AS avg_salary_overall
    FROM
        job)
SELECT
    d.job_title,
    d.avg_salary_data_analysis,
    o.avg_salary_overall,
    round(d.avg_salary_data_analysis - o.avg_salary_overall,2) AS salary_difference
FROM
    DataAnalysisAvg d
CROSS JOIN
    OverallAvg o;


--13.Calculate the year-over-year percentage change in the average salary for each job category.

WITH t1 AS (
    SELECT
        work_year,
        job_category,
        round(AVG(salary_in_usd),2) AS avg_salary_in_usd,
        LAG(AVG(salary_in_usd)) OVER (PARTITION BY job_category ORDER BY work_year) AS prev_avg_salary
    FROM
        Job
    GROUP BY
        work_year, job_category
)
SELECT
    work_year,
    job_category,
    avg_salary_in_usd,
    CASE
        WHEN prev_avg_salary IS NULL THEN 0
        ELSE round(((avg_salary_in_usd - prev_avg_salary) / prev_avg_salary) * 100,2)
    END AS percentage_change 
FROM
    t1
ORDER BY
    job_category, work_year;



--14. Determine the median salary for Data engineering within each country.---


SELECT
    job_category,
    employee_residence AS country,
    PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY salary_in_usd) AS median_salary
FROM
    Job
WHERE
    job_category='Data Engineering'
GROUP BY
    job_category, country
ORDER BY
    job_category, country;


---15.List the job categories with the highest and lowest salary standard deviation in UK----

(SELECT
    job_category,
    round(STDDEV(salary_in_usd),2) AS salary_std_dev
FROM
    Job
WHERE 
     company_location = 'United Kingdom'
GROUP BY
    job_category
ORDER BY
    salary_std_dev DESC, job_category
LIMIT 1)

UNION ALL

(SELECT
    job_category,
    round(STDDEV(salary_in_usd),2) AS salary_std_dev
FROM
    Job
WHERE 
     company_location = 'United Kingdom'
GROUP BY
    job_category
ORDER BY
    salary_std_dev ASC, job_category
LIMIT 1);

