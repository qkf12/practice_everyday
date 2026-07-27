package com.qkf12.practice;

public class arr_dome1 {
    static void main() {
        int arr[] = {33,5,22,44,55 };
        int max = arr[0];
        int min = arr.length;
        for (int i= 1;i < min;i++ ){
            if (max < arr[i]){
                max = arr[i];
            }
        }
        System.out.println(max);
    }
}
