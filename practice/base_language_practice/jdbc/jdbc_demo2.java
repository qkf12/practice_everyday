package com.qkf12.jdbc;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.Statement;
import java.util.ArrayList;

public class jdbc_demo2 {
    static void main() throws Exception {
//        注册
        Class.forName("com.mysql.jdbc.Driver");
//        登录
        String url = "jdbc:mysql://127.0.0.1:3306/practice";
        String user = "root";
        String password = "*****5.";
        Connection conn = DriverManager.getConnection(url, user, password);
//      mql 语言
        String sql ="select * from course";
//      接收对象
        Statement stmt = conn.createStatement();
//      执行sql语言
        ResultSet rs = stmt.executeQuery(sql);

        ArrayList list = new ArrayList();
        while (rs.next()) {
            subject su  = new subject();
            int id = rs.getInt("id");
            String name = rs.getString("name");
            int credit = rs.getInt("credit");
            su.setId(id);
            su.setName(name);
            su.setCredit(credit);
            list.add(su);
        }
        rs.close();
        stmt.close();
        conn.close();
        for(int i=0;i<list.size();i++){
            System.out.println(list.get(i));
        }
    }
}
