<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8" isErrorPage="true"%>
<!DOCTYPE html>
<html>
<head>
	<meta charset="UTF-8">
	<title>Insert title here</title>
	<style>
		body{
			background-color:#ff4 d4d;
			margin:0;
			padding:0;
			height = 50px;
			max-height:400px;
			overflow:hidden;
			
		}
	</style>
</head>
<body>
	<h4>Error</h4>
	<%=exception.getMessage() %>
</body>
</html>