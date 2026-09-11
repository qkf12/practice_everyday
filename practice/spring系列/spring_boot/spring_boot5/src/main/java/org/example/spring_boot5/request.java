package org.example.spring_boot5;



import org.springframework.web.bind.annotation.*;

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

//@RestController
//public class request {
//    @GetMapping("/hello/{name}")
//    public String hello(@PathVariable String name){
//        System.out.println(name);
//        return "hello world";
//    }
//}


//第三种接受前端信息的方法

//@RestController
//public class request {
//    @PostMapping("/user")
//    public String hello(@RequestBody User user){
//        System.out.println("name:"+user.getName());
//        System.out.println("age:"+user.getAge());
//        return "hello world";
//    }
//}

// 增删改查  用户信息的雏形

@RestController
@RequestMapping("/hello")
public class request {
    @GetMapping
    public String get1(){
        return "查看所有信息";
    }

    @GetMapping("/{id}")
    public String get2(@PathVariable int id){
        return "查看指定信息";
    }

    @PostMapping("/{id}")
    public String add1(@RequestBody User user){
        return "增加学生信息";
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






