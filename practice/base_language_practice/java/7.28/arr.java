package com.qkf12.practice;

public class arr {
    static void main() {
        int [] num = {10,20,30,40,50};
//        遍历数组
        String ss = arr_uitl.print_arr(num);
        System.out.println(ss);
//        找最大数
        int ss1 = arr_uitl.print_max(num);
        System.out.println("数组中最大数为："+ss1);
//        求平均值
        System.out.println("平均值为：" + arr_uitl.print_average(num));
    }
}
