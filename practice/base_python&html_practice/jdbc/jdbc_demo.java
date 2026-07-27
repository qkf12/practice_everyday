package com.qkf12.jdbc;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.Statement;

public class jdbc_demo {
    static void main() throws Exception {
        Class.forName("com.mysql.jdbc.Driver");
        String url = "jdbc:mysql://127.0.0.1:3306/practice";
        String user = "root";
        String password = "**********";
        Connection conn =  DriverManager.getConnection(url,user,password);
        String sql ="update course set credit = 5 where name = '高等数学'" ;

        Statement stmt = conn.createStatement();

        int i = stmt.executeUpdate(sql);

        System.out.println(i);

        stmt.close();
        conn.close();
    }
}
