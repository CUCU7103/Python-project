'''
여러 줄 주석 : 쌍, 홑 따옴표 구분을 하지 않는다.
'''

# 한 줄 주석입니다.
from jedi.api import keywords

# 변수 : 기본형 x, 모든 것이 참조변수(객체)이다. 들어오는 값에 따라서 type이 정해지는 것

a = '안녕'
print(a)

# 한줄에다가 2개의 statement줄때는 ; 사용 자바스크립트와 동일한 방식이다.
a = 5;  a = '변수 선언 시 type은 참조 되는 변수의 의해 결정되어진다.';
print(a)  
# a = 5와  a = '변수 선언 시 type은 참조 되는 변수의 의해 결정되어진다.' 는 주소가 다르다.
# 즉 a에 인스턴스의 값을 담는 것이 아니라  주소를 담는 것이다.

a = 10 # 객체 변수의 주소를 기억한다. 즉 10을 직접 담는 것이 아닌 10의 주소를 가르키는 것
b = 20
c = b # 주소를 치환한다.

print(a,b,c)
print(id(a),id(b),id(c)) # 2184586723856 2184586724176 2184586724176 id를 통해서 주소를 확인 할 수 있다.
print(a is b, a==b) # is는 주소 비교 연산자,  == 는 값 비교 연산자 이다.
print(b is c, b==c) 

aa = [10] # 집합형 자료 list
bb = [10]
print(aa is bb, aa == bb) # False / True  주소는 다르고 값은 같다.
print(id(aa), id(bb)) # 1453765687360 1453768575808 (주소 값)

A = 1; a = 2;
print(A ,id(A),'',a, id(a)) # 변수명은 대소문자를 구분한다.
    # 1 2752688554224  /  2 2752688554256

# 1 = 4  변수명으로 숫자는 사용이 불가능하다.
_1 = 4 # _숫자로 변수명으로 사용 가능하다. 특수문자중에 _ 만 허용됨.
# for = 5 # 예약어는 변수명으로 자격이 없다
import keyword # 파이썬에 설치는 되어있으나 로딩이 되어있지 않는 것을 import 함
print('키워드 목록: '  , keyword.kwlist) #  ['False', 'None', 'True', 'and', 'as', 'assert', 'async', ... 이러한 예약어는 변수명으로 사용 x

print('\n 숫자 진법-- ')
print(10, oct(10),hex(10),bin(10)) # 10 0o12 0xa 0b1010 
    # 10진수 8진수 16진수 2진수
print(10, 0o12, 0xa, 0b1010 ) # 10 10 10 10
 
print('type(자료형) 확인--------------')
print(3, type(3))  # 3 <class 'int'>
print(3.4, type(3.4))  # 3.4 <class 'float'>
print(3+4j, type(3+4j)) # (3+4j) <class 'complex'> 복소수를 나타내는 타입이다.
print(True, type(True)) # True <class 'bool'>
print('a', type('a'))  # a <class 'str'>
#====================================================================
print((1,), type((1,))) # (1,) <class 'tuple'>
# 리스트는 [ ]으로 둘러싸지만 튜플은 ( )으로 둘러싼다.
# 리스트는 요소 값의 생성, 삭제, 수정이 가능하지만 튜플은 요소 값을 바꿀 수 없다.

print([1], type([1])) # [1] <class 'list'>

print({1},type(({1}))) # {1} <class 'set'>
# set()은 중복을 허용하지 않고, 순서가 없다(Unordered).
# set()의 괄호 안에 리스트를 입력하여 만들거나 다음과 같이 문자열을 입력

print({'k':1}, type({'k':1})) # {'k': 1} <class 'dict'>
# 딕셔너리는 Key와 Value를 한 쌍으로 갖는 자료형













