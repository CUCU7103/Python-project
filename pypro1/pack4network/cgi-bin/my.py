# 사용자가 입력한 자료 얻기 : get
import cgi

form = cgi.FieldStorage()
irum = form["name"].value
nai = form["age"].value 

print('''
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
<h2>파이썬 자료 출력</h2>
이름과 나이:{0},{1}
</body>
</html>
'''.format(irum,nai))
