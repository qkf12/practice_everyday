package com.qkf12.jdbc.library_control_books;

public class book {
    private int book_id;
    private String book_name;
    private String book_author;
    private double book_price;
    private int book_quantity;

    public book(){}

    public book(int book_id, String book_name, String book_author, double book_price, int book_quantity) {
        this.book_id = book_id;
        this.book_name = book_name;
        this.book_author = book_author;
        this.book_price = book_price;
        this.book_quantity = book_quantity;
    }

    public int getBook_id() {
        return book_id;
    }

    public void setBook_id(int book_id) {
        this.book_id = book_id;
    }

    public String getBook_name() {
        return book_name;
    }

    public void setBook_name(String book_name) {
        this.book_name = book_name;
    }

    public String getBook_author() {
        return book_author;
    }

    public void setBook_author(String book_author) {
        this.book_author = book_author;
    }

    public double getBook_price() {
        return book_price;
    }

    public void setBook_price(double book_price) {
        this.book_price = book_price;
    }

    public int getBook_quantity() {
        return book_quantity;
    }

    public void setBook_quantity(int book_quantity) {
        this.book_quantity = book_quantity;
    }



    @Override
    public String toString() {
        return "book{" +
                "book_id='" + book_id + '\'' +
                ", book_name='" + book_name + '\'' +
                ", book_author='" + book_author + '\'' +
                ", book_price='" + book_price + '\'' +
                ", book_quantity=" + book_quantity +
                '}';
    }
}
