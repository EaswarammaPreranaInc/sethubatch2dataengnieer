CREATE TABLE students (
    student_id INT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50),
    dob DATE NOT NULL,
    gender CHAR(1) CHECK (gender IN ('M', 'F'))
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
    CONSTRAINT fk_student FOREIGN KEY (student_id) REFERENCES students(student_id),
    CONSTRAINT fk_course FOREIGN KEY (course_id) REFERENCES courses(course_id)
);

CREATE TABLE enrollments_cascade (
    enroll_id INT PRIMARY KEY,
    student_id INT,
    course_id INT,
    CONSTRAINT fk_student_cascade FOREIGN KEY (student_id) REFERENCES students(student_id) ON DELETE CASCADE,
    CONSTRAINT fk_course_cascade FOREIGN KEY (course_id) REFERENCES courses(course_id) ON DELETE CASCADE
);

ALTER TABLE students
ADD email VARCHAR(100);

ALTER TABLE students
RENAME COLUMN dob TO date_of_birth;

ALTER TABLE courses
DROP COLUMN credits;

INSERT INTO students (student_id, first_name, last_name, date_of_birth, gender, email)
VALUES (1, 'Ravi', 'Kumar', '2000-05-12', 'M', 'ravi@example.com'),
       (2, 'Sita', 'Sharma', '1999-11-25', 'F', 'sita@example.com');

INSERT INTO courses (course_id, course_name)
VALUES (101, 'Database Systems'),
       (102, 'Computer Networks');

INSERT INTO enrollments (enroll_id, student_id, course_id)
VALUES (1, 1, 101),
       (2, 2, 102);

TRUNCATE TABLE enrollments;
DROP TABLE courses;

