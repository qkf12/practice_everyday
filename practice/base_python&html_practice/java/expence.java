package com.qkf12.practice;

import java.util.Scanner;

public class expence {
    static void main() {
        Scanner sc = new Scanner(System.in);
        System.out.println("请输入你的外卖总价格：");
        double num = sc.nextDouble();
        if (num >= 0 ){
//            饿了么的价格：
            double elm = 0.9;
            double num1 = num *elm;
//        美团的价格：
            double num2;
            if (num >= 30){
                 num2 = num - 10;

            }else{
                 num2 = num;
            }
            if (num1 > num2){
                System.out.println("你要选择美团的");
            }else {
                System.out.println("你要选择饿了么的");
            }
        }else{
            System.out.println("请输入正确的价格哦");
        }
//


    }
}
