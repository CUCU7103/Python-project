# 클래스의 상속
class Person: 
    say = '난 사람이야 ~' # 공유자원
    nai = '20'  # 공유자원
    __kor = 'good' # private 멤버이다.
    
    
    def __init__(self,nai):
        print('Person 생성자')
        self.nai = nai
        
    def printInfo(self):
        print("나이 :{}, 이야기:{},".format(self.nai, self.say))
        
    def hello(self):
        print('안녕')
        print("hello : ", self.say, self.__kor)
        
    @staticmethod  # 스테틱 메소드로 설정함. 모듈 내의 클래스에서 전부 사용이 가능하다.
    def sbs(tel): 
        print('sbs static memthdo의 tel :', tel)  
        
person = Person('22')
person.printInfo() #  나이 :22, 이야기:난 사람이야 ~,
person.hello() # 안녕

print('Employe--------------')

class Employee(Person): # 상속 받음
    say = '일하는 동물' #  맴버가 존재함 같은이름의 부모의 변수는 은닉화 된다.
    subject ='근로자'

    def __init__(self):
        print('Employee 생성자') # 자식의 생성자가 있으면 부모의 생성자를 호출하지 않음
                                 # 호출을 하려면 명시적으로 호출을 진행해야 한다.
         
    def printInfo(self): 
        print('Employee의 printinfo')
    
    def empPrintInfo(self):
        self.printInfo()
        super().printInfo() # 바로 부모 클래스의 값을 찾아간다 명시했기 때문,
                            # 자식클래스가 부모클래스의 멤버를 반드시 사용하고자 할 super사용.
        self.say
        print(self.say," ", super().say, " ",self.subject) 
                    # 먼저 값을 해당 클래스에서 찾고 없으면 부모클래스로 이동함.
                    # subject만 먼저 해당 클래스의 멤버변수에서 찾고 사용시 모듈에서 값을 찾는다.
emp = Employee() # 객체 생성함.
# emp.printInfo() 
                # 부모의 멤버를 전부 사용이 가능하다.
                # self는 주소를 달고 다닌다.
                # 해당 멤버가 없으면  혹은 값이 없다면 부모 클래스에서 값을 찾는다. 있으면 해당 값 사용함. 
  
emp.empPrintInfo() #     def empPrintInfo(self): 실행함.  
                
print('Worker--------------')               
class Worker(Person):
    def __init__(self,nai):
        print('Worker 생성자')
        
        super().__init__(nai)  # 부모클래스의 생성자를 명시적으로 호출 - Bound Method call
        
        
    def worPrintInfo(self):
        self.printInfo()
      #  print(super().__kor)  private 멤버를 다른 클래스에서 호출하여 에러가 발생.
                
wor = Worker('33') # 33을 가지고 부모 클래스로 올라간다. wor의 주소를 가지고 올라가기 때문이다.
print(wor.say," ", wor.nai)
wor.worPrintInfo()   

print('Programmer--------------')
class Programmer(Worker):
    def __init__(self, nai):
        print('Programmer 생성자')
        # super().__init__(nai) 아래와 동일한 의미
        Worker.__init__(self,nai) #  UnBound Method call
    
    def worPrintInfo(self):
        print('Programmer에서 worPrintInfo를 오버라이드')
        self.printInfo()
        
        
pr = Programmer(28) 
print(pr.say, ' ', pr.nai) # say는 person , nai는 pr의 나이이다.
pr.worPrintInfo() # 나이 :28, 이야기:난 사람이야 ~,
                
print('클래스 타입')
print(type(pr))
print(Programmer.__bases__) # __bases__ 현재 클래스의 부모클래스를 확인함.      
                            #   (<class '__main__.Worker'>,) 다중상속, (부모가 여러개 존재할 수 있어서 tuple 형식)
print(Worker.__bases__) # (<class '__main__.Person'>,)
print(Person.__bases__) # (<class 'object'>,)         
 
                
print('--' * 30)
pr.sbs('111-1111') # 비권장한다. 클래스 이름으로 부르는 것을 권장한다.
Person.sbs('111-1111111')           
Worker.sbs('1222-222222')
                
                
                
                
                
                
                
                
                
                
                
                