-- Assignment: DDL Commands – Student Database

-- Q1. CREATE Tables (with & without constraints)

-- Create students table with constraints
CREATE TABLE students (
    student_id INT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50),
    dob DATE NOT NULL,
    gender CHAR(1) CHECK (gender IN ('M','F'))
);

-- Create courses table without constraints
CREATE TABLE courses (
    course_id INT,
    course_name VARCHAR(100),
    credits INT
);

------------------------------------------------------------

-- Q2. Add Constraints using ALTER

ALTER TABLE courses
ADD CONSTRAINT pk_course PRIMARY KEY (course_id);

ALTER TABLE courses
MODIFY course_name VARCHAR(100) NOT NULL;

ALTER TABLE courses
ADD CONSTRAINT chk_credits CHECK (credits BETWEEN 1 AND 6);

------------------------------------------------------------

-- Q3. Create a Relationship with Foreign Key

-- Create enrollments table
CREATE TABLE enrollments (
    enroll_id INT PRIMARY KEY,
    student_id INT,
    course_id INT,
    CONSTRAINT fk_student FOREIGN KEY (student_id) REFERENCES students(student_id),
    CONSTRAINT fk_course FOREIGN KEY (course_id) REFERENCES courses(course_id)
);

-- Alternative with ON DELETE CASCADE
-- (this version automatically removes enrollments if a student or course is deleted)
CREATE TABLE enrollments_cascade (
    enroll_id INT PRIMARY KEY,
    student_id INT,
    course_id INT,
    CONSTRAINT fk_student_cascade FOREIGN KEY (student_id) REFERENCES students(student_id) ON DELETE CASCADE,
    CONSTRAINT fk_course_cascade FOREIGN KEY (course_id) REFERENCES courses(course_id) ON DELETE CASCADE
);

------------------------------------------------------------

-- Q4. ALTER Commands Practice

-- Add new column
ALTER TABLE students ADD email VARCHAR(100);

-- Rename column dob → date_of_birth
ALTER TABLE students CHANGE dob date_of_birth DATE NOT NULL;

-- Drop credits column from courses
ALTER TABLE courses DROP COLUMN credits;

------------------------------------------------------------

-- Q5. DROP vs TRUNCATE

-- Insert rows into students
INSERT INTO students (student_id, first_name, last_name, date_of_birth, gender, email)
VALUES (1, 'Goutham', 'Macha', '2002-05-10', 'M', 'goutham@example.com'),
       (2, 'Sita', 'Rao', '2003-08-21', 'F', 'sita@example.com');

-- Insert rows into courses
INSERT INTO courses (course_id, course_name)
VALUES (101, 'Data Science'),
       (102, 'AI & ML');

-- Insert rows into enrollments
INSERT INTO enrollments (enroll_id, student_id, course_id)
VALUES (1, 1, 101),
       (2, 2, 102);

-- TRUNCATE enrollments table (removes all rows but keeps structure)
TRUNCATE TABLE enrollments;

-- DELETE example (removes rows conditionally, slower than TRUNCATE)
-- DELETE FROM enrollments WHERE enroll_id = 1;

-- DROP courses table (removes structure + data completely)
DROP TABLE courses;
