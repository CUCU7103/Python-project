class CoinIn:
    def __init__(self):
        pass
    
    def calc(self, coin, cupCount):
        if 200 * cupCount > coin:
            return '요금이 부족합니다.'
        else:
            change = coin - (200 * cupCount)
            return '커피 ' + str(cupCount) + '잔과 잔돈 ' + str(change)

class Machine:
    def __init__(self):
        self.coinIn = CoinIn()   # 포함

    def showData(self):
        coin=input('동전을 입력하세요: ')
        coin=int(coin)
        cupCount=int(input('몇 잔을 원하세요: '))
        
        print(self.coinIn.calc(coin, cupCount))

if __name__=='__main__':
    Machine().showData()