create database College;

use College;

create table Student (
id int primary key,
name varchar(50),
age int not null
);

insert into student values(1, "Karan", 26);
insert into student values(2, "Arjun", 25);

select * from student;