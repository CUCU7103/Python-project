# 자원의 재활용 중 클래스의 포함
# 어떤 객체가 다른 객체를 참조함에 있어 자신의 맴버처럼 선언하고 사용 가능

# 사실 핸들 클래스는 별도의 모듈로 작성해야 하나 편의상 하나의 모듈에서 완성차를 
# 생성하기로 함.

class PohamHandle: # 완성차의 부품 클래스
    quantity = 0 # 핸들의 회전량
    
    def LeftTurn(self, quantity):
        self.quantity = quantity
        return '좌회전'
    
    def RigthTurn(self, quantity):
        self.quantity = quantity
        return '우회전'
    
    #....

# 완성차 클래스 작성
class PohamCar:
    turnShowMessage ='정지'
    
    def __init__(self,ownerName): # 클래스 생성시 ownerName의 값이 필요함.
        self.ownerName = ownerName
        self.handle = PohamHandle() # 클래스의 포함
        
    def TurnHandle(self,q):
        if q > 0:
            self.turnShowMessage = self.handle.RigthTurn(q) # 포함관계이다. '.' 두번 사용함
        elif q < 0:
            self.turnShowMessage = self.handle.LeftTurn(q)
        elif q == 0:
            self.turnShowMessage = '직진'
            self.handle.quantity = 0
            
            
if __name__ == '__main__': # 메인 모듈임을 명시한다.
    
    tom = PohamCar('tom')  # 생성자가 요구하는 값을 넣음    
    tom.TurnHandle(10) # 메소드 호출
    print(tom.ownerName + '의 회전량은 ' +tom.turnShowMessage + str(tom.handle.quantity))   
            
    james = PohamCar('james')  # 생성자가 요구하는 값을 넣음    
    james.TurnHandle(-10) 
    print(james.ownerName + '의 회전량은 ' +james.turnShowMessage + str(james.handle.quantity))          
            
            
            