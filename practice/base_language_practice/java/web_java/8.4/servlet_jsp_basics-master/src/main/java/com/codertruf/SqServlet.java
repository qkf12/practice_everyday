package com.codertruf;

import java.io.IOException;
import java.io.PrintWriter;

import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;

public class SqServlet extends HttpServlet {
	public void service(HttpServletRequest req, HttpServletResponse res) throws IOException {
		int i = Integer.parseInt(req.getParameter("num1"));
//		int j = Integer.parseInt(req.getParameter("num2"));
		int sqr= i*i;
		
		// getting the value form session
		HttpSession session = req.getSession();
		int k = (int)session.getAttribute("i");
		
		//removing the value form the session
		session.removeAttribute("i");
		//only the 'i' is removed 'j' is still present in the session
		
		int sqrPlus1 = k+1;
		PrintWriter out = res.getWriter();
		out.println(i+" ^ 2 = "+sqr);
		
		out.println(k+" + 1 = "+sqrPlus1);
		
		//session
//				HttpSession session = req.getSession();
				String userName = (String) session.getAttribute("user");
				out.println(userName);
		
		
	}
}
