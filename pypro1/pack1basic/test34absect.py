# Abstract class
from abc import abstractmethod, ABCMeta

class AbstractClass(metaclass=ABCMeta): # 추상클래스로 설정함.  metaclass=ABCMeta
    @abstractmethod # 데코레이터(decorator)라고 부른다.
    def absMethod(self): # @abstractmethod로 장식된 추상메소드 
        pass # 추상메소드에는 내용이 없어야 함.

    def normalMethod(self):
        print("추상클래스 내의 일반메소드") # 자식이 부를 예정이다.
    
# kbs = AbstractClass() # 추상 클래스는 인스턴스 할 수 없다. 즉 추상 클래스는 스스로 인스턴스 할 수없다.
# TypeError: Can't instantiate abstract class AbstractClass with abstract method abcMethod

class Child1(AbstractClass): # 추상 클래스를 상속받은 클래스이다. 즉 추상메소드를 반드시 오버라이딩 해야한다. 
                             # 그렇지 않으면 오류가 발생한다. 
    name = '난 Child1'
        
    def absMethod(self):
        print('추상메서드를  Override 해서 일반 메소드화 시켜준다.')    # 추상클래스는 스스
    

c1 = Child1()
print(c1.name)
c1.absMethod()
c1.normalMethod()

print()
class Child2(AbstractClass):
    
    def absMethod(self):
        print('추상메소드를 Child2에서 재정의: 강요당함. 즉 필수적으로 오버라이딩이 필요함.')  
    
    def normalMethod(self):
        print('추상 클래스 내의 일반 메소드를 재정의하였다. 내 의지로 오버라이딩')

c2 = Child2()
c2.absMethod()
c2.normalMethod() 
    
print('\n다형성---')
sbs = c1
sbs.absMethod() # 동일한 statement이나 결과는 다양하게 나올 수 있다.
sbs = c2
sbs.absMethod()







