package org.example.spring_boot6.entity;

import com.baomidou.mybatisplus.annotation.TableName;
import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

@Data      //这里的Data 在第六步导入  要导入环境
//data  的作用是简写 get 和set 方法
@TableName("`user`")
@NoArgsConstructor    //无参构造
@AllArgsConstructor  //实参构造

public class User {
    private Long id;
    private String name;
    private Integer age;
    private String email;
}

