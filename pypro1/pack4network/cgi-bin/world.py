s1 = '자료 1'
s2 = '두번째 자료'

# /   : 루트
# ./  : 현재 위치 
# ../ : 현재 위치의 상단 폴더

print('''
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
<h2>파이썬 자료 출력</h2>
자료 출력 :{0},{1}
</br>
<a href="../index.html">
    <img src="../images/aaa.png" width = 60% /> (하이퍼 이미지)
</a>
</body>
</html>
'''.format(s1,s2))