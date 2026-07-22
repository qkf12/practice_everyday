package com.qkf12.practice;

import java.util.Scanner;

public class fordome3 {
    static void main() {
        Scanner sc = new Scanner(System.in);
        System.out.println("请输入一个两位数字的范围");
        int sum = sc.nextInt();
        int b = 0;
        for (int i = 1;i <= sum;i++){
            if (i % 3 ==0 && i % 5==0){
                b ++;
                System.out.println(i);
            }
        }
        System.out.println(b);
    }
}
