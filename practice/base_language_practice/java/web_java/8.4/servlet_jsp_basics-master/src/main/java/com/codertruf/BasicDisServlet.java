package com.codertruf;

import java.io.IOException;
import java.io.PrintWriter;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@WebServlet("/basicDis")
public class BasicDisServlet extends HttpServlet {
	public void service(HttpServletRequest req, HttpServletResponse res) throws IOException, ServletException{
		res.setContentType("text/html");		
		
		PrintWriter out = res.getWriter();
		String title = "Basic visual page ";
		String docType = "<! doctypte html public \"-//w3c//dtd html 4.0 " + "transitional//en\">\n";
		out.println(docType+
				"<html>\n"+
					"<head><title>"+title+"</title></head>"+
					"<body bgcolor=\"#f0f0f0\">\n"+
						"<h1 align = \"center\">" + title+"</h1> \n"+
						"<ul>\n"+
							"<li><b>First Name</b> :"+
							req.getParameter("firstName") + "\n"+
							"<li><b>Last Name</b> : "+
							req.getParameter("lastName") + "\n"+
						"</ul>\n"+
					"</body>"+
				"</html>"
				
				
				);
		
	}
}
