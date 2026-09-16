alter table `user`
modify column `id` bigint not null auto_increment comment "主键id",
add column `create_time` datetime comment "创建时间",
add column `update_time` datetime comment "修改时间";



select * from `user`;

delete from `user` where id = 6;

update `user` 
set create_time = now(),update_time = now() 
where id != 1;

