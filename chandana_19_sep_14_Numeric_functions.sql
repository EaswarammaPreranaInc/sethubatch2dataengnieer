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