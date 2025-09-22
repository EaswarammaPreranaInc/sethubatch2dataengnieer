CREATE DATABASE employees;
USE employees;

CREATE TABLE departments(
dept_no INT PRIMARY KEY,
dept_name VARCHAR(50) NOT NULL UNIQUE);

CREATE TABLE employees(
emp_no INT PRIMARY KEY,
birth_date DATE NOT NULL,
first_name VARCHAR(14) NOT NULL,
last_name VARCHAR(16) NOT NULL,
gender CHAR(1) NOT NULL CHECK(gender IN ('M','F')),
hire_date DATE NOT NULL,
dept_no INT,
email VARCHAR(100) UNIQUE,
salary DECIMAL(10,2),
CONSTRAINT fk_dept FOREIGN KEY(dept_no) REFERENCES departments(dept_no)
);



INSERT INTO departments(dept_no,dept_name) VALUES
(1,'HR'),
(2,'Finace'),
(3,'IT'),
(4,'sales');





INSERT INTO  employees(emp_no,birth_date,first_name,last_name,gender,hire_date,dept_no,email,salary) VALUES
(151,'1987-07-15','Jyothi','vone','F','2020-01-10',2,'jyothi.vone@example.com',65000.50),
(152,'1988-08-18','chiranjeevi','nani','M','2019-03-06',1,'chiranjeevi.nani@example.com',52000.55),
(153,'1990-05-16','venkatesh','sativada','M','2018-07-19',4,'venkatesh.sativada@example.com',45000.25),
(154,'1986-06-12','Thulasi','Thumala','F','2021-06-01',3,'Thulasi.Thumala@example.com',40000.00),
(155,'1992-02-25','karuna','Eruvada','F','2017-11-23',2,'karuna.Eruvada@example.com',75000.55);



-- 1.Show current date, time, and timestamp separately.
SELECT CURRENT_DATE();
SELECT CURRENT_TIME();
SELECT CURRENT_TIMESTAMP();

-- 2.Display each employee’s hire year, month number, and month name.
SELECT first_name,
YEAR(hire_date) AS Hire_year,
MONTH(hire_date) AS month_number,
MONTHNAME(hire_date) AS month_Name FROM employees;

-- 3.From which quarter each employee was hired in.
SELECT first_name,hire_date,
QUARTER(hire_date) AS Hire_Quarter FROM employees;



-- 4.Display hire dates with their corresponding week numbers.
SELECT first_name,hire_date,
WEEK(hire_date) AS hire_week FROM employees;


-- 5.Show the 200th day of the year 2025 using MAKEDATE.
 SELECT MAKEDATE(2025,200) AS Two_hundredth_day_2025;
 
 
 -- 6.Create a time value '09:15:00' using MAKETIME.
 SELECT MAKETIME(09,15,00) AS custom_time;
 
 -- 7.Find out the difference in time between '14:45:00' and '09:30:00'.
SELECT TIMEDIFF('14:45:00','09:15:00') AS time_diff;


-- 8.Convert '15/08/2025' into a proper date using STR_TO_DATE.
SELECT STR_TO_DATE('15-08-2025', '%d-%m-%Y') AS formatted_date;

-- 9.Show employee hire date and extract day, month, year separately.
SELECT first_name,hire_date,
DAY(hire_date) AS Day,
MONTH(hire_date) AS month,
YEAR(hire_date) AS year FROM employees;


-- 10.Find employees hired in the month of January.
SELECT first_name,hire_date FROM employees WHERE(hire_date)=1;


-- string functions
-- 1.Concatenate first name and last name into one column.
SELECT concat(first_name ,' ',last_name) AS full_name
FROM employees;

-- 2.Display first 3 characters of last name.
SELECT LEFT(last_name,3) AS lastName FROM employees;

-- 3.Show names in upper and lower case.
SELECT UPPER(first_name) AS UpperName,
LOWER(first_name) AS LowerName FROM employees;


-- 4.Find position of '@' in each email.
SELECT email,INSTR(email,'@') AS at_position
FROM employees;


-- 5.Replace domain 'example.com' with 'company.org'.
SELECT email,REPLACE(email,'example.com','company.org') AS email
FROM Employees;


-- 6.reverse the first name of each employee. 
SELECT first_name, REVERSE(first_name) AS reversed_name
FROM employees;


-- 7.Show the length of each employee email.
SELECT email,LENGTH(email) AS name_length
FROM employees;

-- 8.Trim spaces from 'SQL Practice'.
SELECT TRiM('  SQL practice  ') AS trimmed_text
FROM employees;

-- 9.Extract the last 4 characters from email addresses (domain)
SELECT email,RIGHT(email,4) AS last_char FROM employees;


-- 10.Display employees whose last name starts with 'S'.
SELECT last_name FROM employees WHERE last_name LIKE 'S%';


-- NUMERIC FUNCTIONS
-- 1.Show absolute value of -1000.
SELECT -1000 AS number,ABS(-1000) AS absoulte_value;


-- 2.find the ceiling and floor values of 123.45.
SELECT CEIL(123.45) AS ceil_value;
SELECT FLOOR(123.45) AS floor_value;

-- 3.Round the number 98.7654 to 2 decimals.
SELECT ROUND(98.7654,2) AS rounded_value;

-- 4.Show modulus when 55 is divided by 6
SELECT MOD(55,6) AS modulus_value;

-- 5.Find square root of 121.
SELECT SQRT(121) AS square_root;

-- 6.Raise 2 to the power of 8
SELECT POWER(2,8) AS power_value;

-- 7.find natural log and base-10 log of 1000.
SELECT LN(1000) AS natural_log,LOG10(1000) AS base_10_log;

-- 8.Display the sign of -45, 0, and 20
SELECT SIGN(-45),SIGN(0),SIGN(20);

-- 9.Show 3 random numbers between 0 and 1.
SELECT RAND() AS rand1,RAND() AS rand2,RAND() AS rand3;

-- 10.Find highest and lowest salary from employees table.
SELECT MAX(salary) AS max_salary,MIN(salary) AS min_salary
FROM employees;


-- 11.Display employee salary truncated to 2 decimals.
SELECT first_name,TRUNCATE(salary,2) AS sal FROM employees;

-- 12.Add a random bonus (between 500 and 2000) to each employee’s salary.
SELECT first_name,salary,salary+FLOOR(RAND()*(2000-500+1))+500 AS salary_bonus
FROM employees;




