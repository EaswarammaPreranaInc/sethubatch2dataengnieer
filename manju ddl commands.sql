/*
Assignment: DDL Commands – Student Database
Design a simple Student Database for a college. The database should store information about students, their courses, and enrollments.
*/
CREATE DATABASE SUREKHA;
USE SUREKHA;
 
CREATE TABLE students (
    student_id INT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50),
    dob DATE NOT NULL,
    gender CHAR(1) CHECK (gender IN ('M','F'))
);

CREATE TABLE courses (
    course_id INT,
    course_name VARCHAR(100),
    credits INT
);


ALTER TABLE courses
ADD CONSTRAINT pk_course PRIMARY KEY (course_id);

ALTER TABLE courses
MODIFY course_name VARCHAR(100) NOT NULL;

ALTER TABLE courses
ADD CONSTRAINT chk_credits CHECK (credits BETWEEN 1 AND 6);


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


ALTER TABLE students
ADD email VARCHAR(100);

ALTER TABLE students
RENAME COLUMN dob TO date_of_birth;

ALTER TABLE courses
DROP COLUMN credits;


INSERT INTO students (student_id, first_name, last_name, date_of_birth, gender, email)
VALUES 	(1, 'k', 'Manju', '2004-08-26', 'F', 'manju@gmail.com'), 
		(2, 'M', 'Chandrika', '2004-04-06', 'F', 'chandrika19@gmail.com'),
		(3, 'V',  'Karuna', '2003-09-07', 'F', 'Karuna5@gmail.com'); 

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

