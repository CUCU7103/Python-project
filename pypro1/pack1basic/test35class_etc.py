# 싱글톤 패턴 : 객체 변수 여러 개를 사용하여 한 개의 객체를 생성

class SingletonClass: # 싱글톤 패턴을 사용한다.
    inst = None
    
    # 파이썬에서 객채를 생성해보면 __init__ 이 생성되기 전에 항상 __new__ 가 먼저 실행되며,
    # 이 때 객체에 메모리가 할당
    def __new__(cls):
        if cls.inst is None:
            cls.inst = object.__new__(cls)
        return cls.inst
    
   
    
class SubClass(SingletonClass):
    pass

s1 = SubClass() # 싱글톤을 사용하여 두 객체의 주소가 동일하다.
s2 = SubClass()
print(id(s1),id(s2))

print('-----------------')
# 사용 가능한 맴버 변수를 고정함.
class Animal:
    __slots__ = ['name','age'] # 맴버변수 고정

    def printData(self):
        print(self.name, self.age)
    
    #....
    
ani = Animal()
ani.name = "호랑이"
ani.age = 3
# ani.eat ='동물' => 멤버변수가 고정되어서 더 이상 추가가 불가하다. __slots__로 인함.
ani.printData()




