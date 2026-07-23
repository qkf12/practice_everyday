package com.qkf12.practice;

public class while_dome2 {
    static void main() {
//        珠穆朗玛峰的高
        double z = 8848860;
//        纸的厚度
        double zhi = 0.1;
//        次数
        int c = 0;
        while (zhi < z){
            zhi = zhi * 2;
            c += 1;
        }
        System.out.println("需要"+c+"次");
    }
}
