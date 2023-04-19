# 클래스의 상속: 각 클래스는 별도의 모듈로 작성한 후 main 모듈에서 호출해야 한다.
# 다중 상속이 가능하다.
print('뭔가를 하다가....')

# 모든 동물들이 기본적으로 갖춰야 할 행위와 속성을 Animal 클래스에 적은 후 상속하는 것

class Animal:
    def __init__(self):
        print('Animal 생성자')

    def move(self):
        print('움직이는 생물')
        
        
    
class Dog(Animal): # 상속 :
    
    # 생성자가 없으면 부모의 생성자가 수행되어진다.
    # 자식의 생성자가 있으면 부모의 생성자를 수행하지 않는다. "은닉화"
    # 명시적으로 호출하지 않는 이상 자바와의 다른점이다.
     
    def __init__(self):
        print('Dog 생성자')
        
    def my(self):
        print('댕댕이라 불러주세요')

dog1 = Dog()
dog1.my() # 상속받으면 부모의 맴버도 자유롭게 사용이 가능하다.
dog1.move() 

print()
class Horse(Animal):
    pass

horse1 = Horse()
horse1.move()







    