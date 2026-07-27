package com.qkf12.practice;

import java.util.Random;

public class arr_dome2 {
    static void main() {
        int arr[] = {1,2,3,4,5,6,7,8,9,10};
//生成随机数
        Random r = new Random();
//数组的长度
        int min = arr.length;
        for (int i = 0; i < min; i++) {
//           随机索引数字
            int ree = r.nextInt(min);
            //中间变量
            int mouth = arr[i];

            arr[i] = arr[ree];
            arr[ree] = mouth;
        }
        for (int i = 0; i < arr.length; i++) {
            System.out.println(arr[i]);
        }
    }
}
