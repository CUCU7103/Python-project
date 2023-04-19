# 조건판단문 if 
from datashape.typesets import boolean

var = 10

if var >= 3: 
   # print('크구나') # 블럭의 위치를 맞추자.
   print('참일 때 수행')
   pass # 건너뛴다.
else:
    print('작네')
    
var2 = 6   
if var2 <= 4:
    print("참입니다.")
else: 
    print("거짓입니다.")   
          
print('ex1 end') # if문 블록 외부에 위치해 있다.

print()

money = 1000 
age = 23 

if money >= 500: # 참이몀 아래 수행 거짓이면 else로 넘어간다.
    item = '사과'
    if age < 30:
        msg = '영 하구만'
    else:
        msg = '올드'
else:
    item = '딸기'
    if age >= 20:
        msg = '김밥'
    else: 
        pass

print(item, msg)
print('ex2 end')

print("===" * 20)
# jumsu = int(input('점수입력 : ')) 기본적으로 키보드로 입력 받는 값은 str이므로 형변환이 필요하다.
jumsu = 78

if jumsu >= 90:
    print('우수')
elif jumsu >= 70: 
    print('보통')
else:
    print('저조')
    
print("===" * 20)

if 90 <= jumsu <=100:
    res = 5 
elif 70 <= jumsu < 90:
    res = 3
else: 
    res = 1
  
print('res : ' , res)   
print('res : ' + str(res)) # + 시 숫자를 문자로 변경해줘야한다. 자바는 '문자열 +' 은 문자열로 자동 형변환 되었지만 파이썬은 아니다.
print('ex3 end')

print()
names = ['길동', '순신', '기해']
if '길동' in names:
    print('내 친구야')
else:
    print('누구')
    
print("친구") if '길동' in names else print('누구') # if문 한 줄쓰기 진행한다.

print()
a = 'kbs'
b = 9 if a == 'kbs' else 11 # a가 참이면 if 왼쪽 값을 거짓이면 else문을 수행한다. if문 한 줄쓰기
print("b :" , b) # b : 9

a = 11
b = 'mbc' if a== 9 else 'kbs'
print('b :' ,b)  # b : kbs

a = 3
if a < 5: 
    print(0)
elif a <10:
    print(1)
else:
    print(2)

print(0 if a < 5 else 1 if a < 10 else 2) # 위의 조건문을 줄여씀. 보통 짧은 문장만 줄여쓴다.

print()

a = 6
aa = a * 2 if a > 5 else a + 2
print(aa) # 12

print(bool(True), bool(False))

a = 4   # 0    # 1
print((a + 2, a * 2)[a > 5])  # tuple과 조건이다. 조건이 참이면 1번째 거짓이면 0번째가 출력됨.

aa = '한번만'
print((aa + '이기자', aa +'도망가자')[aa=='한번만']) 



