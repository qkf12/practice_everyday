package com.qkf12.practice;

public class while_dome1 {
    static void main() {
//        本金
        double n = 100000;
//        复利
        double f = 0.017;
        double m = 200000;
        int y = 0;
        while (n < m){
            n =n + n * f;
            y ++;
        }
        System.out.println("你需要"+y+"年");
    }
}
