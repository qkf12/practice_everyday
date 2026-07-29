package com.qkf12.practice2;

public class food {
    private String name;
    private double price;
    private String introduction;
    public food(){}

    public food(String name,double price, String introduction ) {
        this.price = price;
        this.introduction = introduction;
        this.name = name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getName() {
        return name;
    }

    public void setPrice(double price) {
        this.price = price;
    }

    public double getPrice() {
        return price;
    }

    public void setIntroduction(String introduction) {
        this.introduction = introduction;
    }

    public String getIntroduction() {
        return introduction;
    }


}
