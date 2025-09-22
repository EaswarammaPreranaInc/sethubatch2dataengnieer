
CREATE DATABASE employees;

USE employees;

-- Date and time

CREATE TABLE departments (
    dept_no     INT PRIMARY KEY,
    dept_name   VARCHAR(50) NOT NULL UNIQUE
);


CREATE TABLE employees(
emp_no      INT PRIMARY KEY,
birth_date  DATE NOT NULL,
first_name  VARCHAR(14) NOT NULL,
last_name   VARCHAR(16) NOT NULL,
gender      CHAR(1) NOT NULL CHECK (gender IN ('M', 'F')),
hire_date   DATE NOT NULL,
dept_no     INT,
CONSTRAINT fk_dept FOREIGN KEY (dept_no) REFERENCES departments(dept_no));


INSERT INTO departments (dept_no, dept_name) 
VALUES (1, 'HR'), 
       (2, 'Finance'), 
       (3, 'IT');

INSERT INTO employees (emp_no, birth_date, first_name, last_name, gender, hire_date, dept_no)
VALUES (101, '1994-08-05', 'v', 'Thapaswi', 'F', '2020-05-10', 3),
       (102, '2002-07-12', 'V', 'Akhil', 'M', '2021-06-09', 2),
       (103, '2000-06-07', 'E', 'Karuna', 'F', '2024-07-08', 1);
       
-- 1.CURRENT DATE
SELECT CURRENT_DATE();

-- CURRENT TIME
SELECT CURRENT_TIME();

-- CURRENT TIMESTAMP : returns current date and time
SELECT CURRENT_TIMESTAMP();

-- 2.Display each employee's hire year, month number, and month name.
SELECT first_name, 
YEAR(hire_date) AS Hire_Year, 
MONTH(hire_date) AS Month_Number,
MONTHNAME(hire_date) AS Month_Name FROM employees;

-- 3. From which quarter each employee was hired in.
SELECT first_name, hire_date, 
QUARTER(hire_date) AS Hire_Quarter from employees;

-- 4. Display hire dates with their corresponding week numbers.
SELECT first_name, hire_date,
WEEK(hire_date) AS Hire_week from employees;

-- 5. show the 200th day of the year 2025 using MAKEDATE
SELECT MAKEDATE(2025,200) AS Two_hundredth_day_2025;

-- 6. create a time value '09:15:00' using MAKETIME
SELECT MAKETIME(9,15,0) AS Custom_time;

-- 7. Find  out the difference in time between '14:45:00' and '09:30:00'
SELECT TIMEDIFF('14:45:00' , '09:30:00') AS Time_diff;

-- 8.convert '15/08/2025' into a proper date using STR_TO_DATE
SELECT STR_TO_DATE('15-08-2025', '%d-%m-%Y') AS formatted_date;

-- 9.show employee hire date and extract day, month, year separately
SELECT first_name, hire_date,
DAY(hire_date) AS Day , 
MONTH(hire_date) AS Month,
YEAR(hire_date) AS Year from employees;

-- 10. find employees hired in the month of january
SELECT first_name, hire_date FROM employees WHERE MONTH(hire_date) =1;

-- Numeric functions

use employees_db;

-- 1.show absolute value of -1000
select ABS(-1000) AS absolute_value;

-- 2. Find the ceiling and floor values of 123.45
select CEIL(123.45) AS ceil_value ,FLOOR(123.45) AS Floor_value;

-- 3. Round the number 98.7654 to 2 decimals
select ROUND(98.7654) as Rounded_value;

-- 4. show modules when 55 is divided by 6
select MOD(55,6) as modulus_value;

-- 5. Find square root of 121 
select SQRT(121) AS sqrt;

-- 6. Raise 2 to the power of 8
select POW(2,8) AS power_val;

-- 7. Find natural log and base -10 log of 1000
select LN(1000) as natural_log , LOG10(1000) as Base_10_log;

-- 8. Display the sign of -45, 0 and 20
select SIGN(-45) as sign1 , SIGN(0) as sign2, SIGN(20) as sign3;

-- 9. Show 3 random numbers between 0 and 1 
select RAND() as rand1 , RAND() as rand2 , RAND() as rand3;

-- 10. Find highest and lowest salary from employees table 
select MAX(salary) AS max_salary, MIN(salary) as min_salary from employees;

-- 11. Display employee salary truncated to 2 decimals
select first_name, TRUNCATE(salary,2) As  Sal from employees;

-- 12. Add a bonus(between 500 and 2000) to each employee's salary
select first_name,salary,salary+FLOOR(RAND()*(2000-500+1))+500 AS salary_bonus from employees;

-- string functions

CREATE DATABASE employees_db;

USE employees_db;

CREATE TABLE departments (
dept_no INT PRIMARY KEY,
dept_name VARCHAR(50) NOT NULL UNIQUE);

CREATE TABLE employees (
emp_no INT PRIMARY KEY,
birth_date DATE NOT NULL,
first_name VARCHAR(14) NOT NULL,
last_name VARCHAR(16) NOT NULL,
gender CHAR(1) NOT NULL CHECK (gender IN ('M','F')),
hire_date DATE NOT NULL,
dept_no INT,
email VARCHAR(100) UNIQUE,
salary DECIMAL(10,2),
CONSTRAINT fk_dept FOREIGN KEY (dept_no) REFERENCES departments(dept_no)
);


INSERT INTO departments (dept_no, dept_name) VALUES
(1, 'HR'),
(2, 'Finance'),
(3, 'IT'),
(4, 'Sales');


INSERT INTO employees (emp_no, birth_date, first_name, last_name, gender, hire_date, dept_no, email, salary) VALUES
(101, '1997-06-15', 'Aarav', 'Mehta', 'M', '2020-01-10', 1, 'aarav.mehta@example.com', 55000.75),
(102, '1995-09-22', 'Ananya', 'Reddy', 'F', '2019-03-05', 2, 'ananya.reddy@example.com', 72000.50),
(103, '1998-12-11', 'Rohan', 'Mishra', 'M', '2018-07-19', 3, 'rohan.mishra@example.com', 68000.00),
(104, '1997-04-08', 'Radya', 'Iyer', 'F', '2021-06-01', 4, 'Radya.iyer@example.com', 48000.20),
(105, '1992-02-25', 'Devansh', 'Dixit', 'M', '2017-11-23', 3, 'devansh.dixit@example.com', 89000.90);

-- 1.concatenate first name and last name into one column
SELECT CONCAT(first_name,' ',last_name) As Name FROM employees;

-- 2.Display first 3 characters of last name
SELECT LEFT(last_name,3) AS LastName FROM employees;

-- 3. show names in upper and lower case 
SELECT UPPER(first_name) AS UpperName,
LOWER(first_name) AS LowerName from employees;

-- 4.find position of '@' in each email
SELECT email, INSTR(email, '@') AS at_position
FROM employees;

-- 5. replace domain 'example.com' with 'company.org'
SELECT email, 
REPLACE(email,'example.com','company.org') AS Email 
from employees;


-- 6.reverse the first name of each employee
SELECT first_name, REVERSE(first_name) As reversed_First_name FROM employees;

-- 7.show the length of each emoloyee eamail
SELECT first_name, LENGTH(first_name) AS first_name_length FROM employees;

-- 8.Trim spaces from 'SQL Practice'
SELECT TRIM('  SQL PRACTICE  ') AS trimmed_text;

-- 9.Extract the last 4 characters from email addresses(domain)
SELECT email, RIGHT(email,4) AS Last_char from employees;

-- 10.Display employees whose last name starts with 'S'
SELECT last_name from employees where last_name like 'S%';



