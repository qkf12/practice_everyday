package com.qkf12.practice2;

import java.lang.reflect.Array;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class function {
    private static  ArrayList<food> foods = new ArrayList<>();
    public static void main_function(){

        Scanner sc = new Scanner(System.in);
        while(true){
            System.out.println("1,上架菜品");
            System.out.println("2,查看菜品");
            System.out.println("3,更改菜品");
            System.out.println("4,删除菜品");
            System.out.println("5,退出界面");
            System.out.println("请输入你想要的功能");
            String min_function = sc.nextLine();

            switch(min_function) {
                case "1":
                    one_function();
                    break;
                case "2":
                    two_function();
                    break;
                case "3":
                    three_function();
                    break;
                case "4":
                    four_function();
                    break;
                case "5":
                    return;
                default:
                    System.out.println("请输入正确的功能数字");
            }
        }
    }
    public static void one_function(){
        Scanner sc = new Scanner(System.in);

        while(true){
            System.out.println("请输入菜品名称");
            String name = sc.next();
            System.out.println("请输入菜品价格");
            double price = sc.nextDouble();
            System.out.println("请输入菜品简介");
            String introduction = sc.next();
            food f = new food(name,price,introduction);
            foods.add(f);
            while (true){
                System.out.println("添加成功！您是否还要继续添加食物 1/添加  2/结束");
                int m =  sc.nextInt();
                if(m == 1){
                    break;
                }else if(m == 2){
                    return;
                }else {
                    System.out.println("请输入正确功能哦");
                }
            }
        }
    }

    public static void two_function(){
        if (foods.size()==0){
            System.out.println("请先上架菜哦");
            return;
        }
        for (int i = 0; i < foods.size(); i++) {

                System.out.print( "[" + foods.get(i).getName() + ",");
                System.out.print(foods.get(i).getPrice() + ",");
                System.out.println(foods.get(i).getIntroduction()+ "]");

        }
    }
    public static void three_function(){
        Scanner sc = new Scanner(System.in);
        System.out.println("请输入你要更改的菜品名字");
        String update_name = sc.next();
        for (int i = 0; i < foods.size(); i++) {
           String  ere =  foods.get(i).getName();
           if(ere.contains(update_name)){
               System.out.println("您要修改的是[" + ere + "]的信息吗？");

           }
        }
        System.out.println("请输入你要修改的菜品名字");
        String wew = sc.next();
        for (int i = 0; i < foods.size(); i++) {
            if ( wew.equals(foods.get(i).getName())){
                System.out.println("请输入菜品名称");
                String name2 = sc.next();
                System.out.println("请输入菜品价格");
                double price2 = sc.nextDouble();
                System.out.println("请输入菜品简介");
                String introduction2 = sc.next();
                foods.get(i).setName(name2);
                foods.get(i).setPrice(price2);
                foods.get(i).setIntroduction(introduction2);
                System.out.println(foods.get(i).getName());
                System.out.println(foods.get(i).getPrice());
                System.out.println(foods.get(i).getIntroduction());
            }
        }
    }
    public static void four_function(){
        Scanner sc = new Scanner(System.in);
        System.out.println("请输入你要删除的菜品关键字");
        String key_name = sc.next();
//        boolean flag = false;
        for (int i = 0; i < foods.size(); i++) {
            if (foods.get(i).getName().contains(key_name)) {
                System.out.println("您要删除的是[" + foods.get(i).getName() + "]吗？");
            }
        }
        System.out.println("请输入你要删除的菜品名称");
        String name3 = sc.next();
        for (int i = foods.size() - 1; i >=0 ; i--) {
            if (name3.equals(foods.get(i).getName())) {
                foods.remove(i);
            }
        }

    }
}
