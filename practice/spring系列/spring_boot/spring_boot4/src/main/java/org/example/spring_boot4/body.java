package org.example.spring_boot4;


import org.springframework.beans.factory.annotation.Value;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;




@RestController
public class body {
    @Value("${name}")
    private String name;


    @RequestMapping("/hello")
    public String hello() {
        System.out.println(name);
        return "hello world";
    }
}
