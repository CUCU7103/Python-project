
class Machine:
    
    def showData(self):
        coin=input('동전을 입력하세요: ')
        coin=int(coin)
        cupCount=input('몇 잔을 원하세요: ')
        cupCount=int(cupCount)
        money=CoinIn(coin,cupCount)
        
        print(money.calc(cupCount))
        
class CoinIn:
    
    def __init__(self, coin,cupCount):
        self.coin=coin
        self.cupCount=cupCount
    
        
    def calc(self, cupCount):
        if 200*cupCount > self.coin:
            return '요금이 부족합니다.'
        else:
            change=self.coin-(200*cupCount)
            return '커피 '+str(cupCount)+'잔과 잔돈 '+str(change)
    
if __name__=='__main__':
    Machine().showData()
    
    
# class Machine:
#     def __init__(self,coin,cupCount):
#         self.coin = coin
#         self.cupCount = cupCount
#
#     def showData(self):
#         res = CoinIn().culc(self.coin,self.cupCount) 
#         if res < 0:
#             print('요금이 부족합니다')
#         else:
#             print('커피 {0} 잔과 잔돈 {1} 원'.format(self.cupCount,res))
#
# class CoinIn:
#     def culc(self,coin,cupCount):
#         self.change = coin - cupCount * 200
#         return self.change
#
# if __name__ == '__main__':
#     coin = input('동전을 입력하세요')
#     cup = input('몇 잔을 원하세요')
#     m=Machine(int(coin),int(cup))
#     m.showData()