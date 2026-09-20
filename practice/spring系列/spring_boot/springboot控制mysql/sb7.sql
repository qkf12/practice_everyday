CREATE TABLE t_user (
  id int NOT NULL auto_increment,
  username varchar(32) DEFAULT NULL,
  password varchar(32) DEFAULT NULL,
  PRIMARY KEY (id)
) engine=innodb DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;


insert into t_user  values 
(1,"张三","123"),
(2,"李四","234");