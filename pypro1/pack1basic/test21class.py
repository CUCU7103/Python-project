# class : 객체지향적(중심적인)인 프로그래밍 구사
# 클래스는 새로운 이름공간을 지원하는 단위이다. 멤버변수와 메소드를 갖는다.
# 접근지정자 X , 메소드 오버로딩 X 
from hamcrest.core.core import isinstanceof

print('뭔가를 하다가....')

class TestClass: # class header 
    # 이하는 class body가 된다.
    aa = 1 # 멤버변수는 클래스 내에서 전역이다. 
    
    def __init__(self): # 생성자이다. 내용이 없다면 생략이 가능하다.
        print('생성자')
        # 생성자 --> 작업수행 -->소멸자 
    def  __del__(self): # 생략이 가능하다.
        print('소멸자')
        
    def printMsg(self): # 멤버 메소드이다. ㄴ>self의 유무에 따라 메소드와 함수로 나뉜다. 
                        # self 가 들어있으면 메소드 아니면 함수로 구분한다.
        name = '한국인'
        print(name) # 지역변수를 출력한다.
        print(self.aa) # 멤버변수(전역)를 출력한다.

print(TestClass.aa) # 클래스도 객체로 생성되어진다. 메모리를 확보한다 , 단 자주 쓰이는 방법은 아니다.
print("----------------------------")
test = TestClass() # 생성자 호출. 인스턴스가 만들어진다. 인스턴스명 = 클래스() 형식으로 생성한다.
print(test.aa) # 생성자, 1
print(id(TestClass),' ',id(test))

print("--------------------------------")
# TestClass.printMsg() # err 인수와 매개변수를 맞추지 않음
test.printMsg()  # 메소드 호출 방법 : Bound method call 
TestClass.printMsg(test) # 메소드 호출 방법 2: UnBound Method call
print()
print('클래스 타입 확인 ', isinstance(test,TestClass)) # 이 타입이 니 타입이냐~" 하는 타입, 클래스, 객체 비교 확인 함수인 isinstance 함수
print(type(test))
print(type(TestClass))





