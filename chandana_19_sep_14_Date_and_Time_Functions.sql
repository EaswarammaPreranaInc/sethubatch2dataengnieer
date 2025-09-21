CREATE DATABASE employees;

USE employees;

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
VALUES (101, '1994-08-05', 'Aarav', 'Mehta', 'M', '2020-05-10', 3),
       (102, '2002-07-12', 'Arjun', 'Patel', 'M', '2021-06-09', 2),
       (103, '2000-06-07', 'Priya', 'Sharma', 'F', '2024-07-08', 1);
       
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






       
       
 



