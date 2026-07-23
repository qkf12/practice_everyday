package com.qkf12.practice;

import java.util.Scanner;

public class for_dome2 {
    static void main() {
        Scanner sc = new Scanner(System.in);
        System.out.println("请输入一个项数");
        int num = sc.nextInt();
        int sum = 0 ;
        for (int i = 1;i <=num;i++){
            if (i % 2 ==0){
                sum =  sum - i;
            }else {
                sum  = sum + i;
            }

        }
        System.out.println(sum);
    }
}
