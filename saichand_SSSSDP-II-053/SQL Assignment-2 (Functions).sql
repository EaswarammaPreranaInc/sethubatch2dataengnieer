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


INSERT INTO employees (first_name, last_name, department, hire_date, email, salary) VALUES
('Arun', 'Vasa', 'IT', '2021-06-15', 'arun.vasa@example.com', 55000.00),
('Priya', 'Sharma', 'HR', '2020-03-10', 'priya.sharma@example.com', 48000.00),
('Rahul', 'Patel', 'Finance', '2019-11-25', 'rahul.patel@example.com', 60000.00),
('Neha', 'Reddy', 'IT', '2022-01-05', 'neha.reddy@example.com', 53000.00),
('Kiran', 'Singh', 'Marketing', '2023-07-20', 'kiran.singh@example.com', 45000.00);

select * from employees;

-- Date & Time Functions
-- 1. Show current date, time, and timestamp separately.
SELECT CURRENT_DATE(),CURRENT_TIME(),CURRENT_TIMESTAMP();

-- 2. Display each employee’s hire year, month number, and month name.
SELECT hire_date, YEAR(hire_date), MONTH(hire_date), MONTHNAME(hire_date)FROM employees;

-- 3. Find which quarter each employee was hired in.
SELECT hire_date, QUARTER(hire_date) FROM employees;

-- 4. Display hire dates with their corresponding week numbers.
SELECT hire_date, WEEK(hire_date) FROM employees;

-- 5. Show the 200th day of the year 2025 using MAKEDATE.
SELECT MAKEDATE(2025, 200) AS two_hundredth_day;

-- 6. Create a time value '09:15:00' using MAKETIME.
SELECT MAKETIME(9, 15, 0) AS time;

-- 7. Find out the difference in time between '14:45:00' and '09:30:00'.
SELECT TIMEDIFF('14:45:00', '09:30:00') AS time_difference;

-- 8. Convert '15/08/2025' into a proper date using STR_TO_DATE.
SELECT STR_TO_DATE('15/08/2025', '%d/%m/%Y') AS formatted_date;

-- 9. Show employee hire date and extract day, month, year separately.
SELECT hire_date,DAY(hire_date) AS hire_day,MONTH(hire_date) AS hire_month,
       YEAR(hire_date) AS hire_year FROM employees;

-- 10. Find employees hired in the month of January.
SELECT * FROM employees WHERE MONTH(hire_date) = 1;


-- String Functions
-- 1. Concatenate first name and last name into one column.
SELECT CONCAT(first_name, ' ', last_name) AS full_name FROM employees;

-- 2. Display first 3 characters of last name.
SELECT last_name, LEFT(last_name, 3) as first3characters FROM employees;

-- 3. Show names in upper and lower case.
SELECT CONCAT(first_name, ' ', last_name) as fullname,
LCASE(CONCAT(first_name, ' ', last_name)) as lowercase,
UCASE(CONCAT(first_name, ' ', last_name)) AS uppercase FROM employees;

-- 4. Find position of '@' in each email.
SELECT email, INSTR(email, '@') AS at_position FROM employees;

-- 5. Replace domain 'example.com' with 'company.org'.
SELECT email, REPLACE(email, 'example.com', 'company.org') AS updated_email
FROM employees;

-- 6. Reverse the first name of each employee.
SELECT first_name, REVERSE(first_name) AS reversed_name FROM employees;

-- 7. Show the length of each employee email.
SELECT email,LENGTH(email) AS email_length FROM employees;

-- 8. Trim spaces from ' SQL Practice '.
SELECT TRIM('   SQL Functions   ') AS trimmed_text;

-- 9. Extract the last 4 characters from email addresses (domain).
SELECT email, RIGHT(email, 4) AS domain FROM employees;

-- 10. Display employees whose last name starts with 'S'.
SELECT * FROM employees WHERE last_name LIKE 'S%';


-- Numeric Functions
-- 1. Show absolute value of -1000.
SELECT ABS(-1000) AS absolute_value;

-- 2. Find the ceiling and floor values of 123.45.
SELECT CEIL(123.45) AS ceiling_value, FLOOR(123.45) AS floor_value;

-- 3. Round the number 98.7654 to 2 decimals.
SELECT ROUND(98.7654, 2) AS rounded_value;

-- 4. Show modulus when 55 is divided by 6.
SELECT MOD(55, 6) AS modulus;

-- 5. Find square root of 121.
SELECT SQRT(121) AS square_root;

-- 6. Raise 2 to the power of 8.
SELECT POW(2, 8) AS power_result;

-- 7. Find natural log and base-10 log of 1000.
SELECT LN(1000) AS natural_log, LOG10(1000) AS base10_log;

-- 8. Display the sign of -45, 0, and 20.
SELECT SIGN(-45) AS sign_neg,SIGN(0) AS sign_zero,SIGN(20) AS sign_pos;

-- 9. Show 3 random numbers between 0 and 1.
SELECT RAND() AS rand1,RAND() AS rand2,RAND() AS rand3;

-- 10. Find highest and lowest salary from employees table.
SELECT MAX(salary) AS highest_salary,MIN(salary) AS lowest_salary FROM employees;

-- 11. Display employee salary truncated to 2 decimals.
SELECT salary,TRUNCATE(salary, 2) AS salary FROM employees;

-- 12. Add a random bonus (between 500 and 2000) to each employee’s salary
SELECT salary,salary + FLOOR(500 + (RAND() * 1501)) AS bonus FROM employees;
