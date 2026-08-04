package com.codertruf;

import java.io.IOException;
import java.io.PrintWriter;

import javax.servlet.ServletException;
import javax.servlet.http.Cookie;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;



public class AddServlet extends HttpServlet {
	
	public void doPost(HttpServletRequest req, HttpServletResponse res) throws IOException {
		int i = Integer.parseInt(req.getParameter("num1"));
		int j = Integer.parseInt(req.getParameter("num2"));
		
		int k = i+j;
		PrintWriter out = res.getWriter();
		out.println(i+" + "+j+" = "+k);
		
	}
	public void service(HttpServletRequest req, HttpServletResponse res) throws IOException, ServletException{
		int i = Integer.parseInt(req.getParameter("num1"));
		int j = Integer.parseInt(req.getParameter("num2"));
		
		int k = i*j;
		PrintWriter out = res.getWriter();
		out.println(i+" * "+j+" = "+k);
		
		 	
		
		//initializing the session for storing the data throughout the application
		HttpSession session = req.getSession();
		session.setAttribute("i", i);
		session.setAttribute("j", j);
		// now we can access the variables i and j from anywhere from the application
		// in session the data is stored in server 
		
		req.setAttribute("x", 10);
		
		res.sendRedirect("sqrdSum?num1="+i+"&num2="+j);		//URL rewriting 
		
		
		//initializing cookies
		Cookie token1 = new Cookie("i", i+"");
		Cookie token2 = new Cookie("j", j+"");
		
		res.addCookie(token2);
		res.addCookie(token1);
		
		
		
		
		
//		RequestDispatcher rd2 = req.getRequestDispatcher("sqrdSum");
//		rd2.forward(req, res);
		
//		RequestDispatcher rd = req.getRequestDispatcher("sq");
//		rd.forward(req, res);
		
		
	}
}
