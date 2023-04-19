# int, float, bool, complex 타입은 변수가 객체 값 하나를 참조함.

# 집합형 자료형 : 여러개의 값들을 묶은 집합
# str, list, tuple, set, dict, type 이 여기에 해당합니다.

# str : 문자열 묶음 자료형, 순서 O, 수정이 불가하다. 
# (인덱싱 (1개참조)과 슬라이싱(여러개 참조)이 가능하다.)
s = 'sequence' 
print(len(s)) # 문자열의 길이를 확인함
print(s.count('e')) # 문자열 관련 함수들
print(s.find('e'),s.find('e',3),s.rfind('e')) # 1 4 7
# s.find('e') 문자열 e가 처음나오는 인덱스 반환 
# s.find('e', 3) 3번째 인덱스 부터 검색하여 e가 있는 인덱스를 반환함.
# s.rfind('e') 뒤에서 부터 찾는다.
#....

# 문자열 묶음 자료형 요소값은 수정이 불가하다.
ss = 'mbc'
print(ss, id(ss)) # mbc 1785297624112 mbc 객체의 주소를 참조함
ss = 'abc'
print(ss, id(ss)) # abc 1785297543024 mbc 연결을 끊고 abc 객체의 주소를 참조함.

print('인덱싱/슬라이싱')  # 문자열에서 값을 가져올때...
print(s[0],s[3],s[-1])  # s u e  인덱싱
# -1은 오른쪽에서부터 읽는 것 
# ss[0]  = 'k'   수정이 불가하다.
print(s[0:3],'' ,s[-5:-1]) #  seq  uenc
print(s[0:6:1],'', s[0:6:2], ' ' ,s[::2])  # 슬라이싱 sequen  sqe   sqec 즉 증가치를 부여할 수 있다.
print(s[0:5] + 'good')

imsi = 'kbs mbc sbs'
nice = imsi.split(sep=' ') # 문자열 자르기 (분리)  ['kbs', 'mbc', 'sbs']
print(nice)
good = ':' .join(nice) # 문자열 합치기 (결합) kbs:mbc:sbs
print(good)

a = 'Life is too long' 
b = a.replace("Life","My leg") # replace() 문자열 바꾸기 
print(a) # Life is too long
print(b) # My leg is too long

