package org.example.spring_boot5;


import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

//第一种接受前端信息的方法

//@RestController
//public class request {
//    @GetMapping("/hello")
//    public String hello(@RequestParam(defaultValue = "") String name){
//        System.out.println(name);
//        return "hello world";
//    }
//}



//第二种接受前端信息的方法

@RestController
public class request {
    @GetMapping("/hello/{name}")
    public String hello(@PathVariable String name){
        System.out.println(name);
        return "hello world";
    }
}