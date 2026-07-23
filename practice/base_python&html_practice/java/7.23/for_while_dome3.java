package com.qkf12.practice;

import java.util.Scanner;

public class for_while_dome3 {
    static void main() {
//        判断一个大于2的数字是否为质数
        Scanner sc = new Scanner(System.in);
        int num;
        while (true){
            System.out.println("请输入一个大于2的整数");
             num = sc.nextInt();
            if (num > 2){
                break;
            }else {
                System.out.println("这个数字小于等于2 ");
            }
        }
        int b = 0;
        for (int i = 2; i < num; i++) {
            if (num % i == 0){
                b ++;
                break;
            }
        }
        if (b == 0){
            System.out.println(num + "是质数");
        }else {
            System.out.println(num + "不是质数");
        }
    }
}
