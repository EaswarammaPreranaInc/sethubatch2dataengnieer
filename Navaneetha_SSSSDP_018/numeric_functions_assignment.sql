select * from employees;
-- Show absolute value of -1000.
SELECT -1000 AS number, ABS(-1000) AS absolute_value;

-- 2. Find the ceiling and floor values of 123.45.
SELECT CEIL(123.45) AS ceil_value, floor(123.45);

--  3. Round the number 98.7654 to 2 decimals.
select round(98.7624,2) As rounded_value;

--  4. Show modulus when 55 is divided by 6.
SELECT MOD(55, 6) AS modulus;

--  5. Find square root of 121.
SELECT SQRT(121) AS square_root;

-- 6. Raise 2 to the power of 8.
SELECT POWER(2, 8) AS power_value; 

--  7 Find natural log and base-10 log of 1000.
SELECT LOG(1000) AS natural_log, LOG10(1000) AS log_base10;

--  8 Display the sign of -45, 0, and 20.
SELECT SIGN(-45), SIGN(0), SIGN(20);

--  9 Show 3 random numbers between 0 and 1.
select rand() as random_number;
SELECT round(RAND()*10,0) AS random_number;

--  10 Find highest and lowest salary from employees table.
SELECT max(salary) AS greatest_salary, 
min(salary) as lowest_salary
from employees;

--  11 Display employee salary truncated to 2 decimals.
SELECT salary,TRUNCATE(salary, 2) AS truncated_value
from employees;

--  12 Add a random bonus (between 500 and 2000) to each employee’s salary


