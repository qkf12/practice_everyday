package com.qkf12.practice;

import java.util.Random;

public class arr_dome3 {
    static void main() {
        int arr[] = new int[5];
        int gua = 0;
        Random r = new Random();
        for (int i = 0;i < arr.length;){
//            生成随机数
            int mouth = r.nextInt(100)+1;
            for (int j = 0; j < arr.length; j++) {
                if (mouth == arr[j]){
                    gua++;
                    break;
                }
            }
            if (gua == 0){
                arr[i] =mouth;
//                i++ 放在这里  是  如果生成数字已经在数组里面了
//                不跳过这一个 立即重新输入
                i++;
            }
        }
        for (int i = 0; i < arr.length; i++) {
            System.out.print(arr[i]+ " ");
        }
//        System.out.println();
    }
}
