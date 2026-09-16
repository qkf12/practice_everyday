package org.example.spring_boot6.controller;


import com.baomidou.mybatisplus.extension.conditions.update.LambdaUpdateChainWrapper;
import jakarta.annotation.Resource;
import org.example.spring_boot6.entity.User;
import org.example.spring_boot6.mapper.UserMapper;
import org.springframework.web.bind.annotation.*;

import java.util.List;


@RestController
@RequestMapping("/user")
public class UserController {

    @Resource
    private UserMapper userMapper;

    @GetMapping
    public List<User> getAll() {
        return userMapper.selectList(null);
    }
    @GetMapping("/{id}")
    public String get2(@PathVariable int id){
        return "查看指定信息";
    }
    @PostMapping("/id")
    public String save(@RequestBody User user) {
        return "用户新增成功";
    }
    @PutMapping("/{id}")
    public String update1(@PathVariable int id, @RequestBody User user){
        return "修改学生信息";
    }
    @DeleteMapping("/id")
    public String delete1(@RequestParam int id){
        return "删除学生信息";
    }

}
