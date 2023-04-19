
from cryptography.x509 import name


# 묶음 자료형 : list - 순서가 o , 변경이 가능하다, 요소값의 종류는 다양하다.
# 속도가 느리다 - 데이터 분석의 경우 numpy의 ndarray를 사용해야 함.

a = [1,2,3] # list 형식이다.
b = [10, a, 20.1,True, 'kbs'] # list 안에는 다양한 type이 들어올 수 있다.

print(a, type(a), id(a)) #  [1, 2, 3] <class 'list'> 2173060151616
print(b, type(b), id(b)) # [10, [1, 2, 3], 20.1, True, 'kbs'] <class 'list'> 2173060173952
print(b[0]) # scalar
# Python은 4가지의 Scalar 타입이 있습니다.
# int(정수), float(실수), None(값없음), bool(True, False) 4가지
print(b[1]) # [1, 2, 3]


print()
family = ['엄마', '아빠', '나'] # 
family.append('남동생') # list에 추가 ['엄마', '아빠', '나' , '남동생'] 뒤에 추가된다.
family.insert(0, '할아버지' ) # insert는 삽입 지정된 인덱스에 삽입되어진다.
family.extend(['여동생', '삼촌']) # 여러개 추가 한 번에 여러 개를 추가할 수 있다.
family += ['고모','이모'] # 위와 동일함.
family.remove('남동생') # 제거함.
print(len(family), family)
print(family.index('엄마')) # 해당 값의 인덱스를 확인한다.
print('엄마' in family) # 존재여부 확인 boolean

print()
aa = [1,2,3,['a','b','c'],4,5]
print(aa[0]) # 인덱싱 list에서 해당 값을 하나 출력한다고 생각하면 된다.
print(aa[0:3]) # 슬라이싱 (0 이상 3미만)  [1, 2, 3]
print(aa[3]) # ['a', 'b', 'c']
print(aa[3][:2])  
# ['a', 'b'] aa[3]을 통해서 해당 인덱스의 값을 불러오고 
# [:2]를 통해서 불러온 인덱스의 전체 값 중에서 첫번째 요소부터 두번째 요소까지를 반환하여 새로운 리스트를 만든다.
print(aa[::2]) # 증가치 첫 번째 요소 부터 시작해서 두 칸씩 건너뛰면서 리스트의 모든 요소를 포함하는 부분 리스트를 반환한다.


print()
print(aa, id(aa)) # [1, 2, 3, ['a', 'b', 'c'], 4, 5] 2173060174848
aa[0] =7 # 요소값 변경이 가능하다.
print(aa,id(aa)) # [7, 2, 3, ['a', 'b', 'c'], 4, 5] 2173060174848
aa.remove(4) # 값에 의한 삭제 list 내에 해당 값이 있으면 삭제한다. 단 삭제하려는 값이 리스트 내 2개 이상 존재한다면 앞에 있는 값을 삭제함.
print(aa) # [7, 2, 3, ['a', 'b', 'c'], 5]
del aa[4] # 순서에 의한 삭제 
print(aa) # [7, 2, 3, ['a', 'b', 'c']]

aa[3].remove('c') # [7, 2, 3, ['a','b']]
del aa[3][0] # [7, 2, 3, ['b']]
print(aa)

del aa # 전체 삭제
 # print(aa)

# sort (정렬)
aa = [3,1,5,2,4]
aa.sort() # [1,2,3,4,5]
print(aa)
aa.sort(reverse=True) # [5, 4, 3, 2, 1]
print(aa)

aa2 = [3,1,5,2,4]
aa3 = sorted(aa2) # 원본이 정렬되지 않는다.
print(aa2) # [3, 1, 5, 2, 4]
print(aa3) # [1, 2, 3, 4, 5]

print('복사')
names = ['톰','제임스','오스카']
names2 = names # 주소치환 - 얕은 복사
print(names, id(names)) # ['톰', '제임스', '오스카'] 2132646860672
print(names2, id(names2)) # ['톰', '제임스', '오스카'] 2132646860672
names[0] = '길동'
print(names) # ['길동', '제임스', '오스카']
print(names2) # ['길동', '제임스', '오스카']

print('깊은 복사')
import copy
names3 = copy.deepcopy(names) # 새로운 객체를 생성함.
print(names, id(names)) # ['길동', '제임스', '오스카'] 2132646860672
print(names3, id(names3)) #  ['길동', '제임스', '오스카'] 2828391979520 주소가 다름.
names3[0] = '순신'
print(names) # ['길동', '제임스', '오스카'] 서로 다른 객체이기에 변하지 않는다.
print(names3) #  ['순신', '제임스', '오스카'] 

# 자료구조 : stack(LiFO), queue(Fifo)
sbs = [1,2,3]
sbs.append(4) # [1,2,3,4]
print(sbs)
print(sbs.pop()) # 4 빠져나감
print(sbs.pop()) # 3 빠져나감
print(sbs) # [1, 2]

print()
sbs2 = [1,2,3]
sbs2.append(4)
print(sbs2.pop())
print(sbs2.pop())
print(sbs2)













