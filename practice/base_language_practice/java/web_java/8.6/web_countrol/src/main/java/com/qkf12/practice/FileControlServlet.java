package com.qkf12.practice;  // 你的包名

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.*;
import java.nio.charset.StandardCharsets;
import java.nio.file.*;

@WebServlet("/file-op")
public class FileControlServlet extends HttpServlet {

    // ⚠️ 这里改成你要控制的文件路径（绝对路径）
    private static final String FILE_PATH = "C:/Users/32738/Desktop/practice/sun.txt";

    @Override
    protected void doGet(HttpServletRequest req, HttpServletResponse resp)
            throws ServletException, IOException {

        String action = req.getParameter("action");
        resp.setContentType("text/plain;charset=UTF-8");

        if ("read".equals(action)) {
            // 读取文件内容并返回给前端
            try {
                String content = new String(Files.readAllBytes(Paths.get(FILE_PATH)), StandardCharsets.UTF_8);
                resp.getWriter().write(content);
            } catch (NoSuchFileException e) {
                resp.getWriter().write("文件不存在，请先保存内容");
            } catch (Exception e) {
                resp.getWriter().write("读取失败：" + e.getMessage());
            }
        } else {
            resp.getWriter().write("未知操作");
        }
    }

    @Override
    protected void doPost(HttpServletRequest req, HttpServletResponse resp)
            throws ServletException, IOException {

        String action = req.getParameter("action");
        resp.setContentType("text/plain;charset=UTF-8");

        if ("write".equals(action)) {
            // 获取前端提交的内容
            String content = req.getParameter("content");
            if (content == null) {
                resp.getWriter().write("内容为空");
                return;
            }
            try {
                // 覆盖写入文件
                Files.write(Paths.get(FILE_PATH), content.getBytes(StandardCharsets.UTF_8));
                resp.getWriter().write("保存成功");
            } catch (Exception e) {
                resp.getWriter().write("保存失败：" + e.getMessage());
            }
        } else {
            resp.getWriter().write("未知操作");
        }
    }
}