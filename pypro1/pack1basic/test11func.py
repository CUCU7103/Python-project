# 사용자 정의 함수
 
def DoFunc1():
    print('DoFunc1 수행')

DoFunc1() # 함수를 실행하라
DoFunc1
print(type(DoFunc1)) # <class 'function'> 모든 것이 전부 클래스이다.
print(DoFunc1, id(DoFunc1))  # <function DoFunc1 at 0x0000021ED8453E20> 2331500690976

print("==" * 20)
#==============================
def DoFunc2(para1, para2): # 함수명(매개변수,,) parameter
    su1 = para1 # 5
    imsi = su1 + para2 # 12
    result = DoFunc3(imsi) # DoFunc3 호출함.  / 함수를 호출한다.
    print(result + ' DoFunc2 수행')

def DoFunc3(imsi):
    print(imsi)
    return "성공"

DoFunc2(5,7) # 함수명(인수) argument 
# 5,7은 각각 para1, para2로 넘어간다.

# =================================================
print()
def SwapFunc(a,b):
    return b,a # 묶음형 자료 tuple로 넘기고 있다. 즉 하나의 객체를 반환한다, return 값이 하나이다.

a = 10 ; b = 20
a,b = SwapFunc(a,b)
print(a,' ',b)

print(SwapFunc(a,b)) # tuple 형식으로 값이 출력되어진다. (10, 20)

#==================================================

print()
def AbcFunc():
    print('good')

print(AbcFunc()) # None, 함수는 반환값이 반드시 존재한다. 
                 # 즉 return 값을 설정하지 않으면 None 표시됨 

print()
def func1():
    print('func1 process')
    def func2(): # 내부함수
        print('func2 process')
    func2() # func1에 의존하고 있다. 즉 func1을 통해서 실행되어져야함.
            # 함수 내에서 return을 만나면 함수 밖으로 빠져나온다.
func1() 

# if 조건식에 함수를 사용한다.
def isOdd(para):
    return para % 2 == 1 # para % 2 == 1 홀수를 구하는 식, 홀수면 true (1) 짝수면 false(0)가 나온다.

print(isOdd(5)) # True
print(isOdd(6)) # False
# 함수의 반환값이 True / false이기에 조건문에 적용이 가능하다.

mydict = { x : x*x for x in range(11) if isOdd(x)}  # dict 형식이다.

print(mydict) # {1:1, 3:9, 5:25, 7:49, 9:81}








