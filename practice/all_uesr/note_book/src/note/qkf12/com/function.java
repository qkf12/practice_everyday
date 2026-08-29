package note.qkf12.com;

import java.awt.print.Printable;
import java.sql.SQLOutput;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Scanner;

public class function {
    public static Scanner sc ;
    public static ArrayList<nothing> list = new ArrayList<>();


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
                    delete_function();
                    break;
                case "3":
                    update_function();
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
    //=================================添加新信息====================
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
    //======================删除信息=========================
    public static void delete_function(){
        sc = new Scanner(System.in);
        System.out.println("请输入要删除的日期");
        String answer = sc.next();
        for (int i = list.size() -1; i >= 0 ; i--) {
            nothing note = list.get(i);
            if(note.getDate().equals(answer)){
                String date = note.getDate();
                String type = note.getType();
                double money = note.getMoney();
                System.out.println("您确定要删除这个吗  是/否");
                System.out.println("日期\t类型\t金额");
                System.out.println("==========================");
                System.out.printf("%s\t%s\t%.2f\n",date, type, money);
                String answer1 = sc.next();
                if(answer1.equals("是")){
                    System.out.println("====删除成功====");
                    list.remove(i);
                }
            }


        }
    }



    //===========================更改信息======================
    public static void update_function(){
        sc = new Scanner(System.in);
        System.out.println("请输入你想修改信息的日期");
        String date = sc.next();
        for (int i = 0; i < list.size(); i++) {
            nothing note = list.get(i);
            if(note.getDate().equals(date)){
                String date1 = note.getDate();
                String type = note.getType();
                double money = note.getMoney();
                System.out.println("您要修改哪一列呀");
                System.out.println("======================");
                System.out.println("日期\t类型\t金额");
                System.out.printf("%s\t%s\t%.2f\n",date1,type,money);
                String date3 = sc.next();
                if(date3.equals("类型")){
                    System.out.println("请输入正确的 <类型>");
                    String type3 = sc.next();
                    note.setType(type3);
                    System.out.println("修改<类型>成功");
                }
                if (date3.equals("金额")){
                    System.out.println("请输入正确的 <金额>");
                    Double money3 = sc.nextDouble();
                    note.setMoney(money3);
                    System.out.println("修改<金额>成功");
                }
                return;
            }
        }

    }
    //=============================查看所有信息======================
    public static void check_function(){
        System.out.println("日期\t类型\t金额");
        System.out.println("======================");
//        System.out.println(list);/*测试 类里的@Override*/
        for (int i = 0; i < list.size(); i++) {
            nothing note = list.get(i);
            String date = note.getDate();
            String type = note.getType();
            double money = note.getMoney();
            System.out.printf("%s\t%s\t%.2f\n",date,type,money);
        }
    }
}
