package note.qkf12.com;

import java.sql.SQLOutput;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Scanner;

public class function {
    public static Scanner sc ;
    public static ArrayList list = new ArrayList();


//    ======================主系统==================
    static void main() {
        sc = new Scanner(System.in);
        while(true){
            System.out.println("====欢迎进入记事本====");
            System.out.println("请选择你想要的功能");
            System.out.println("1.增加日常信息");
            System.out.println("2.删除无用信息");
            System.out.println("3.更改错误信息");
            System.out.println("4.查看全部信息");
            System.out.println("5.退出记事本");
            String choice = sc.next();
            switch (choice){
                case "1":
                    add_function();
                    break;
                case "2":
//                    delete_function();
                    break;
                case "3":
//                    update_function();
                    break;
                case "4":
                    check_function();
                    break;
                case "5":
                    System.out.println("====欢迎下次登录====");
                    return;
            }
        }
    }
    public static void add_function(){
        sc = new Scanner(System.in);

        while(true){
            System.out.println("请输入日期");
            String date = sc.next();
            System.out.println("请输入方式  (支出/获得)");
            String type = sc.next();
            System.out.println("请输入金钱");
            double money = sc.nextDouble();
            nothing note = new nothing(date,type,money);
            list.add(note);
            System.out.println("您是否还要添加新事情   是(1)/否(2)");
            String choice = sc.next();
            if(choice.equals("2")){
                break;
            }
        }

    }
    public static void check_function(){
        System.out.println(list);

    }
}
