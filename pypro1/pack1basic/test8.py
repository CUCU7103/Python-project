# 반복문 while 
from astropy.units import count
a = 1
while a <= 5:
    print(a, end= ' ') # end는 line skip을 생략한다.
    a +=1
print()

i = 1
while i <= 3:
    j = 1
    while j <= 4:
        # print('i :' + str(i) + ', j: ' + str(j))
        j = j + 1
    i += 1

print('1 ~ 100 사이의 정수 중 3의 배수의 합은?')

i = 1; hap = 0
while i <= 100:
    if i % 3 == 0:
        hap += i
    i += 1
    
print('합계 :'  + str(hap))

print('1 ~ 100 사이의 정수 중 3의 배수이나 2의 배수가 아닌 수를 출력하고 합은?')

# i2 =1; hap2 =0
# while  i2 <= 100:
#     if i2 % 3 == 0 and i2 % 2 != 0:
#         print(i2, end=' ')
#         hap2 += i2 
#     i2 +=1 
# print()   
# print(hap2)

i = hap = 0
while i <= 100:
    i += 1
    if i % 3 == 0 and i % 2 != 0: # 3의 배수이고 2의 배수는 아니다.
        print(i, end = ' ,')
        hap += i
    i += 1
    
print('\n합계 :'  + str(hap))

print()
colors = ['red','green','blue']
a = 0
print('횟수 확인 : ' + str(len(colors)))
while a < len(colors): 
    print(colors[a], end = ' ') # red green blue 
    a += 1 
    
print()

while colors: 
    print(colors.pop(), end = ' ') # blue green red 
    
print()
i = 1 
while i <= 10:
    j = 1
    res = ''
    while j <= i:
        res = res + "*"
        j += 1 
    print(res)
    i += 1

print("\n -1,3,-5,7,-9,11~99까지의 합은?")

i = 1; cnt =1; tot=0
while i < 100: 
  # print(i, end = ' '  )
        # 짝수 지역 숫자 처리
    if cnt % 2 == 0: 
        tot += i
        # 
        print(i, end= ' ')
        
        # 홀수 지역 숫자 처리
    else: 
        k = -1 * i 
        tot += k
        # 홀수자리의 음수의 합을 구한다.
        # -1
        print(k, end=" ")
    
    cnt += 1 #  반복하도록 함.
    i += 2  # 
print('\ntot :', tot)

# if 블럭이 while 블럭을 포함
import time
# time.sleep(3)
# print('good')

# sw = input('폭탄 스위치를 누를까요 [y/n]')
sw = 'n'
if sw == 'y' or sw == 'Y':
    count = 5
    while  1 <= count:
        print('%d초 남았습니다' %count)
        time.sleep(1) # 응답지연시간을 부여한다.
        count -= 1
    print("해체실패")
elif sw =='n' or sw == 'N':
    print('작업취소')
    pass
else:
    print('y 또는 n을 누르시오')   
    
# continue , break
a = 0
while a < 5: 
    a += 1
    if a == 3:continue
    # if a == 4:break # 강제종료
    print(a)
else:
    print('while 정상 종료') # break 없을 시 만나게된다.
print('while 수행 후 %d' %a)

print('난수관련')
import random
# random.seed(1) # 일정한 난수를 출력하도록 함.
print(random.random()) # 0 ~ 1 사이의 난수가 발생함./
print(random.randint(1,5)) # 1 ~ 5 사이의 숫자 출력
print(random.randint(2,10))  # 2 ~ 10 사이의 숫자를 출력한다.

friend = ['재섭','준규','영진','유진']
print(random.choice(friend)) # 랜덤으로 하나를 찍음
print(random.sample(friend, 1)) # 랜덤으로 하나를 찍음
random.shuffle(friend) # 랜덤으로 섞는다.
print(friend)

# 컴퓨터가 가진 임의의 숫자 맞추기

num =random.randint(1,10) # 1~10 사이 숫자를 담는다. 
while True:  # 항상 (참) 무한루프
    print('1 ~ 10 사이의 컴이 지닌 예상 숫자 입력하기')
    su = int(input())
    if su == num: # 입력한 값과 num이 같다고 한다면
        print(' 성공 ' * 10 )
        break
    elif su < num: # 숫자의 범위를 추측하게 해줌
        print('더 큰 수를 입력하세요')
    elif su > num:
        print(' 더 작은 수를 입력하세요')




   
   
        




