# 함수
# 여러개의 수행문을 묶은 실행단위이다.
# 반복 소스의 단순화. (재활용이 가능)
# 독립적으로 구성된 프로그램 코드의 집합
# python은 멀티 패러다임이 가능한 언어이다. : 객체지향, 절차지향, 함수지향 모두 지원한다.
# def 함수명([매개변수 , ....]):
# 수행문.....

# 내장함수,외장함수,사용자 정의함수
# 내장함수 일부 경험하기 
print(sum([3,5,7])) # 15
print(int('5'),float('5.5'),str(5) + '오') # 5 5.5 5오

a = 10 
b = eval('a + 5') # 수식의 모양을 하고 있는 문자열을 수식처럼 사용하려면 eval 사용한다.
print(b)

print(round(1.2), round(1.5)) # 반올림
import math
print(math.ceil(1.2), math.ceil(1.5)) # 올림
print(math.floor(1.2), math.floor(1.5)) # 내림

bb = [1,3,2,5,7,6]
res = all(a < 5 for a in bb) 
print('모든 숫자가 5미만인가?', res) # False

res = any(a < 5 for a in bb)
print('숫자 중 5미만이 있나?', res) # True

print()
x = [1,2,3]
y = ['a','b']
for i in zip(x,y):  # 복수 개의 자료를 쌍을 이뤄 tuple 형으로 만들어준다.
    print(i)







