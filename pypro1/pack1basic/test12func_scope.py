# 변수의 생존 범위 
# 변수가 저장되는 이름공간은 변수가 어디서 선언되고, 치환되었는가에 따라 생존 범위가 결정되어진다.

# 변수 영역 및 접근 순서
# Local > Enclosing function > Global  > Built - in 

player = '전국대표' # 모듈에서 선언함, 전역변수(모듈의 어디서든 공유가 가능하다.)
player2 = '전국대표233'
c = 0

def func123(a,b,c):
    return a,b,c

print(func123(player, player2, c)) # tuple형식으로 출력됨
      
      
def FuncSoccer():
    name = '임영웅' # 지역변수
    player = '지역대표'
    print(name, player, player2) 
    
print(FuncSoccer)
FuncSoccer() # 임영웅, 지역대표 지역변수가 우선 시 된다.

print()
a = 10; b = 20; c = 30 # 위에서부터 한줄한줄 읽어 내려간다.
print('함수 수행 전 : a:{}, b:{}, c:{}'.format(a,b,c)) 
def Foo():
    print('지역변수 영역입니다 local.')
    print(' 내부함부 입장에서 nonlocal')
    a = 40 # Foo와 Bar에서만 의미가 있다.
    b = 50
    def Bar(): # Bar에 선언되지 않으면 가장 가까이 있는 곳으로 들어간다.
      # c = 60 # Bar에서만 의미가 있다.
        global c # c는 Bar의 멤버가 아니라 모듈의 멤버이다.
        nonlocal b # b는 Bar의 멤버가 아니라 foo의 멤버가 된다.
        print('내부함수 입장에서의 local')
        print('함수 수행 중1 : a:{}, b:{}, c:{}'.format(a,b,c)) 
        c = 60 # global (전역변수가 됨)  
        b = 70 # foo 지역변수가 되어진다.
      # c = 60 객체를 담기 전에 위에서 참조해서 오류가 발생한다. global 사용전
      # local variable 'c' referenced before assignment
        print('함수 수행 중2 : a:{}, b:{}, c:{}'.format(a,b,c)) 
    Bar() # Foo 함수 실행시 내부함수 Bar 실행한다.
    
Foo()
print('함수 수행 후 : a:{}, b:{}, c:{}'.format(a,b,c)) # 같은 수준(위치)에 있는 값 출력함. 

print("**" * 20)

# 인수와 매개변수 매칭 
# 매개변수 유형 : 위치, 기본값, 키워드, 가변 매개변수 존재함.

def ShowGugu(start,end=5): # 기본값 부여함.
    for dan in range(start, end + 1):
        print(str(dan) + '단 출력')

ShowGugu(2,3)
print()
ShowGugu(3)
print()
ShowGugu(3,4) # 새로운 매개변수를 입력하면 기존의 함수에서 설정한 기본값 무시됨. 즉 end = 5는 4로 변경되어진다.
print()
ShowGugu(start = 2,end = 3) # 키워드 맵핑이다. 
print()
ShowGugu(end = 3, start = 2) # 키워드로 맵핑할때는 순서가 달라도 상관없다.
print()
ShowGugu(2, end = 3) 
print()
# ShowGugu(start = 2, 3) 
# 키워드 매핑시 뒤의인자만 키워드 설정하는 것은 가능하나 그 반대의 경우는 불가능하다.
print()  
# * : packing 연산자를 사용해 가변인수를 처리할 수 있다.
def func1(*para): # 1개가 들어오면 1개를 받고 3개가 들어오면 3개를 받는다... 가변인수
    print(para) # 여러개의 값을 출력하게 되면 tuple type으로 출력되어진다.
    for i in para:
        print('음식 ' + i)
        
func1('공기밥','김밥','주먹밥')
func1('공기밥') # ('공기밥',)
print("-----------------------------------")
# def func2(a,*para): ok 
def func2(a,b,*para): # ok
    
        # def func2(*para, a) 는 되지 않는다. 즉 packing 연산자는 뒤에와야 한다.

    print(a) # 공기밥
    print(b) # 김밥
    print(para) # 값이 여러개면 tuple 형태로 반환되어진다.
    
func2('공기밥','김밥','주먹밥')

print()
def selectProcess(choice, *ar):
    if choice == 'sum': # 입력받은 값이 sum이라면 
        re = 0
        for i in ar:
            re += i # 1~5까지 합 반환함
    elif choice == 'mul': # 입력받은 값이 mul이라면
        re = 1
        for i in ar: 
            re *= i # 1~5까지 순차적으로 곱한다.
    return re

print(selectProcess('sum', 1,2,3,4,5)) # 15
print(selectProcess('mul', 1,2,3,4,5)) # 120

print() # 사전형 데이터인 경우 ** 을 사용한다.
def func3(w, h, **other):
    print('몸무게 {}, 키{}'.format(w,h))
    print(other) # dict type
    
func3(66, 177) # dict type의 인수가 없기에 비워두고 출력함.
               # 몸무게 66, 키177 {}

func3(66, 177, irum='지구인', nai=22) 
                # 몸무게 66, 키177
                # {'irum': '지구인', 'nai': 22}

print()
def func4(a,b,*c,**d): # packing과 dict 사용함.
    print(a,b)
    print(c)
    print(d)
    
func4(1,2) # tuple과 dict는 비어있음
func4(1,2,3,4,5) #tuple 사용함 dict빔
func4(1,2,3,4,5, x=6,y=7) # 다 사용함. 
          
          
          
          
          
          







