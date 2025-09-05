Assignment: DDL Commands – Student Database
Design a simple Student Database for a college. The database should store information about students, their courses, and enrollments.
Questions
Q1. CREATE Tables (with & without constraints)
Create a table students with the following columns (add constraints where needed):
student_id (INT, Primary Key)
first_name (VARCHAR(50), NOT NULL)
last_name (VARCHAR(50))
dob (DATE, NOT NULL)
gender (CHAR(1), check constraint: only 'M' or 'F')

create database Student;
use Student;
create table Students(
student_id int primary key,
first_name varchar(20) not null,
last_name  varchar(50),
dob date not null,
gender char(1) check (gender in ('m' ,'f'))
);


Create another table courses without constraints with the following columns:
course_id (INT)
course_name (VARCHAR(100))
credits (INT)

create table courses(
course_id int,
course_name varchar(100),
credits int
);

Q2. Add Constraints using ALTER
Using ALTER TABLE, modify the courses table to add:
Primary key on course_id
NOT NULL on course_name
Check constraint on credits (must be between 1 and 6)

alter table courses
add constraint primary key(course_id);
alter table courses
modify column course_name varchar(100) not null;
alter table courses
add constraint credits check (credits between 1 and 6);

Q3. Create a Relationship with Foreign Key
Create an enrollments table with:
enroll_id (INT Primary Key)
student_id (INT)
course_id (INT)
Add foreign key constraints so that:
student_id references students(student_id)
course_id references courses(course_id)
Try creating this with and without ON DELETE CASCADE, and note the difference.

create table enrollments(
enroll_id int primary key,
student_id int,
course_id int,
foreign key (student_id) references Students(student_id),
foreign key (course_id) references courses(course_id)
);

Q4. ALTER Commands Practice
Perform the following changes:
Add a new column email (VARCHAR(100)) to the students table.
Rename the column dob in students to date_of_birth.
Drop the column credits from the courses table.

alter table students
add email varchar(100);
alter table students
rename column dob to date_of_birth;
alter table courses
drop column credits;

Q5. DROP vs TRUNCATE
Insert a few rows into students and courses.
Use TRUNCATE on the enrollments table and observe the difference vs DELETE.
Finally, use DROP TABLE to remove the courses table completely.

insert into students values(
1,
'Jagannath',
'Bishwal',
'1999-12-31',
'm',
'jagannathbishwal123'
);
insert into enrollments values(
1,
1,
1
);
insert into enrollments values(
2,
1,
1
);
insert into courses values(
1,
'data engineer'
);
truncate table enrollments;
drop table courses;
