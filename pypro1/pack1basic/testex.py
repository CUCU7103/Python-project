
class Machine:
    def showData(self):
        coin = input("동전을 입력하세요")
        coin = int(coin)
        cupCount = input("몇 잔을 원하세요")
        cupCount = int(cupCount)
        money = CoinIn(coin,cupCount)
        
        
class CoinIn:
    def __init__(self,coin,cupCount):
        self.coin = coin
        self.cupCount = cupCount
    
    def calc(self, cupCount):
        if 200 * cupCount > self.coin:
            return'요금이 부족합니다.'
        else: 
            change = self.coin - (200 * cupCount)
            return '커피' + str(cupCount) + '잔과 잔돈' + str(change)     
        
if __name__ == '__main__':
    Machine().showData()
    
      
   