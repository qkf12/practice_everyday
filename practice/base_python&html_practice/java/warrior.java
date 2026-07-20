package com.qkf12.practice;

public class warrior {
    public static void main(String[] args) {
//        我方英雄 叉子
        int my_ae = 220;
        int my_ac = 85;
        double my_hp = 1012.5;
        double my_aoe = 1.2;
//        敌方英雄 长手
        int you_ae = 210;
        int you_ac = 80;
        double you_hp = 1223.3;
        double you_aoe = 1.3;
//        技能造成伤害
        double hit1 = my_ae * my_aoe - you_ac;
//        普工造成伤害
        double hit2 = my_ae - you_ac;
//        1
        System.out.println(you_hp-hit2);
//      2
        you_hp = you_hp - hit2;
        System.out.println(you_hp-hit1);

    }
}
