
create database if not exists student;
                                                                                                                                                                         create database student;
use student;

create table students(
	student_id INT Primary Key,
    	first_name VARCHAR(50) NOT NULL,
	last_name VARCHAR(50),
	dob DATE NOT NULL,
	gender CHAR(1) CHECK (gender IN ('M', 'F'))
);

create table courses(
	course_id INT,
	course_name VARCHAR(100),
	credits INT 
);

alter table courses modify course_id INT primary key;

alter table courses modify course_name VARCHAR(100) not null;

alter table courses add CONSTRAINT chk_credits  CHECK (credits between 1 and 6);

create table enrollments(
	enroll_id int primary key,
	student_id int,
	course_id int
    );
    
alter table enrollments 
add constraint fk_students foreign key (student_id) 
references students(student_id);
    
alter table enrollments drop foreign key fk_students; 
    
alter table enrollments 
add constraint fk_students foreign key (student_id) 
references students(student_id)
on delete cascade;
    
alter table students add email varchar(100);
    
alter table students change dob date_of_birth date not null;
    
alter table courses drop credits;
    
insert into students( student_id , first_name , last_name , date_of_birth , gender , email )
values(1,'nikesh','Rao','2003-05-18','M','nikesh@gmail.com'),
      (2,'aravind','boats','2003-10-10','M','aravind@gmail.com');
          
select * from students;
    
insert into enrollments(enroll_id,student_id,course_id)
values(1,1,1),
      (2,2,2);    

select * from enrollments;

delete from enrollments where enroll_id =2;
select * from enrollments;

truncate table enrollments;
select * from enrollments;

drop table courses;
select * from courses;