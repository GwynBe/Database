CREATE DATABASE IF NOT EXISTS `student_cms_plusplus` CHARACTER SET = utf8mb4;

use student_cms_plusplus;
CREATE TABLE student(
	id int primary key auto_increment,
    `name` varchar(45) null,
    mssv varchar(10) null,
    password varchar(10) null,
    phone varchar(10) null,
    address varchar(45) null,
    age smallint null,
    email varchar(45) null,
    created_timestamp timestamp(4) not null default current_timestamp(), 
    last_updated_timestamp timestamp(4) not null default current_timestamp()
);
create table class(
	id int primary key auto_increment,
    `name` varchar(45) null,
    major varchar(45) null,
    total_student smallint null,
    teacher_name varchar(45) null,
    teacher_phone varchar(10) null,
    created_timestamp timestamp(6) not null default current_timestamp(),
    last_updated_timestamp timestamp(6) not null default current_timestamp()
);
create table student_class(
	student_id int null,
    class_id int null
);