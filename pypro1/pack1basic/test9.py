# 반복문 for
# 형식 for target in object\

for i in [1,2,3,4,5]:
    print(i, end= ' ')
     # 1 2 3 4 5 
print()  
for i in (1,2,3,4,5):
    print(i, end= ' ')
    # 1 2 3 4 5 
print()
for i in {1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,1,2,3,4,5}: # ㄴset은 중복값을 허용하지 않는다.
    print(i, end= ' ')
    
print()
soft = {'java' : '웹용언어', 'python' : '만능언어', 'mariadb' : 'db'}
for i in soft.items(): # item을 사용하게 되면 key-value를 tuple 형식으로 변환한다
    print(i, end=' ,')  # ('java', '웹용언어') ...
    print(i[0] + ' ' + i[1]) # java 웹용언어
    
print()
for k in soft.keys():
    print(k, end= ' ') # key만 출력함 java python mariadb

print()
for v in soft.values():
    print(v, end= ' ') # value만 출력함. 웹용언어 만능언어 db
    
print()
for k, v in soft.items(): # 'java' : '웹용언어' .. 순서대로 k,y에 들어간다.
    print('k: ',k) # key 값
    print(v) # value 값

print()
color = ['r','g','b']
it = iter(color)  # iterator(반복자)
print(next(it))   # r 포인터가 하나씩 이동한다.
print(next(it))   # g
print(next(it))   # b
print()

it = iter(color)
for imsi in it: # next로 돌린것과 동일한 결과가 나온다
    print(imsi, end=' ') # r g b

for idx, data in enumerate(color): #  enumerate를 사용하여 인덱스를 얻을 수 있다.
    print('\n인덱스: {}'.format(idx),', 값:{}'.format(data)) # 인덱스:  0 , 값: r
    
print('구구단 출력함.')
for n in [2,3]:
    print('--{}단--'.format(n))
    # for i in [1,2,3,4,5,6,7,8,9]:
    for i in range(1,10): # range 사용가능함.
        print('{0}*{1} = {2}'.format(n,i,n*i))
    
print()
datas = [1,2,3,4,5]
for i in datas:
    if i == 3:
        continue
    if i == 4:
        break # break는 강제종료이다.
    print(i, end =' ') 
else: 
    print('for 정상종료') 

print()
jumsu = [95,70,60,50,100]
number = 0 
for jum in jumsu: 
    number += 1
    if jum < 70:continue
    print('%d번째 합격' %number)
    
print('for + 정규표현식 사용하기 : 단어 빈도수 출력')
import re

ss ="""유희동 기상청장은 11일 국회에서 열린 제2회 국가현안 대토론회 기조 발제를 통해 탄소 감축 없는 고탄소 시나리오를 따라 개발이 진행될 경우 유희동 기상청장은 11일 국회에서 열린 제2회 국가현안 대토론회 기조 발제를 통해 탄소 감축 없는 고탄소 시나리오를 따라 개발이 진행될 경우 
2100년경 우리나라 기온은 산업혁명 이전 대비 6.3도 상승할 것이라고 전망했다.
2100년경 우리나라 기온은 산업혁명 이전 대비 6.3도 상승할 것이라고 전망했다."""

ss2 =re.sub(r'[^가-힝\s]','',ss) 
# re.sub 정규 표현식을 사용하여 문자열에서 특정 패턴을 찾아 다른 문자열로 치환하는 함수
# 첫 번째 인수로는 정규 표현식 패턴, 두 번째 인수로는 바꿀 문자열, 세 번째 인수로는 대상 문자열을 입력받습니다
# 한글과 공백을 제외한 나머지 공백처리 진행, 즉 한글하고 공백만 보이도록 한다.
print(ss2)

ss3 = ss2.split(' ') # 지정한 구분자로 분리하여 list 형식으로 반환한다.
print(ss3)
print(len(ss3))

cou = {} # 단어의 발생빈도를 dict로 저장
for i in ss3:
    if i in cou: # 중복된 단어(key)가 있으면 value 증가
        cou[i] += 1
    else:
        cou[i] = 1
        
print(cou)

print()
for test_str in ['111-1234', '일이삼- 사오육칠','222-1234']:
    # 처음(^) 정수 3개 - 정수 4개로 끝나는($) 패턴
    if re.match(r'^\d{3}-\d{4}$', test_str):
        print(test_str,'전화번호 맞네')
    else:
        print(test_str,'이건 어째....')

print('\n\nfor문 comprehension 기능 연습')
l1 = [3,4,5]
l2 = [0.5,1.0,1.5]
result = []

for a in l1: 
    for b in l2:
        #print(a + b, end = ' ')
        result.append(a + b)
print(result)
    
datas = [ a + b for a in l1 for b in  l2] # 위의 for문을 간략하게 줄임
print(datas)
   
for d in datas:
    print(d,end= ' ')
    
print()
a = [1,2,3,4,5,6,7,8,9,10]
li = [] 
for i in a: 
    if i % 2 == 0:
        li.append(i)
print(li) # [2, 4, 6, 8, 10]

print(list(i for i in a if i % 2 ==0)) # [2, 4, 6, 8, 10]
print([i for i in a if i % 2 ==0]) # [2,4,6,8,10] 위와 동일하다.

print()
datas = [1,2,'a', True, 3]
li = [ i + i for i in datas if type(i) == int] 
# 핵심은 for 앞 여기서는  if type(i) == int에 해당되는 i+i이 진행된다.
print(li)

datas = {1,1,2,3,2}
se = {i * i for i in datas} # 핵심은 for 앞
print(se)

id_name = {1:'tom', 2:'oscar'}
name_id = { v:k for k,v in id_name.items()}
print(name_id) # {'tom': 1, 'oscar': 2} key,value 위치 변환

aa = [(1,2),(3,4),(5,6)]
for a, b in aa:
    print(a+b , end=' ')  # 3 7 11

# print(sum([20,30,40])) # 합을 구하는 내장함수이다.

print('과일 값 계산')
price = {'사과' : 2000, '오랜지':1000, '배':3000}
my = {'사과':2, '오랜지':3}
print('my ', my['사과'])
bill = sum( price[f] * my[f] for f in my ) # 여기서 f는 과일이름 값을 참조한다.
# my[key값]으로 value를 불러온다.
print('구매 총액: {}원'.format(bill) )

# 수열 생성 : range()
print(list(range(1,11,2))) # [1, 3, 5, 7, 9]
print(set(range(-10,-100,-20))) # {-30, -90, -50, -10, -70}
print(tuple(range(1,11)))  # (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

print()
for i in range(6): # 0이상 6미만 증가치는 1
    print(i, end=' ')
    
print()
for _ in range(6): # 0이상 6미만 증가치는 1
    print('Hi' ,end=' ')
print()
tot = 0
for i in range(1,11):
    tot += i
    
print('합은 ' + str(tot))
print('내장 함수로 합은 ', sum(range(1,11)))

print('문제 1 2~9단까지 구구단 출력')
for n in range(2,10): # 2 ~ 9
    print('--{}단--'.format(n))
    for i in range(1,10): # 1 ~ 9
        print('{}*{} = {}'.format(n,i,n*i)) # {}에 순서대로 값이 들어간다.

print('문제 2 1~100 사이의 정수중 3의 배수이면서 5의 배수의 합 구하기')
hap = 0
for n in range(1,101):
    if n % 3 == 0 and n % 5 == 0:
        hap += n
print("합은 %d 이다 " %hap)

print('문제 3 주사위를 두번 던져서 나온 숫자들의 합이 4의 배수가 되는 경우의 주사위 눈의 값을 출력')   
for n in range(1,7):
    for n2 in range(1,7):
        su = n + n2 
        if su % 4 == 0:
            print(n,' ' ,n2)
            
            
li = [ str(n) +' '+ str(n2) for n in range(1,7) for n2 in range(1,7) if (n + n2) % 4 == 0 ]
print(li)

# N-gram : 문자열에서 N개의 연속된 문자를 추출
text = 'hello'
aa = range(len(text)- 1)
print(aa)
for i in range(len(text)-1): # 0 1 2 3 4 에서 2개씩 문자열을 추출하면 마지막 4번째에서는 공백이 생기기에 이를 방지하기 위함.
    print(text[i:i+2])










