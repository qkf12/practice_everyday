package com.codertruf;

import java.io.IOException;
import java.io.PrintWriter;

import javax.servlet.ServletConfig;
import javax.servlet.ServletContext;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.Cookie;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;

@WebServlet("/sqrdProd")
public class SqrdProductServlet extends HttpServlet {
	
	public void service(HttpServletRequest req, HttpServletResponse res) throws IOException, ServletException  {
		
		//getting the first number from the session
		HttpSession session = req.getSession();
		int j = (int) session.getAttribute("j");
		// we cannot get the 'i' from the session as it was deleted from the session in '/sqAdd'
		
		
		// getting the number 'i' from cookies
		int i = 0;
		Cookie cookies[] = req.getCookies();
		for(Cookie cookie : cookies) {
			if(cookie.getName().equals('i')) {
				j = Integer.parseInt(cookie.getValue());
			}
		}
		
		int sqrdProd = square(i) * square(j);
		
		
		//printing the output on the web page
		PrintWriter out = res.getWriter();
		out.println(i+"^2   X   "+j+"^2   =   "+sqrdProd);
		out.println("bye");
		// Servlet context 
				ServletContext ctx = getServletContext();
				String name = ctx.getInitParameter("name");
				String rollNo = ctx.getInitParameter("Roll No");
				
				
				//Servelte config
				ServletConfig cfg = getServletConfig();
				String phone = cfg.getInitParameter("Phone");
				out.println("   Name :   "+ name);
				out.println("   Roll No :   "+rollNo);
				out.println("   Phone  :   "+phone);
				out.println("<div>");
		
	}
	public int square(int i ) {
		return i*i;
	}
}
