/*
Assignment: DDL Commands – Student Database
Design a simple Student Database for a college. The database should store information about students, their courses, and enrollments.
*/

-- Q1: CREATE Tables (with constraints)
CREATE TABLE students (
    student_id INT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50),
    dob DATE NOT NULL,
    gender CHAR(1) CHECK (gender IN ('M','F'))
);
-- 1.2 Create courses table (without constraints)
CREATE TABLE courses (
    course_id INT,
    course_name VARCHAR(100),
    credits INT
);

-- Q2: Add Constraints using ALTER
ALTER TABLE courses
ADD CONSTRAINT pk_course PRIMARY KEY (course_id);

ALTER TABLE courses
MODIFY course_name VARCHAR(100) NOT NULL;

ALTER TABLE courses
ADD CONSTRAINT chk_credits CHECK (credits BETWEEN 1 AND 6);

-- Q3: Create a Relationship with Foreign Key
CREATE TABLE enrollments (
    enroll_id INT PRIMARY KEY,
    student_id INT,
    course_id INT,
    CONSTRAINT fk_enroll_student FOREIGN KEY (student_id) 
        REFERENCES students(student_id),
    CONSTRAINT fk_enroll_course FOREIGN KEY (course_id) 
        REFERENCES courses(course_id)
);-- (without cascade)
CREATE TABLE enrollments_cascade (
    enroll_id INT PRIMARY KEY,
    student_id INT,
    course_id INT,
    CONSTRAINT fk_enroll_student_c FOREIGN KEY (student_id) 
        REFERENCES students(student_id) ON DELETE CASCADE ON UPDATE CASCADE,
    CONSTRAINT fk_enroll_course_c FOREIGN KEY (course_id) 
        REFERENCES courses(course_id) ON DELETE CASCADE ON UPDATE CASCADE
);-- (with cascade)

-- Q4: ALTER Commands Practice
ALTER TABLE students
ADD email VARCHAR(100);

ALTER TABLE students
RENAME COLUMN dob TO date_of_birth;

ALTER TABLE courses
DROP COLUMN credits;

-- Q5: DROP vs TRUNCATE
INSERT INTO students (student_id, first_name, last_name, date_of_birth, gender, email)
VALUES 	(1, 'V', 'Thapaswi', '2002-10-08', 'F', 'thapaswi1@gmail.com'), 
		(2, 'A', 'Chandana', '2002-07-20', 'F', 'chandana19@gmail.com'),
		(3, 'V',  'Varsha', '2003-09-07', 'F', 'varsha5@gmail.com'); 

INSERT INTO courses (course_id, course_name)
VALUES 	(101, 'Python'), 
		(102, 'SQL'),
		(103, 'JAVA'); 

INSERT INTO enrollments (enroll_id, student_id, course_id)
VALUES 	(1, 1, 101),
		(2, 2, 102),
		(3, 3, 103);

TRUNCATE TABLE enrollments; -- truncate will only deletes the records of the table but not structure

ALTER TABLE enrollments_cascade
DROP FOREIGN KEY fk_enroll_course_c; -- to drop table first drop the related foreign key in the parent table

DROP TABLE enrollments;
DROP TABLE enrollments_cascade;
DROP TABLE courses; -- drop table delete the records of the table and also structure
