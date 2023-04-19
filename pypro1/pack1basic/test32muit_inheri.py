# 다중 상속 
# 파이썬에서는 다중 상속을 지원한다.
class Tiger: 
    data = "호랑이 세계"
    
    def Cry(self):
        print('호랑이 : 어흥')
    
    def Eat(self):
        print('맹수는 생고기를 좋아함.')
        
class Lion:
    
    def Cry(self):
        print('사자 : 으르렁')
    
    def Hobby(self):
        print('백수의 왕은 프로그래밍')
        
class Liger1(Tiger,Lion): # 맴버가 중복됬을 시 먼저 적은 클래스(상속된)가 우선순위를 가진다. 
    pass

lig1 = Liger1()
lig1.Cry() # 호랑이 : 어흥
lig1.Eat() # 맹수는 생고기를 좋아함. Tiger의 맴버를 사용가능하게 함.
lig1.Hobby() # Lion의 맴버를 사용한다.

print()

class Liger2(Lion, Tiger):
    data ="라이거 만세" # 은닉화
    
    def play(self):
        print('play는 라이거 고유메소드')
        
    def Hobby(self): # 메소드 오버라이딩
        print('라이거는 사색을 즐김')
    
    def show(self):
        self.Hobby()
        super().Hobby()
        print(self.data+" "  +super().data)        
        
lig2 = Liger2()
lig2.Cry() # 먼저 적어준 lion이 우선순위
lig2.show()
      
        
        
        