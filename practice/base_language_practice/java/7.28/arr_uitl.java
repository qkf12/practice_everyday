package com.qkf12.practice;

public class arr_uitl {
//    防止外界重新定义  new
    private arr_uitl (){}

//    遍历数组

//    只打印
//    public static void print_arr (int [] arr) {
//        System.out.print("[");
//        for (int i = 0; i < arr.length; i++) {
//            if (i == arr.length - 1) {
//                System.out.println(arr[i] + "]");
//            }else  {
//                System.out.print(arr[i] + ", ");
//            }
//        }
//    }
//    返回数字符串

    public static String print_arr (int[] arr) {
        String stytle = "[";
        for (int i = 0; i < arr.length; i++) {
            if (i == arr.length - 1) {
                stytle = stytle + arr[i] +  ']';
            }else  {
                stytle = stytle + arr[i] +  ",";
            }
        }
        return stytle;
    }

//    求最大值
    public static int print_max(int [] arr) {
        int max = arr[0];
        for (int i = 1; i < arr.length; i++) {
            if (max < arr[i]) {
                max = arr[i];
            }
        }
        return max;
    }

//    求平均值
    public static double print_average(int [] arr) {
        double sum = 0;
        for (int i = 0; i < arr.length; i++) {
            sum = sum + arr[i];
        }
        return  sum / arr.length;
    }
}
