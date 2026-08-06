<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8" errorPage="error.jsp"%>
    
    <!-- some import -->
    <%@ page import="java.util.*" %>
    <%@ page import="java.util.ArrayList, java.util.Scanner" %>
    <!-- import is the only attribute that we can have multiple times in directive -->
    
    
    <!-- Include that file before the below content  -->
    <!-- Here we include the header file -->
    <%@ include file="header.jsp" %>

<!DOCTYPE html>
<html>
<head>
	<meta charset="UTF-8">
	<title>Easy Visual By JSP</title>
	<style>
		body{
			margin:0;
			padding:0;
		}
		a {
			text-decoration:none;
		}
	</style>
</head>

<body bgcolor="#c8c8c8">
	<h1 align="center">Easy Visual By JSP</h1>

	<%
		String firstName = request.getParameter("firstName");
		String lastName = request.getParameter("lastName");
		session.setAttribute("user", "Prakash");
	%>

	<ul>
		<li> First Name : <%= firstName %></li>
		<li> Last Name : <%= lastName %></li>
		<br>
		<li> Full Name : <b> ${param.firstName} ${param.lastName}</b> </li>
		<br>
		<h3><%=session.getAttribute("user") %></h3>
		<br>
		<h4><a href="sq">Go To sq</a></h4>
	</ul>
	
	
	<!-- Let's try some exception handling  and above mentioned @ page  -->
	<%
		/* int i = 9/0; */
	%>
	
	

</body>
</html>
