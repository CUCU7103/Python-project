# 일급 함수의 자격요건
# 함수 안에 함수 선언, 인자로 함수선언, 반환값이 함수이다.

def func1(a,b):
    return a + b

def func2(f): # 인자로 함수 사용
    def func3(): # 함수안에 함수 선언
        print('나는 내부함수야~~')
    # func3() 
    func3() # 함수를 실행시킨다.
    return f # 반환값이 함수이다.

mbc = func2(func1) # func1()은 실행결과를 넘기는것  인자로 함수 사용
print(mbc(3,4))

print('\n람다함수(lambda funcition) : 이름이 없는 한 줄 짜리 함수')
# def를 쓸 정도로 복잡하지 않거나, def를 쓸 수 없는 곳에서 사용할 수 있다.
def hap(x,y): 
    return x + y 

print(hap(1,2)) # 3

print((lambda x,y: x + y)(1,2)) # 3 위의 함수와 같은 결과를 보인다.
        # 인수 x,y 에 return형식 파라미터 값
aa =  lambda x,y: x + y  # 이름을 부여하지 않았다.
print(aa(1,2)) # 3

print()
bb = lambda: 5 + 10 # 인수가 없으면 생략가능함.
print(bb()) 

print()
kbs = lambda a , su = 10: a+su
print((kbs(3)))  # 13
print((kbs(3, 6))) # 6

sbs = lambda a, *tu, **di:print(a,tu,di)
sbs(1,2,3,m=4, n=5)

li  = [lambda a, b : a+b, lambda a , b : a*b] # list 안에서의 람다사용
print(li[0](3,4)) 
print(li[1](3,4)) 

# 임의의 함수 안에서 람다 사용
# filter(조건함수, 순회 가능한 데이터 ) 여러개의 데이터로부터 일부의 데이터만 추려낼때 사용하는 내장함수이다.

print(list(filter(lambda a:a < 5, range(10)))) 
# [0, 1, 2, 3, 4]
print(list(filter(lambda a:a % 2, range(10)))) # 조건이 참인 것들만 필터링한다. 1,0은 True / false
# [1, 3, 5, 7, 9]

# 1~ 100 사이의 정수중 5의 배수이거나 7의 배수만 걸러서 출력
print(list(filter(lambda a:a % 5 == 0 or a % 7 == 0, range(1,101))))


