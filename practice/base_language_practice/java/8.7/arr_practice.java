package com.qkf12.practice;

import com.sun.jdi.PathSearchingVirtualMachine;

import java.util.Random;

public class arr_practice {
    public static void main(String[] args) {

//        生成数组  里面不能为0

//        Random rand = new Random();
//        int [] arr = new int [5];
//        for(int i=0;i<arr.length;){
//            int num = rand.nextInt(101);
//            int count=0;
//            for(int j=0;j<i;j++){  //这里  j< i 可以避免生成0时无法加入数组
//                if(num ==arr[j]){
//                    count++;
//                    break;
//                }
//            }
//            if(count == 0){
//                arr[i]=num;
//                i++;     //只有没有重复的时候 才可以往前一补
//            }
//        }
//        for (int i = 0; i < arr.length; i++) {
//            System.out.print(arr[i] + " ");
//        }

//        int [] arr = {1,1,2,2,2,3,3,3,3};
//        int fast = 1;
//        int slow = 0;
//        while(fast<arr.length){
//            if(arr[slow]!=arr[fast]) {
//                slow ++;
//                arr[slow]=arr[fast];
//            }
//            fast++;
//        }
//        for (int i = 0; i < slow + 1; i++) {
//            System.out.print(arr[i] + " ");
//        }
//        System.out.println();


//        在不考虑 效率的情况下  给定数组  之和 等于目标数字  输出所有  组合和索引
//        int [] nums = {1,2,3,4,5};
//        int target = 6;
//        for (int i = 0; i < nums.length; i++) {
//            for (int j = i + 1;  j< nums.length; j++) {
//                if (nums[i] + nums[j] == target) {
//                    System.out.println( "数字为：" + nums[i] + "(" + i + ")" + "和" + nums[j] + "(" + j + ")");
//                }
//            }
//        }


//      多数组组合排序
//        int [] arr1 = {1,3,5,7,9};
//        int [] arr2 = {2,4,6,8,10};
//        int [] arr3 = new  int[arr1.length+arr2.length];
//        for (int i = 0; i < arr1.length; i++) {
//            arr3[i] = arr1[i];
//        }
//        for (int i = 0; i < arr2.length; i++) {
//            arr3[i+arr1.length] = arr2[i];
//        }
//
//        for (int i = 0; i < arr3.length; i++) {
//            System.out.print(arr3[i] + " ");
//        }
//        System.out.println();

//        外层定位置，内层找下标；内层结束再交换，原位不动最稳妥！
//        for (int i = 0; i < arr3.length -1; i++) {
//            int min = i;
//            for (int j = i+1; j < arr3.length; j++) {
//
//                if (arr3[j] < arr3[min]) {
//                    min = j;
//                }
//            }
//            if (min != i) {
//                int temp = arr3[i];
//                arr3[i] = arr3[min];
//                arr3[min] = temp;
//            }
//        }
//       for (int i = 0; i < arr3.length; i++) {
//           System.out.print(arr3[i] + " ");
//       }


//       另一种写法  三指针法
        int [] arr1 = {1,3,5,7,9};
        int [] arr2 = {2,4,6,8,10};
        int [] arr3 = new  int[arr1.length+arr2.length];

        int i = 0;
        int j = 0;
        int k = 0;  //分别对应每个数组  一个数组一个指针

        while (i < arr1.length && j < arr2.length) {
            if (arr1[i] < arr2[j]) {
                arr3[k] = arr1[i];
                i++;
            }else {
                arr3[k] = arr2[j];
                j++;
            }
            k++;
        }

        System.out.println("字符" + i + j + k);

        while (i < arr1.length) {
            arr3[k] = arr1[i];
            i++;
            k++;
        }
        while (j < arr2.length) {
            arr3[k] = arr2[j];
            j++;
            k++;
        }
        for(int x : arr3){
            System.out.print(x+" ");
        }
    }
}
