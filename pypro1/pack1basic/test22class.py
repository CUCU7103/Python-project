# class 
# 파이썬에선는 전부 public이다..

class Car:  # 객체로 취급되어진다.
    handle  = 0 # 맴버변수
    speed = 0
    
    def __init__ (self, name, speed): 
        self.name = name  # 자바와의 다른점이다.
        self.speed = speed
    
    def showData(self):
        km = '킬로미터'  # 지역변수
        msg = '속도' + str(self.speed) + km #  self는 this라고 생각, self는 주소를 담는다.
                                            #  맴버변수를 사용할때는 self가 선행되어야한다.
        return  msg  
    
print(id(Car), type(Car))   
print(Car.handle) # 원형(prototype) 클래스의 맴버 호출함.
                  # 원형 클래스는 공유자원을 갖고있다.
                  
car1 = Car('tom', 5) # 생성자를 호출
                     # Car type의 오브젝트가 생성되었다. 자바하고 다른 점은 new 키워드가 붙지 않는다는 것,
                     # instance 됨 Car type 객체가 생성이 되었다.
                     # 원형 클래스에서 파생되어졌다 
                     # 없는 값들은 자동적으로 원형클래스에서 찾아진다. 단 메소드는 원형클래스만 가지고 있다.
                     # 여기에는 handle 값이 들어있지 않다.
print('car1:', car1.handle, car1.name, car1.speed)
car1.color = '파랑'
print('car1: ' , car1.color) # car1 객체에 color 멤버를 추가함


print()
car2 = Car('james', 7) # Car type의 오브젝트가 생성되었다
                       # 당연히 car1 와 car2는 다른 객체이다.
                       
print('car2:', car2.handle, car2.name, car2.speed)
# print('car2:', car2.color)
# print('Car: ', Car.color)

print(id(car1), type(car1)) # 같은 Car type 설계도는 같으나 소유주가 다르다는 개념
print(id(car2), type(car2))
print(car1.__dict__)
print(car2.__dict__) # 각 클래스의 멤버를 확인하는 방법

print('method ---- ')
print(car1.showData()) # Bound Method call, car1의 주소를 타고 들어간다. 
print(car2.showData()) 

car1.speed = 80  # 파생된 인스턴스  car1, car2에 speed값을 부여한다.
car2.speed = 110 # 그렇다면 car1와 car2은 각각 speed값을 갖게 되었으니 프로토타입 클래스에서 더 이상 speed를 받아오지 않는다.

print(car1.showData()) 
print(car2.showData()) 

Car.handle = 1 # 원형 클래스의 값을 변경했으니 파생되는 인스턴스들의 값은 자동으로 변경되어진다.
print(car1.handle) 
print(car2.handle)

Car.speed = 123 # 각 객체가 이미 해당 변수의 값을 가지고 있기에 프로토타입 클래스의 값을 참조할 이유가 없다. 
print(car1.speed) # 만일 각 객체의 speed값이 없다면 변경되어지지만 이미 값을 가지고 있다.
print(car2.speed)
 







