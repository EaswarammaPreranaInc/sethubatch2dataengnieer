CREATE DATABASE company_db;
USE company_db;

CREATE TABLE employees (
    emp_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    department VARCHAR(50),
    hire_date DATE,
    email VARCHAR(100),
    salary DECIMAL(10,2)
);
drop table employees;

INSERT INTO employees (first_name, last_name, department, hire_date, email, salary) VALUES
('Arun', 'Vasa', 'IT', '2021-06-15', 'arun.vasa@example.com', 55000.00),
('Priya', 'Sharma', 'HR', '2020-03-10', 'priya.sharma@example.com', 48000.00),
('Rahul', 'Patel', 'Finance', '2019-11-25', 'rahul.patel@example.com', 60000.00),
('Neha', 'Reddy', 'IT', '2022-01-05', 'neha.reddy@example.com', 53000.00),
('Kiran', 'Singh', 'Marketing', '2023-07-20', 'kiran.singh@example.com', 45000.00);

-- Date & Time Functions
-- 1 Show current date, time, and timestamp separately.
Select current_date() As Today_Date,current_time() as Today_Time,current_timestamp() as Today_Timestamp;
-- 2  Display each employee’s hire year, month number, and month name
Select first_name,last_name, Year(hire_date) as Year,Month(hire_date) as Month,monthname(hire_date) as MonthName from employees;
-- 3 Find which quarter each employee was hired in.
Select first_name,last_name,hire_date,quarter(hire_date) as Quarter from employees;
-- 4 Display hire dates with their corresponding week numbers.
Select first_name,last_name,hire_date,week(hire_date) as week from employees;
-- 5 Show the 200th day of the year 2025 using MAKEDATE.
select makedate(Year(now()),200) as '200th day of the present year';
-- 6  Create a time value '09:15:00' using MAKETIME.
select maketime(09,15,00) as 'Time chnage';
-- 7 Find out the difference in time between '14:45:00' and '09:30:00'.
select timediff('14:45:00',  '09:30:00') as Timediff;
-- 8 Convert '15/08/2025' into a proper date using STR_TO_DATE.
select str_to_date("15,08,2025","%d,%m,%y") as date;
-- 9 Show employee hire date and extract day, month, year separately.
Select first_name,last_name, Day(hire_date) as Day,Month(hire_date) as Month,Year(hire_date) as Year from employees;
-- 10 Find employees hired in the month of January.
Select first_name,last_name,monthname(hire_date) as monthname from employees  where monthname(hire_date) ='January';

--------------------------------
-- String Functions
-- 1 Concatenate first name and last name into one column.
select concat(first_name,last_name) as Full_Name from employees;
-- 2 Display first 3 characters of last name.
Select last_name,mid(last_name,-3) as 'last 3 charcters' from employees;
 -- 3 Show names in upper and lower case.
 select Upper(concat(first_name,last_name)) as FULL_NAME,Lower(concat(first_name,last_name)) as full_name from employees;
-- 4 Find position of '@' in each email.
select First_name,POSITION("@" IN email) as 'position of @ in each email' from employees;
-- 5 Replace domain 'example.com' with 'company.org'.
select First_name,REPLACE(email, "example.com", "company.org") as 'Email change' from employees;
-- 6 Reverse the first name of each employee.
select First_name,REVERSE(First_name) as 'Reverse' from employees;
 -- 7 Show the length of each employee email.
 select First_name,email,length(email) as 'length of each employee email' from employees;
 -- 8 Trim spaces from ' SQL Practice '.
 SELECT TRIM(" SQL Practice ") AS TrimmedString;
 -- 9 Extract the last 4 characters from email addresses (domain).
 Select last_name,mid(email,-4) as 'domain' from employees;
-- 10 Display employees whose last name starts with 'S'.
 Select last_name from employees where last_name like 's%';


--  Numeric Functions
 -- 1 Show absolute value of -1000.
 select abs(-1000) as 'absolute value';
 -- 2 Find the ceiling and floor values of 123.45.
  select ceil(123.45) as 'ceil',floor(123.45) as 'floor';
-- 3 Round the number 98.7654 to 2 decimals.
  select Round(98.7654,2) as 'Round';
-- 4 Show modulus when 55 is divided by 6.
select 55%6 as 'modulus',55/6 as 'division';
 -- 5 Find square root of 121.
 select sqrt(121) as 'square root';
-- 6 Raise 2 to the power of 8.
 select power(2,8) as 'power';
-- 7 Find natural log and base-10 log of 1000.
select log(1000) as 'natural log',log10(1000) as 'base-10 log';
 -- 8 Display the sign of -45, 0, and 20.
 select sign(-45) ,sign(0),sign(20);
--  9 Show 3 random numbers between 0 and 1.
SELECT RAND() AS RandomNumber1,RAND() AS RandomNumber2,RAND() AS RandomNumber3;
 -- 10 Find highest and lowest salary from employees table.
 select max(salary) as 'highest salary',min(salary) as 'lowest salary' from employees;
 -- 11 Display employee salary truncated to 2 decimals.
 select truncate(salary,2) as salary from employees;
 -- 12 Add a random bonus (between 500 and 2000) to each employee’s salary.
 select Rand();
 
 



