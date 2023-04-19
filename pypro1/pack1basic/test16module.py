#  Module : 소스코드의 재사용을 가능하게 하며, 
#  코드를 하나의 이름 공간으로 구분 관리를 할 수 있다.
#  한 개의 파이썬 파일에(py) 하나의 Module로 구성된다.
#  표준모듈, 사용자 정의 모듈, 제 3자 모듈 ------> 파일하고 비슷한 느낌

print('뭔가를 하다가')
 
a = 5 
if a > 5:
    print('good')

def func(): 
    pass

print('내장된 모듈 사용')
import math
print(math.pi)
from math import pi
print(pi)

import calendar # 달력 모듈
calendar.setfirstweekday(6)
calendar.prmonth(2023, 4)
 
import random
print(random.random()) # 모듈.멤버

# from을 사용하여 import 없이 불러온다.
from random import random
print(random()) # 모듈명 생략해서 부를 수 있다.


from random import *  #  random 모듈의 멤버 전부를 로딩한다.
print(randrange(1,5))

