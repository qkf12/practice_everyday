package org.example.spring_boot4;


import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.core.env.Environment;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;




@RestController
public class body {
    @Value("${name}")
    private String name;

    @Value("${person.age}")
    private int age;

    @Value("${arr[0]}")
    private String arr1;

    @Autowired
    private Environment env;




    @RequestMapping("/hello")
    public String hello() {
        System.out.println(name);
        System.out.println(age);
        System.out.println("=================");
        System.out.println(env.getProperty("person.name"));
        System.out.println(env.getProperty("person.age"));
        System.out.println("=================");
        System.out.println(arr1);

        return "hello world";
    }
}
