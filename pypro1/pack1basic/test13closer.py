# Closure : Scope의 제약을 받지 않는 변수들을 포함하고 있는 코드블럭이다.
# 내부 함수의 주소를 반환함으로 해서 함수 내의 맴버를 함수 밖에서 참조 가능..

def funcTimes(a,b):
    c = a + b 
    # print(c)
    return c

print(funcTimes(2,3))  # 5
# print(c)  함수 내에서 선언한 변수이므로 사용이 불가하다

kbs = funcTimes(2,3) # 함수의 값을 담는다.
print(kbs) # 5

kbs = funcTimes # 주소를 치환함. 함수의 이름 ()제외 는 주소를 가진다.
print(kbs) # funcTimes와 같은 주소를 가진다. function funcTimes at 0x000001E4E94B3EB0
print(kbs(2,3)) # 5
print(id(kbs), id(funcTimes)) # 2376846163488 2376846163488 동일한 주소

# del kbs
del funcTimes 
# 함수의 주소를 가지고 있는 funcTimes가 제거된 것이다. 함수의 내용은 살아있다. 차후에 gc가 제거한다. 
# 즉 함수와의 연결을 끊어버리는 것이다.
# print(funcTimes(2,3))

mbc = sbs = kbs 
print(mbc(3,4)) # 7

print('클로저로 출발')
def outer():
    count = 0
    def inner():
        nonlocal count # count는 inner의 멤버가 아닌 outer의 멤버이다.
        count += 1
        return count # outer의 count 값이 변경되어진다.
    #inner()
    return inner # 함수의 주소를 return, 이것이 closer이다.

var1 = outer() # outer 함수의 return 값은 inner이다. 즉 inner의 주소를 가짐 
print(var1) # <function outer.<locals>.inner at 0x000001E4E985D480>
print('count:' ,var1()) # 1, inner가 실행되어진 결과값을 받는다,
                        # why? 위에서 설명하였듯 var1는 inner의 주소를 갖기 때문
aa = var1() 
print('count:',aa) # 2
print('count:' ,var1()) # 3

print("===========" * 20)

var2 = outer() # 새로운 객체가 생성되어진다. 앞에 new붙는다고 생각하자
print('count: ', var2())
print('count: ', var1()) # var 2와는 다른 객체이다.
print('count: ', var2())
print(id(var1), id(var2))

print('\n수량 * 단가 * 세금(분기마다 다름)을 출력하는 함수 작성')

def outer2(tax): # tax는 지역변수이다.
    def inner2(su,dan):
        amount = su * dan * tax
        return amount
    return inner2 # closer 사용함.

# 1분기 n tax:0.1
q1 = outer2(0.1)
result1 = q1(5,50000)
print('result1 : ', result1)

result2 = q1(2,10000)
print('result2 : ', result2)

# 2분기 n tax:0.05
q2 = outer2(0.05)
result3 = q2(5,50000)
print('result3 : ', result3)

result4 = q2(2,10000)
print('result4 : ', result4)







