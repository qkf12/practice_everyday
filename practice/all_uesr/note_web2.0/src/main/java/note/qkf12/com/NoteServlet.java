package note.qkf12.com;

import jakarta.servlet.ServletException;
import jakarta.servlet.annotation.WebServlet;
import jakarta.servlet.http.HttpServlet;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.io.IOException;
import java.sql.*;
import java.util.ArrayList;
import java.util.List;

@WebServlet("/api/*")  // 所有 /api/ 开头的请求都走这里
public class NoteServlet extends HttpServlet {

    private static final String URL = "jdbc:mysql://127.0.0.1:3306/practice";
    private static final String USER = "root";
    private static final String PASSWORD = "Qkf070425.";

    private Connection getConnection() throws SQLException {
        return DriverManager.getConnection(URL, USER, PASSWORD);
    }

    // servlet 初始化时加载一次 MySQL 驱动，保证 doGet/doPost/doDelete 都能连库
    @Override
    public void init() throws ServletException {
        try {
            Class.forName("com.mysql.cj.jdbc.Driver");
            System.out.println("✅ MySQL 驱动已加载 (init)");
        } catch (ClassNotFoundException e) {
            throw new ServletException("MySQL JDBC 驱动加载失败", e);
        }
    }

    // ========== GET /api/list = 查询所有 ==========
    @Override
    protected void doGet(HttpServletRequest req, HttpServletResponse resp)
            throws ServletException, IOException {
        String path = req.getPathInfo();
        resp.setContentType("application/json;charset=UTF-8");

        if ("/list".equals(path)) {
            try (Connection conn = getConnection();
                 PreparedStatement stmt = conn.prepareStatement("SELECT date,type,money FROM note");
                 ResultSet rs = stmt.executeQuery()) {

                List<String> jsonItems = new ArrayList<>();
                while (rs.next()) {
                    jsonItems.add(String.format(
                            "{\"date\":\"%s\",\"type\":\"%s\",\"money\":%.2f}",
                            rs.getString("date"),
                            rs.getString("type"),
                            rs.getDouble("money")
                    ));
                }
                String json = "[" + String.join(",", jsonItems) + "]";
                resp.getWriter().write(json);

            } catch (SQLException e) {
                resp.setStatus(500);
                resp.getWriter().write("{\"error\":\"" + e.getMessage() + "\"}");
                e.printStackTrace();
            }
        } else {
            resp.setStatus(404);
            resp.getWriter().write("{\"error\":\"Not Found\"}");
        }
    }

    // ========== POST /api/add = 添加一条 ==========
    @Override
    protected void doPost(HttpServletRequest req, HttpServletResponse resp)
            throws ServletException, IOException {

        req.setCharacterEncoding("UTF-8");

        // 在 doPost 或 init 开头加上：
        try {
            Class.forName("com.mysql.cj.jdbc.Driver");
            System.out.println("✅ 驱动类加载成功！");
        } catch (ClassNotFoundException e) {
            System.out.println("❌ 驱动类加载失败：" + e.getMessage());
            e.printStackTrace();
        }

        // 从请求体读取 JSON（这里简化为从参数读取）
        String date = req.getParameter("date");
        String type = req.getParameter("type");
        String moneyStr = req.getParameter("money");

        resp.setContentType("application/json;charset=UTF-8");

        if (date == null || type == null || moneyStr == null) {
            resp.setStatus(400);
            resp.getWriter().write("{\"success\":false,\"msg\":\"参数不全\"}");
            return;
        }

        try (Connection conn = getConnection();
             PreparedStatement stmt = conn.prepareStatement(
                     "INSERT INTO note (date, type, money) VALUES (?, ?, ?)")) {
            stmt.setString(1, date);
            stmt.setString(2, type);
            stmt.setDouble(3, Double.parseDouble(moneyStr));
            int rows = stmt.executeUpdate();
            resp.getWriter().write("{\"success\":" + (rows > 0) + "}");
        } catch (Exception e) {
            resp.setStatus(500);
            resp.getWriter().write("{\"success\":false,\"msg\":\"" + e.getMessage() + "\"}");
            e.printStackTrace();
        }
    }

    // ========== DELETE /api/delete = 按日期删除 ==========
    @Override
    protected void doDelete(HttpServletRequest req, HttpServletResponse resp)
            throws ServletException, IOException {
        String date = req.getParameter("date");
        resp.setContentType("application/json;charset=UTF-8");

        if (date == null) {
            resp.setStatus(400);
            resp.getWriter().write("{\"success\":false,\"msg\":\"缺少日期参数\"}");
            return;
        }

        try (Connection conn = getConnection();
             PreparedStatement stmt = conn.prepareStatement(
                     "DELETE FROM note WHERE date = ?")) {
            stmt.setString(1, date);
            int rows = stmt.executeUpdate();
            resp.getWriter().write("{\"success\":" + (rows > 0) + "}");
        } catch (Exception e) {
            resp.setStatus(500);
            resp.getWriter().write("{\"success\":false,\"msg\":\"" + e.getMessage() + "\"}");
            e.printStackTrace();
        }
    }
}