package com.qkf12.jdbc;

import java.sql.*;

public class jdbc_users {
    static void main() throws Exception {
        Class.forName("com.mysql.jdbc.Driver");

        String url = "jdbc:mysql://127.0.0.1:3306/practice";;
        String user = "root";
        String password = "***.";
        Connection conn = DriverManager.getConnection(url, user, password);
//      用户输入
        String user_name = "张三";
        String user_password = "123";

        String sql = "select * from users where user = ? and password = ?";

        PreparedStatement pstmt = conn.prepareStatement(sql);

        pstmt.setString(1, user_name);
        pstmt.setString(2, user_password);

        ResultSet rs = pstmt.executeQuery();

        if (rs.next()) {
            System.out.println("登录成功");
        }else {
            System.out.println("登陆录失败");
        }
        rs.close();
        pstmt.close();
        conn.close();
    }
}
