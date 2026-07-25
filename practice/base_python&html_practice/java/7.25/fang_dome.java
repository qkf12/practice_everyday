package com.qkf12.practice;

import java.util.Random;

public class fang_dome {
    static void main() {
        Random r = new Random();
        int arr [] = new  int [5];
        for (int i = 0; i < arr.length;i++) {
            int mouth = r.nextInt(100)+ 1;
            arr[i] = mouth;
            System.out.println("分数：" + arr[i]);
        }
        int max = max_judgement(arr);
        System.out.println("最大值为"+ max);

        int min = min_judgement(arr);
        System.out.println("最小值为"+ min);
    }
    public static int max_judgement (int arr[]){
        int num = arr[0];
        for (int i = 0;i< arr.length;i++) {
            if (num < arr[i]){
                num = arr[i];
            }

        }
        return num;
    }
    public static int min_judgement (int arr[]){
        int num = arr[0];
        for (int i = 0;i< arr.length;i++) {
            if (num > arr[i]){
                num = arr[i];
            }

        }
        return num;
    }
}
