create table `user`(
id bigint primary key not null comment "主键ID",
name varchar(30) null default null comment "姓名",
email varchar(50) null default null comment "邮箱"

);


select * from user;

alter  table `user` drop column email;


alter table  `user` add column age int null default null comment "年龄";

alter  table `user` add column email varchar(50) null default null comment "邮箱";


