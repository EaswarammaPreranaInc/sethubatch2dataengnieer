create table students # create table if not exists students 
(
student_id int primary key,
first_name varchar(50) not null,
last_name varchar(50),
dob DATE NOT NULL,
gender char(1) 	CHECK  (gender in ('M' , 'F' ))
);
# primary key is the uniquely identifies each row in table 
# each table has one primary key and it cannot have null values 

create table courses
(
course_id int ,
course_name varchar(100),
credits int 
);
select * from students;
select * from courses;
#  Add Constraints using ALTER
# multiple columns wont work , do it single column 
alter table
courses modify 
course_id int primary key ;

ALTER TABLE courses modify
course_name  varchar(100) NOT NULL;

alter table courses modify
credits int check (credits between 1 AND 6);
 # foreign key is used to link the tables together and it ensure that value in one column must already exists in another table 
 # table can have multiple foreign keys to refer multiple  other tables 
 
create table enrollments
(
enroll_id int primary key,
student_id int ,
course_id int ,
FOREIGN KEY (student_id) REFERENCES students(student_id),
FOREIGN KEY (course_id) REFERENCES courses(course_id)
);
drop table enrollments;
# with on delete cascade
create table enrollments
(
enroll_id int primary key,
student_id int ,
course_id int ,
FOREIGN KEY (student_id) REFERENCES students(student_id),
FOREIGN KEY (course_id) REFERENCES courses(course_id)
);

# alter command practise

alter table students ADD email varchar(100) not null;

# MODIFY is used to change datatype/constraints of an existing column.

# Rename the column dob in students to date_of_birth 
alter table students change dob date_of_birth date;


# Drop the column credits from the courses table.
alter table courses drop column credits;

 # Q5. DROP vs TRUNCATE

#Insert a few rows into students and courses.
INSERT INTO students (student_id, first_name, last_name, date_of_birth, gender)
VALUES
(1,'vedha','prakash',2002,'M'),
(2,'sai','prakash',2007,'M'),
(3,'sree','pradeepthi',2009,'F');

 # Use TRUNCATE on the enrollments table and observe the difference vs DELETE.

Finally, use DROP TABLE to remove the courses table completely.
