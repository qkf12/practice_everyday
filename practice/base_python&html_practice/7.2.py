import requests

url = "https://my.4399.com/account/login?refer=http%3A%2F%2Fmy.4399.com%2Fforums%2Fmtags&loginRealNameLevel=0&loginRealNameLoginLevel=60&loginRealNameRegLevel=4&bizId=1199006632"

headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36 Edg/145.0.0.0"
}
data ={
    "password":"Qkf070425.",
    "username":"3902124849"

}

response = requests.post(url = url, headers=headers, data = data)

cookie_ = response.cookies
print(response.text)



















