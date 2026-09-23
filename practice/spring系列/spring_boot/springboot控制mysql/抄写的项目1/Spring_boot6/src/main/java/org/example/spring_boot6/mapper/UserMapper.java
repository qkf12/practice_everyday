package org.example.spring_boot6.mapper;


import com.baomidou.mybatisplus.core.mapper.BaseMapper;
import org.example.spring_boot6.entity.User;
import org.apache.ibatis.annotations.Mapper;

@Mapper
public interface UserMapper extends BaseMapper<User> {

}

