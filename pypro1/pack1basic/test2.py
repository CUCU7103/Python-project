# 연산자, 기타
v1 = 3 # 치환
v1 = v2 = v3 =5 
print(v1,v2,v3) # 5 5 5
 
v1 , v2 = 2 , 3 
print(v1, v2) # 2 3

v1, *v2 = 1,2,3,4,5 #  값 할당 packing 연산
*v1, v2 = 1,2,3,4,5 # [1, 2, 3, 4] 5
*v1, v2 , v3 = 1,2,3,4,5 # [1, 2, 3] 4 5
#  *v1, v2 , *v3 = 1,2,3,4,5  값 할당 packing 연산은 한개만 가능하다. 처음이나 마지막에만 사용이 가능하다.
print(v1, v2 ,v3) 
print(v1) # [1, 2, 3]

#======================================================================================================================

print('산술연산자')
print(5 + 3, 5 - 3, 5 * 3, 5 / 3, 5 // 3, 5 % 3, 5 ** 2) # 8 2 15 1.6666666666666667 1 2 25
#     더하기 빼기    곱하기  나누기  몫  나머지 거듭제곱
print(3 + 4 * 5, (3 + 4)* 5) # 23  /  35
# 연산자 우선순위 : 괄호 () , 산술( * , /  > + , -) > 관계연산자 >  논리연산자 > = (치환연산자)

#======================================================================================================================

print('관계연산자', end=' 개행취소') 
# end는 기본적인 line skip을 생략한다 end=''에서 '' 안에 원하는 내용을 기입가능하다.
print(' 살펴보기')  # 관계연산자 개행취소 살펴보기
print(5 > 3, 5 == 3, 5 != 3)
#======================================================================================================================

print('논리연산자') 
print(5 > 4 and 4 < 3 , 5 > 4 or 4 < 3 , not(3>=2))
#======================================================================================================================

print('문자열 더하기')
print('한' + '국' + '인 만세')
print(4 * 10)  # 40
print('4'  * 10) # 4444444444 문자열을 10번 더한것 기본적으로 디지털 컴퓨터는 더하기 연산진행

#======================================================================================================================

print('누적')
a = 5 
a = a + 1
a += 1
# a++ 증감연산자 사용이 불가능하다.
++a # 의미가 없다 a와 동일하다.
print("a : " , a)

print(a , a * -1, -a, --a) # - 는 부호 변경으로 사용된다. / 7 -7 -7 7
print(bool(True), bool(1), bool(-2.5), bool('kbs')) 
# True 0이외의 수이거나 비어있지 않으면 true
print(bool(False), bool(0) ,bool(0.0), bool(""), bool([]), bool({}),bool(None)) 
# False 0이거나 비어 있으면 false이다

# 참고 1=============================================
print('이스케이프 문자 ')
print('aa\tbb') # aa    bb
print(r'aa\tbb') # 선행문자 r은 이스케이프 기능을 무시한다.  aa\tbb
print('aa\nbb')  # \n은 개행기능
print(r'aa\nbb')  # 선행문자 r은 이스케이프 기능을 무시한다 aa\nbb
print('c:\aa\bb\nbc\tbc') 
print(r'c:\aa\bb\nbc\tbc')  # 파일경로 지정할 때 사용함.

# 참고 2=============================================
# 포맷 코드 사용
# "문자열 %s 문자열" %출력값
print(format(123.45678, '10.3f'))
print('{0:.3f}'.format(1.0/3)) # 0.333
print('서식에 의한 자료 출력 %s %d %f'%('문자열', 5, 23.4)) 
# 서식에 의한 자료 출력 문자열 5 23.400000
print('이름:{1}, 가격:{0}'.format(5000, '마우스'))
# formatoe은  순서를 지정할 수 있다.
print('이름:{1}, 가격:{0} {0} {0}'.format('마우스', 5000))
print(format(1.5678, '10.3f'))
print ()

print('나는 나이가 %d 이다.' %23) 
print('나는 나이가 %s 이다.' %'스물셋')
print('나는 나이가 %d 이고 이름은 %s이다.' %(23, '홍길동'))
print('나는 나이가 %s 이고 이름은 %s이다.' %(23, '홍길동'))
print('나는 키가 %f이고, 에너지가 %d%%.' %(177.7, 100))
print('이름은 {0}, 나이는 {1}'.format('한국인', 33))
print('이름은 {}, 나이는 {}'.format('신선해', 33))
print('이름은 {1}, 나이는 {0}'.format(34, '강나루'))


print('''
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠤⠖⠚⠉⠉⠀⠀⠀⠀⠉⠉⠙⠒⠤⣄⡀⠀⠀⣀⣠⣤⣀⡀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠖⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⢯⡀⠀⠀⠀⠉⠳⣄⠀
⠀⠀⣀⠤⠔⠒⠒⠒⠦⢤⣀⢀⡴⠋⠀⠀⠀⠀⠀⠀⠀⠀⢠⣤⣄⠀⠀⠀⠀⠀⣴⢶⣄⠀⠀⠀⠉⢢⡀⠀⠀⠀⠘⡆
⢠⠞⠁⠀⠀⠀⠀⠀⠀⠀⠈⢻⡀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡟⠀⢹⣧⠀⠀⠀⠀⣿⠀⢹⣇⠀⠀⠀⠀⠙⢦⠀⠀⠀⣧
⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣦⣼⣿⡇⠀⠀⠀⢿⣿⣿⣿⡄⠀⠀⠀⠀⠈⢳⡀⢀⡟
⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡸⠁⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⡿⠿⠿⣿⠀⠀⠀⠘⣿⡛⣟⣧⠀⠀⠀⠀⠀⠀⢳⠞⠀
⢳⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣷⡄⢴⡿⠀⠀⠀⠀⠘⣿⣷⡏⠀⢀⡠⠤⣄⠀⠀⣇⠀
⠀⢳⡀⠀⠀⠀⠀⠀⠀⢠⠏⠀⠀⠀⠀⠀⣠⠄⠀⠀⠀⠀⠀⠈⠛⠛⠁⣀⡤⠤⠤⠤⢌⣉⠀⠀⢠⡀⠀⠀⡱⠀⢸⡄
⠀⠀⠙⠦⣀⠀⠀⠀⣰⠋⠀⠀⠀⠀⠀⠸⣅⠀⠀⢀⡀⠀⠀⠀⢀⠴⠋⠀⠀⠀⠀⠀⠀⠈⠳⣄⠀⠈⠉⠉⠀⠀⢘⣧
⠀⠀⠀⠀⠈⠙⢲⠞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠁⠀⠀⠀⣰⣋⣀⣀⣀⣀⠀⠀⠀⠀⠀⠀⠈⢧⠀⠀⠀⠀⠀⢐⣿
⠀⠀⠀⠀⠀⠀⢸⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡰⠁⠀⠀⠀⠀⠀⠉⠙⠒⢤⣀⠀⠀⠈⣇⠀⠀⠀⠀⠀⣿
⠀⠀⠀⠀⠀⠀⠘⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠳⣄⠀⢸⠀⠀⠀⠀⢠⡏
⠀⠀⠀⠀⠀⠀⠀⢳⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⡆⠘⣧⠀⠀⠀⣸⠀
⠀⠀⠀⠀⠀⠀⠀⡟⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢱⢰⠏⠀⠀⢠⠇⠀
⠀⠀⠀⠀⠀⠀⢸⠁⠘⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡼⣸⠀⠀⢀⠏⠀⠀
⠀⠀⠀⠀⠀⠀⣿⠀⠀⠘⢆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡴⣣⠃⠀⣠⠏⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠈⠳⣄⠀⠀⠀⠀⠀⠀⠀⠀⠘⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡤⠞⡱⠋⢀⡴⠁⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠈⠣⣄⠀⠀⠀⠀⠀⠀⠀⠹⣄⠀⠀⠀⠀⢀⣀⡤⠖⢋⡠⠞⢁⡴⠋⡇⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠸⡄⠀⠀⠀⠀⠀⠀⠈⠙⠢⣄⡀⠀⠀⠀⠀⠈⠙⠯⠭⢉⠡⠤⠴⠒⣉⠴⠚⠁⠀⢰⠃⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢳⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢹⠖⠲⠤⠤⠤⠤⠤⠤⢶⡖⠚⠉⠀⠀⠀⠀⢀⡞⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢳⡀⠀⠀⠀⠀⠀⠀⠀⠀⡰⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠲⠤⠤⠤⠤⠔⠋⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢤⡀⠀⠀⠀⠀⣠⠞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠛⠑⠒⠒⠋⠂⠐⠒⠀⠀⠒⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
''')
