# 묶음 자료형 : tuple - list와 유사하다. 단 readonly이다. 변경이 불가함. 검색속도가 빠르다. 순서는 있다.
# t = ('a', 'b','c')
t = 'a','b','c'  # 위와 동일한 의미이다.
print(t, type(t), len(t), t.count('a')) # <class 'tuple'>
 # t[1]  = 'k' 수정이 불가하다 - error 발생함 'tuple' object does not support item assignment.
print(t[0:3])

q = list(t) # list로 형변환
q[1] = 'k'
t = tuple(q)  # 형 변환해서 값을 변경시키고 다시 튜플로 되돌려놓는다.
print(t)
print()

tt =(1,2)
a,b = tt  # 값을 지정함. a = 1 b = 2 인 상태이다.
b,a = a,b # 지정된 서로의 값을 바꾼다. 
tt = a,b 
print(tt)

ttt = (3,) # 튜플에 요소가 하나면 ,를 붙여야 튜플이 적용되어진다. 
print(type(ttt))  # <class 'tuple'>

print("---" *20)
# 묶음 자료형 : set - 순서x, 변경x, 중복이 불가하다.
a = {1,2,3,1} # 중괄호를 사용한다.
print(a, type(a),len(a))  # {1, 2, 3} <class 'set'> 3
# print(a[0])  순서가 없다. 'set' object is not subscriptable
# 순서가 없다는 것은 인덱스를 적용시킬 수없다는 것과 마찬가지

b = {3,4}

print(a.union(b)) # 합집합 {1, 2, 3, 4}
print(a.intersection(b)) # 교집합 {3}
print(a - b ,a | b, a & b) # 차, 합, 교집합 {1, 2} {1, 2, 3, 4} {3}

b.add(5)
print(b)
b.update({6,7}) # 추가할때는 tuple, list 등 타입을 신경쓰지 않는다.
b.update([8,9])
b.update((10,))
print(b)

b.discard(3) # 값 삭제 : 해당 값 없으면 통과함
b.remove(10)  
b.discard(3) 
# b.remove(10) # 값 삭제 : 해당 값 없으면 에러발생
print(b)

b.clear() # 안에 있는 요소들을 전부삭제 , set()
print(b)
del b # 변수삭제
# print(b) # name 'b' is not defined

li = [1,2,3,4,2,1]
print(li)
s = set(li) # 변수에 set 담고
li = list(s) # list로 변경함
print(li) 

# 묶음 자료형 : dict(사전형) -{key:value}로 구성되어져 있다. 
# key는 중복이 불가하다 value는 중복이 가능하다. key를 이용해 value를 찾는다. 순서가 없다.
mydic = dict(k1 =1, k2 ='kbs', k3 = [1.2, 2.3]) # value는 list가 와도 가능
print(mydic, type(mydic), len(mydic)) # {'k1': 1, 'k2': 'kbs', 'k3': 1.2} <class 'dict'> 3
print()

dic = {'아나콘다' : '뱀', '자바':'커피' , '스프링' : '용수철'}
print(dic)
print(dic['자바']) # key로 value를 찾는다.
# print(dic[0]) # 순서가 없다.
dic['오라클'] = '예언자' # 추가함. 
# dict에서는 append를 사용 x
print(dic)

del dic['오라클'] # 제거
dic.pop('자바') #  추출함.
dic['스프링'] ='웹프레임웍' # value 값을 수정함.
print(dic)

print(dic.keys()) # 키 값만 출력함
print(dic.values()) # value값만 출력한다.
print(dic.get('스프링')) # 웹프레임웍 key를 통한 값의 출력이다.
print('스프링' in dic) # True












