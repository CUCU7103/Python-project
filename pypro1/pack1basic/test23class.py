# 모듈의 멤버 / 클래스의 맴버 이해

kor = 100 # 전역변수
 
def abc(): 
    print('함수')
    

class MyClass:
    kor = 90 # 지역변수
    
    def abc(self):
        print(self.kor,'메소드')
        
    def showData(self):
       # kor = 80 # 메소드의 지역변수
        print(self.kor, ' ',kor) # self는 this와 비슷하다. 
                                 # kor의 유무를 먼저 메소드의 지역변수에서 확인 후 없다면 상위 객체인 모듈로 넘어가서 확인한다.
        self.abc() # 메소드 
        abc() # 클래스 내에서 외부에 있는 함수를 호출함.
        
my = MyClass() # my는 MyClass의 주소를 가진다.
my.showData() # self를 타고 my(주소)가 들어간다.
#
# kor는 메소드의 지역변수를 확인하고 없으면 모듈의 멤버변수를 찾아간다.
# class 와 함수는 동급이기에 상위객체인 모듈로 넘어간다.(메소드도 마찬가지이다.)
# self는 주소를 넣어야한다는 것, 기능은 this와 비슷
my2 = MyClass() # 새로운 객체를 생성한다.
my2.eng = 95 # 신규 멤버를 추가함.
print(my2.eng) # my2 객체변수가 참조하는 인스턴스에 eng가 만들어짐.
# print(my1.eng) my과 원형클래스에서는 존재x  


