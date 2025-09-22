-- Date & Time Functions

CREATE TABLE employees (
    emp_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    hire_date DATE
);

-- Sample Data
INSERT INTO employees (first_name, last_name, hire_date) VALUES
('John', 'Smith', '2019-01-15'),
('Alice', 'Johnson', '2020-03-22'),
('Mark', 'Brown', '2021-07-10'),
('Sophia', 'Davis', '2022-10-05'),
('David', 'Wilson', '2025-08-15');

-- Table
SELECT * FROM EMPLOYEES;

-- 1. Show current date, time, and timestamp separately.

SELECT 
    CURDATE() AS `Current_Date`, 
    CURTIME() AS `Current_Time`, 
    NOW() AS `Current_Timestamp`;


-- 2. Display each employee’s hire year, month number, and month name.

SELECT emp_id, first_name, last_name,
       YEAR(hire_date) AS Hire_Year,
       MONTH(hire_date) AS Month_No,
       MONTHNAME(hire_date) AS Month_Name
FROM employees;

-- 3. Find which quarter each employee was hired in.

SELECT emp_id, first_name, last_name,
       QUARTER(hire_date) AS Hire_Quarter
FROM employees;

-- 4. Display hire dates with their corresponding week numbers.

SELECT emp_id, hire_date, WEEK(hire_date) AS Week_No
FROM employees;

-- 5. Show the 200th day of the year 2025 using MAKEDATE.

SELECT MAKEDATE(2025, 200) AS Day_200;

-- 6. Create a time value '09:15:00' using MAKETIME.

SELECT MAKETIME(9, 15, 0) AS Time_Value;

-- 7. Find out the difference in time between '14:45:00' and '09:30:00'.

SELECT TIMEDIFF('14:45:00', '09:30:00') AS Time_Difference;

-- 8. Convert '15/08/2025' into a proper date using STR_TO_DATE.

SELECT STR_TO_DATE('15/08/2025', '%d/%m/%Y') AS Converted_Date;

-- 9. Show employee hire date and extract day, month, year separately.

SELECT emp_id, hire_date,
       DAY(hire_date) AS Day,
       MONTH(hire_date) AS Month,
       YEAR(hire_date) AS Year
FROM employees;

-- 10. Find employees hired in the month of January.

SELECT * FROM employees
WHERE MONTH(hire_date) = 1;


-- String Functions

CREATE TABLE staff (
    emp_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    email VARCHAR(100)
);

-- Sample Data
INSERT INTO staff (first_name, last_name, email) VALUES
('John', 'Smith', 'john.smith@example.com'),
('Alice', 'Johnson', 'alice.johnson@example.com'),
('Mark', 'Brown', 'mark.brown@example.com'),
('Sophia', 'Davis', 'sophia.davis@example.com'),
('David', 'Wilson', 'david.wilson@example.com');

SELECT * FROM staff;

-- 1. Concatenate first name and last name into one column.

SELECT CONCAT(first_name, ' ', last_name) AS Full_Name FROM staff;

-- 2. Display first 3 characters of last name.

SELECT last_name, LEFT(last_name, 3) AS First3Chars FROM staff;

-- 3. Show names in upper and lower case.

SELECT UPPER(first_name) AS Upper_Name, LOWER(last_name) AS Lower_Name FROM staff;

-- 4. Find position of '@' in each email.

SELECT email, LOCATE('@', email) AS Position_At FROM staff;

-- 5. Replace domain 'example.com' with 'company.org'.

SELECT email, REPLACE(email, 'example.com', 'company.org') AS Updated_Email FROM staff;

-- 6. Reverse the first name of each employee.

SELECT first_name, REVERSE(first_name) AS Reversed_Name FROM staff;

-- 7. Show the length of each employee email.

SELECT email, LENGTH(email) AS Email_Length FROM staff;

-- 8. Trim spaces from ' SQL Practice '.

SELECT TRIM(' SQL Practice ') AS Trimmed_Text;

-- 9. Extract the last 4 characters from email addresses (domain part).

SELECT email, RIGHT(email, 4) AS Last4Chars FROM staff;

-- 10. Display employees whose last name starts with 'S'.

SELECT * FROM staff
WHERE last_name LIKE 'S%';


--

CREATE TABLE staff_salary (
    emp_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    salary DECIMAL(10,2)
);

-- Sample Data
INSERT INTO staff_salary (first_name, last_name, salary) VALUES
('John', 'Smith', 45000.50),
('Alice', 'Johnson', 52000.75),
('Mark', 'Brown', 61000.00),
('Sophia', 'Davis', 47000.25),
('David', 'Wilson', 58000.90);


-- 1. Show absolute value of -1000.

SELECT ABS(-1000) AS Absolute_Value;

-- 2. Find the ceiling and floor values of 123.45.

SELECT CEIL(123.45) AS Ceiling_Value, FLOOR(123.45) AS Floor_Value;

-- 3. Round the number 98.7654 to 2 decimals.

SELECT ROUND(98.7654, 2) AS Rounded_Value;

-- 4. Show modulus when 55 is divided by 6.

SELECT MOD(55, 6) AS Modulus;

-- 5. Find square root of 121.

SELECT SQRT(121) AS SquareRoot;

-- 6. Raise 2 to the power of 8.

SELECT POW(2, 8) AS Power_Value;

-- 7. Find natural log and base-10 log of 1000.

SELECT LN(1000) AS Natural_Log, LOG10(1000) AS Base10_Log;

-- 8. Display the sign of -45, 0, and 20.

SELECT SIGN(-45) AS Sign_Negative, SIGN(0) AS Sign_Zero, SIGN(20) AS Sign_Positive;

-- 9. Show 3 random numbers between 0 and 1.

SELECT RAND() AS Random1, RAND() AS Random2, RAND() AS Random3;

-- 10. Find highest and lowest salary from staff_salary table.

SELECT MAX(salary) AS Highest_Salary, MIN(salary) AS Lowest_Salary FROM staff_salary;

-- 11. Display employee salary truncated to 2 decimals.

SELECT first_name, last_name, TRUNCATE(salary, 2) AS Truncated_Salary FROM staff_salary;

-- 12. Add a random bonus (between 500 and 2000) to each employee’s salary.

SELECT first_name, last_name, salary,
       salary + FLOOR(RAND() * (2000 - 500 + 1)) + 500 AS Salary_With_Bonus
FROM staff_salary;







