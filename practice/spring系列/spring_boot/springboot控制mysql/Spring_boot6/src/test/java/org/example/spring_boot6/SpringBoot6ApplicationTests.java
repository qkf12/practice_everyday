package org.example.spring_boot6;

import com.baomidou.mybatisplus.core.toolkit.Assert;
import jakarta.annotation.Resource;
import org.example.spring_boot6.entity.User;
import org.example.spring_boot6.mapper.UserMapper;
import org.junit.jupiter.api.Test;
import org.springframework.boot.test.context.SpringBootTest;

import java.util.List;

@SpringBootTest
class SpringBoot6ApplicationTests {
    @Resource  //依赖注入
    public UserMapper userMapper;



    @Test
    void contextLoads() {
        System.out.println(("----- selectAll method test ------"));
        List<User> userList = userMapper.selectList(null);
        Assert.isTrue(5 == userList.size(), "");
        userList.forEach(System.out::println);

    }

}
