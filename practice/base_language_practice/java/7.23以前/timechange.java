package com.qkf12.practice;

import java.util.Scanner;

public class timechange {
    public static void main(){
        Scanner sc = new Scanner(System.in);
        System.out.println("请输入任意秒");
        int num = sc.nextInt();
        int hours = num / 3600;
        int min = num % 3600 / 60;
        int second = num %3600 %60;
        System.out.println(hours + "时" + min + "分" + second + "秒");
//        System.out.println(min);
//        System.out.println(second);

    }
}
