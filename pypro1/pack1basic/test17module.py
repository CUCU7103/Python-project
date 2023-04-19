'''
메인 모듈에서 작성된 사용자 정의 모듈 호출
'''

print('무언가를 하다가....')

import pack1basic.test17my_mod1     # import 전체 경로(패키지 + 파일명)  해당모듈을 참조한다.

list1=[1,2]
list2=[3,4,5]

pack1basic.test17my_mod1.Listhap(list1, list2) # 다른 모듈의 함수를 사용함.
# ([1, 2], [3, 4, 5]) 

# from pack1basic import test17my_mod1
# test17my_mod1.Listhap(list1, list2)
# ([1, 2], [3, 4, 5]) 

def ThisListhap(*ar): # packing 
    print(ar)
    if __name__ == '__main__': 
        # __name__ 모듈의 이름 값 가짐 즉 이 모듈이 main 이면 실행한다. 즉 main 모듈인지 확인하는 작업이다.
        print('최상위 메인 모듈임을 선언')
 
ThisListhap(list1, list2)  #  ([1, 2], [3, 4, 5])

from pack1basic import test17my_mod1 # 해당 모듈을 사용가능함.
test17my_mod1.Kbs()
print('tot : ', test17my_mod1.tot)

# test17my_mod1 의 함수나 멤버변수들을 가져와 사용가능해진다. 좀 더 세부적으로 설정함.
from pack1basic.test17my_mod1 import Mbc, tot
print("tot : ", tot)
Mbc(11)

print('패키지가 다른 영역의 모듈 읽기')
import pack1other.test17my_mod2
print(pack1other.test17my_mod2.Hap(3, 2))

from pack1other.test17my_mod2 import Cha
print(Cha(3, 2))

print('classpath가 설정된 패키지의 모듈읽기') # 패키지명을 생략가능하게 한다. 아나콘다에 lib에 해당 패키지를 넣으면 된다.
import test17my_mod3
print(test17my_mod3.Gop(3,2))
from test17my_mod3 import Nanugi
print(Nanugi(3, 2))
















