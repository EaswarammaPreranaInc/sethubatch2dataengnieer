-- Step1: Creating a database college 
CREATE DATABASE college;
USE college;
-- Q1. CREATE Tables (with & without constraints)
CREATE TABLE students(
student_id INT,
first_name VARCHAR(50),
last_name VARCHAR(50),
dob DATE,
gender CHAR(1));
DROP TABLE students;
CREATE TABLE students(
student_id int primary key,
first_name VARCHAR(50) not null,
last_name VARCHAR(50) ,
dob DATE NOT NULL,
gender CHAR(1),
CHECK(gender IN ('M','F' ))) ;

CREATE TABLE courses(
course_id INT,
course_name VARCHAR(100),
credits INT);
ALTER TABLE courses
ADD constraint cs3 PRIMARY KEY(course_id),
ADD constraint cs1 CHECK(credits>1 AND credits<6);
-- --error 
ALTER TABLE courses
ALTER COLUMN course_name SET NOT NULL ;
-- error 
CREATE TABLE enrollments(
enroll_id INT PRIMARY KEY,
student_id INT,
course_id INT,
CONSTRAINT cs4 FOREIGN KEY(student_id) REFERENCES students(student_id),
CONSTRAINT cs5 FOREIGN KEY(course_id) REFERENCES courses(course_id));

DROP TABLE enrollments;

CREATE TABLE enrollments(
enroll_id INT PRIMARY KEY,
student_id INT,
course_id INT,
CONSTRAINT cs6 FOREIGN KEY(student_id) REFERENCES students(student_id) ON UPDATE CASCADE ON DELETE CASCADE,
CONSTRAINT cs7 FOREIGN KEY(course_id) REFERENCES courses(course_id) ON UPDATE CASCADE ON DELETE CASCADE);

ALTER TABLE students
ADD email VARCHAR(100),
RENAME COLUMN dob to date_of_birth;

ALTER TABLE courses
DROP COLUMN credits;

-- Q5. DROP vs TRUNCATE

INSERT INTO students VALUES
(1, 'Aarav',  'Sharma',   '2003-05-14', 'M', 'aarav.sharma@example.com'),
(2, 'Isha',   'Patel',    '2002-09-22', 'F', 'isha.patel@example.com'),
(3, 'Rahul',  'Verma',    '2004-01-30', 'M', 'rahul.verma@example.com'),
(4, 'Sneha',  'Reddy',    '2001-12-10', 'F', 'sneha.reddy@example.com'),
(5, 'Kiran',  'Nair',     '2003-07-08', 'M', 'kiran.nair@example.com'),
(6, 'Meera',  'Menon',    '2002-03-19', 'F', 'meera.menon@example.com'),
(7, 'Vikram', 'Singh',    '2004-06-25', 'M', 'vikram.singh@example.com'),
(8, 'Ananya', 'Iyer',     '2001-11-03', 'F', 'ananya.iyer@example.com');

INSERT INTO courses VALUES
(1, 'Computer Science Fundamentals'),
(2, 'Data Structures and Algorithms'),
(3, 'Database Management Systems'),
(4, 'Operating Systems'),
(5, 'Computer Networks'),
(6, 'Software Engineering'),
(7, 'Machine Learning'),
(8, 'Artificial Intelligence'),
(9, 'Compiler Design'),
(10, 'Web Development'),
(11, 'Chemistry');

-- Use TRUNCATE on the enrollments table and observe the difference vs DELETE.
select * from enrollments;
TRUNCATE TABLE enrollments;
select * from enrollments;
DELETE from enrollments;
-- Finally, use DROP TABLE to remove the courses table completely.
DROP TABLE courses