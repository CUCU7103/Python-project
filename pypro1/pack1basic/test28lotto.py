# 클래스의 포함 : 로또 번호 출력
import random # 난수 출력을 위한 모듈 import

class LottoBall : # 공을 담는 역할.
    def __init__ (self, num):
        self.num = num
        
class LottoMachine:
    def __init__(self):
        self.ballList = []
        for i in range(1,46):
            self.ballList.append(LottoBall(i)) # 포함관계
            # ballList에 1~45까지 수를 담는다.
        
    def selectBall(self):
        #섞기 전 볼 출력
        for a in range(45): 
            print(self.ballList[a].num, end =' ')
        print()
        
        random.shuffle(self.ballList) # 섞는다.
        
        # 섞은 후 볼 출력
        for a in range(45):
            print(self.ballList[a].num, end =' ')  # 섞은 후 볼 출력
        
        return self.ballList[0:6]
        
            
class LottUI:
    def __init__(self): # 생성자
        self.machine = LottoMachine() # 포함
        
    def playLotto(self):
        input('로또를 뽑으려면 엔터키를 누르시오')
        selectedBalls = self.machine.selectBall() # 포함사용함.
        print()
        for ball in selectedBalls:
            print("%d" %(ball.num)) # 랜덤으로 6개의 숫자가 출력되어진다.
        
if __name__ == '__main__':
    ui = LottUI() # 인스턴스(객체) 생성, 생성자 호출
    ui.playLotto()

    # LottUI().playLotto() # 줄여쓰기가 가능하다.
    
    
    
    
    
    
    
    
    
    
    
    