package com.qkf12.jdbc.library_control_books;

import jdk.swing.interop.SwingInterOpUtils;

import java.sql.*;
import java.text.BreakIterator;
import java.util.ArrayList;
import java.util.Scanner;


public class function  {
     public static  Scanner sc ;
     public static  Connection conn;
     public static final String url = "jdbc:mysql://127.0.0.1:3306/practice";
     public static final String user = "root";
     public static final String password = "............5.";


//    1，先上架所知道的书籍
//    2，增删改查

//     Scanner sc = new Scanner(System.in);
//            程序执行的时候 就开始登录sql   等到执行5功能时再执行  资源释放
//    String url = "jdbc:mysql://127.0.0.1:3306/library_control_books";
//    String user = "root";
//    String password = "Qkf888.";
//     conn = DriverManager.getConnection(url, user, password);


//    ========================主框架===================================
    public static void main_boots() {
        try {
            conn = DriverManager.getConnection(url, user, password);
            sc = new Scanner(System.in);
            System.out.println("数据库连接成功");
            main_function();
        }catch(Exception e){
            e.printStackTrace();
        }finally {
            try {
                if(conn!=null){
                    conn.close();
                }
//                if(sc!=null){
//                    sc.close();
//                }
            }catch(Exception e){
                e.printStackTrace();
            }
        }
    }


//===============================主程序===========================================
    public static void main_function()  {

            while (true){
                System.out.println("----欢迎来到图书馆管理系统终端----");
                System.out.println("1,上架图书");
                System.out.println("2,删除图书");
                System.out.println("3,更改图书");
                System.out.println("4,查看图书");
                System.out.println("5,退出系统");
                String choice = sc.next();
                switch (choice){
                    case "1":
                        one_function();
                        break;
                    case "2":
                        two_function();
                        break;
                    case "3":
                        three_function();
                        break;
                    case "4":
                        four_function();
                        break;
                    case "5":
                        System.out.println("欢迎下次使用，拜拜！！");
                        return;
                    default:
                        System.out.println("请输入正确的功能按键哈");
                        break;
                }
            }
    }
    //  =====================================功能区域===========================


//        第一个功能  上架新书
    public static void one_function()  {
        while(true){
            System.out.println("----欢迎进入上架图书环节（也可为还书）----");
            System.out.println("请输入图书的id");
            int id = sc.nextInt();
            System.out.println("请输入图书的名字");
            String name = sc.next();
            System.out.println("请输入图书的作者");
            String author = sc.next();
            System.out.println("请输入图书的价格");
            double book_price = sc.nextDouble();
            System.out.println("请输入图书的库存");
            int book_quantity = sc.nextInt();
            String sql ="insert into library_control_books  values(?,?,?,?,?)";

            try(PreparedStatement pstmt = conn.prepareStatement(sql)) {
                pstmt.setInt(1,id);
                pstmt.setString(2,name);
                pstmt.setString(3,author);
                pstmt.setDouble(4,book_price);
                pstmt.setInt(5,book_quantity);

                int rows = pstmt.executeUpdate();
                if(rows>0){
                    System.out.println("书籍上架成功");
                }else {
                    System.out.println("书籍上架未成功");
                }
                System.out.println("您是准备重新输入(1)还是退出这个功能(2)呀？");
                String select = sc.next();
                switch (select){
                    case "1":
                        break;
                    case "2":
                        return;
                    default:
                        System.out.println("那我默认您要重新输入哈");
                        break;
                }
            }catch(Exception e){
                e.printStackTrace();
            }
        }
    }

//===================第二个功能============
    public static void two_function()  {
        while (true){
            System.out.println("请输入您要删除的图书名字");
            String name = sc.next();
            String sql =  "delete from library_control_books where book_name = ?";
            try (PreparedStatement pstmt = conn.prepareStatement(sql)){
                pstmt.setString(1,name);
                int rows = pstmt.executeUpdate();
                if(rows>0){
                    System.out.println("删除成功");
                }else {
                    System.out.println("删除未成功");
                }
                System.out.println("您是准备重新输入(1)还是退出这个功能(2)呀？");
                String select = sc.next();
                switch (select){
                    case "1":
                        break;
                    case "2":
                        return;
                    default:
                        System.out.println("那我默认您要重新输入哈");
                        break;
                }
            }catch(Exception e){
                e.printStackTrace();
            }
        }
    }

//    ========================第三个功能====================
    public static void three_function()  {
        while (true){
            System.out.println("请输入你要更改的功能");
            System.out.println("1,修改图书价格\n 2,修改图书库存");
            String fun = sc.next();
            if("1".equals(fun)){
                System.out.println("请输入你要修改价格的图书名字");
                String name = sc.next();
                System.out.println("请输入新的价格");
                double price = sc.nextDouble();
                String sql = "update library_control_books set book_price = ? where book_name = ?";
                try (PreparedStatement pstmt = conn.prepareStatement(sql)) {
                    pstmt.setString(1,name);
                    pstmt.setDouble(2,price);
                    int rows = pstmt.executeUpdate();
                    if(rows>0){
                        System.out.println("删除成功");
                    }else {
                        System.out.println("删除未成功");
                    }
                    System.out.println("您是准备重新输入(1)还是退出这个功能(2)呀？");
                    String select = sc.next();
                    switch (select){
                        case "1":
                            break;
                        case "2":
                            return;
                        default:
                            System.out.println("那我默认您要重新输入哈");
                            break;
                    }
                }catch(Exception e){
                    e.printStackTrace();
                }
            }else if("2".equals(fun)){
                System.out.println("请输入你要修改价格的图书名字");
                String name = sc.next();
                System.out.println("请输入新的库存");
                int quantity = sc.nextInt();
                String sql = "update library_control_books set book_price = ? where book_name = ?";
                try (PreparedStatement pstmt = conn.prepareStatement(sql)) {
                    pstmt.setString(1,name);
                    pstmt.setDouble(2,quantity);
                    int rows = pstmt.executeUpdate();
                    if(rows>0){
                        System.out.println("删除成功");
                    }else {
                        System.out.println("删除未成功");
                    }
                    System.out.println("您是准备重新输入(1)还是退出这个功能(2)呀？");
                    String select = sc.next();
                    switch (select){
                        case "1":
                            break;
                        case "2":
                            return;
                        default:
                            System.out.println("那我默认您要重新输入哈");
                            break;
                    }
                }catch(Exception e){
                    e.printStackTrace();
                }
            }else{
                System.out.println("请输入正确的功能哈！！");
                break;
            }
        }
    }

//    =======================第四个功能============================
    public static void four_function()  {
        System.out.println("=======一下是图书的全部信息=========");
         String sql = "select * from library_control_books ";
         try (PreparedStatement pstmt = conn.prepareStatement(sql)) {
             ResultSet rs = pstmt.executeQuery();
             System.out.println("ID\t书名\t\t作者\t\t价格\t库存");
             while(rs.next()){
                 int  id = rs.getInt("book_id");
                 String name = rs.getString("book_name");
                 String author = rs.getString("book_author");
                 double book_price = rs.getDouble("book_price");
                 int book_quantity = rs.getInt("book_quantity");
                 System.out.printf("%d\t%s\t%s\t%.2f\t%d\n",id, name, author, book_price, book_quantity);

             }
         }catch(Exception e){
             e.printStackTrace();
         }
    }

//                        rs.close();
//                        stmt.close();
//                        conn.close();
}
