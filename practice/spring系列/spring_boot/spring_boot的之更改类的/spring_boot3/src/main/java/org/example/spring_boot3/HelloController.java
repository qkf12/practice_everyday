package org.example.spring_boot3;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.core.env.Environment;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RequestMapping;



@RestController
public class HelloController {

    @Value("${name}")
    private String name;

    @Value("${address[1]}")
    private String address1;

    @Autowired
    private Environment env;

    @RequestMapping("/hello")
    public String sayHello(){
        System.out.println(name);
        System.out.println(address1);
        System.out.println("===================");
        System.out.println(env.getProperty("person.name"));
        System.out.println(env.getProperty("person.age"));
        System.out.println(env.getProperty("address[0]"));
        return "Hello World";
    }
}
