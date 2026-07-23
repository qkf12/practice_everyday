package com.qkf12.practice;

public class switch2 {
    static void main() {
        int a = 10;
        int b = 20;
        String asdf = "*";

        int  result = switch(asdf){
          case "+" ->{
              int sum = a+b;
              yield sum;
          }
            case "-" ->{
                int sum = a-b;
                yield sum;
            }
            case "*" ->{
                int sum = a*b;
                yield sum;
            }
            case "/" ->{
                int sum = a/b;
                yield sum;
            }
          default -> {
                yield 0;
          }
        };
        System.out.println(result);
    }
}
