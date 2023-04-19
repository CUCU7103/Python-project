# 파이썬 클래스 문제 3번 (카페)

class Animal:
    def move(self):
        pass # 내용 없음 -> 오버라이딩 예정이다.

class Dog(Animal): # 단일 상속이다.
    name = '개'
    def move(self):
        print("댕댕이는 낮에 돌아다님")
        

class Cat(Animal): # 단일 상속이다.
    name = '고양이'
    def move(self):
        print("고양이는 밤에 돌아다님")
        print("눈빛이 빛남")

class Wolf(Dog,Cat): # 다중 상속이다. 먼저 상속받은 클래스를 따라간다.
    pass

class Fox(Cat,Dog): # 다중 상속이다.
    def move(self):
        print("나는 움직이는 불여우")
        
    def foxMethod(self):
        print('여우 고유 메소드')

dog = Dog() # 인스턴스 생성, 생성자를 부른다.
print(dog.name)
dog.move()
print()
cat = Cat()
print(cat.name)
cat.move()
print("-------------------------------------------------")
wolf = Wolf() #
print(wolf.name) 
wolf.move()
print("------------------------------------------------")
fox = Fox() #
print(fox.name) 
fox.move()
print()
fox.foxMethod()
print(Fox.__mro__) # 클래스 탐색 순서를 확인할 수 있다. 상속받은 순서를 확인 할 수있다.
#<class '__main__.Fox'>, <class '__main__.Cat'>, <class '__main__.Dog'>, <class '__main__.Animal'>, <class 'object'>)
print(Wolf.__mro__)
#(<class '__main__.Wolf'>, <class '__main__.Dog'>, <class '__main__.Cat'>, <class '__main__.Animal'>, <class 'object'>)

print()
anis = [dog,cat,wolf,fox]
for a in anis:
    a.move() # 다형성이 구현되고 있다.
    print()
    
    
