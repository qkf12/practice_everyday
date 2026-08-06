package com.codertruf;

import java.io.IOException;
import java.io.PrintWriter;

import javax.servlet.ServletConfig;
import javax.servlet.ServletContext;
import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;

public class SqrdSumServlet extends HttpServlet {
	
	public void service(HttpServletRequest req, HttpServletResponse res) throws IOException, ServletException{
		int i = squareNum(Integer.parseInt(req.getParameter("num1")));
		int j = squareNum(Integer.parseInt(req.getParameter("num2")));
		int k = i + j;
		
		PrintWriter out = res.getWriter();
		out.println("The squared Sum or the two numbers are : "+k);
		
		
		
		// Servlet context 
		ServletContext ctx = getServletContext();
		String name = ctx.getInitParameter("name");
		
		
		//Servelte config
		ServletConfig cfg = getServletConfig();
		String rollNo = cfg.getInitParameter("Roll No");
		String phone = cfg.getInitParameter("Phone");
		out.println("   Name :   "+ name);
		out.println("   Roll No :   "+rollNo);
		out.println("   Phone  :   "+phone);
		res.sendRedirect("sqrdProd");
		
		
		
		
	}
	
	public static int squareNum(int n) {
		return n*n;
	}

}
