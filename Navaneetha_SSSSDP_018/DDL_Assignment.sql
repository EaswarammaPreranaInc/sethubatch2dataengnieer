CREATE DATABASE IF NOT EXISTS student;
USE student;
create table student(
	student_id INT PRIMARY KEY,

	first_name VARCHAR(50) NOT NULL,

	last_name VARCHAR(50) NOT NULL,

	dob DATE NOT NULL,

	gender CHAR(1) NOT NULL
);
show tables;

create table courses(
course_id INT,
course_name VARCHAR(100),
credits INT
);
select * from courses;

alter table courses
add primary key(course_id);

alter table courses
modify course_name VARCHAR(100) NOT NULL;

alter table courses
modify credits INT NOT NULL CHECK (credits BETWEEN 1 and 6);


Create table enrollments(
enroll_id INT Primary Key,
student_id INT,
course_id INT);

alter table enrollments
add foreign key (student_id) references student(student_id);

alter table enrollments
add foreign key (course_id) references courses(course_id);

show tables;
select * from enrollments;

-- Add a new column email (VARCHAR(100)) to the students table.
alter table student
add email VARCHAR(100) NOT NULL;

-- Rename the column dob in students to date_of_birth.
alter table student
rename column dob to date_of_birth;

-- Drop the column credits from the courses table.
alter table courses
drop column credits;

-- Insert a few rows into students and courses.
create table student(
	student_id INT PRIMARY KEY,

	first_name VARCHAR(50) NOT NULL,

	last_name VARCHAR(50) NOT NULL,

	dob DATE NOT NULL,

	gender CHAR(1) NOT NULL
);
INSERT INTO student (student_id,first_name, last_name, date_of_birth, gender,email)
VALUES
(1, 'Don','joe','2000-01-19','M','abc@gmail.com'),
(2,'Bose','Roy','2003-05-13','F','ab12@gmail.com'),
(3,'Subam','bose','1990-02-19','M','abc123@gmail.com');
select * from student;

-- truncate on enrollments table
TRUNCATE table enrollments;
select * from enrollments;
-- use DROP TABLE to remove the courses table completely.
DROP TABLE enrollments;
DROP TABLE courses;
USE student;
show tables;
