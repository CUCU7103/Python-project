
# mdays = int(input())
# if mdays % 4 == 0 && mdays % 100 !=0 || mdays % 400 == 0:
#         print('{}년은 윤년 ".format(mdays,))
# else :
#         print('{}년은 평년 ".format(mdays,))
#

# if mdays % 4 == 0 and mdays % 100 !=0 or mdays % 400 == 0:
#         print('{}년은 윤년 '.format(mdays))
# else :
#         print('{}년은 평년 '.format(mdays))



# 아래 코드가 동작하도록 자전거 클래스(Bicycle class)를 정의하시오.
# 조건1 : 멤버 변수는 name, wheel, price 이다.
# 조건2 : 바퀴 가격은 바퀴수 * 가격이다. (배점:10)
# gildong = Bicycle('길동', 2, 50000)      # name, wheel, price
# gildong.display()
# 길동님 자전거 바퀴 가격 총액은 100000원 입니다
#
# class Bicycle:
#     name =''
#     wheel=0
#     price = 0
#     def __init__(self,name, wheel, price):
#         self.name = name
#         self.wheel= wheel
#         self.price = price
#
#     def display(self):
#         Pay = self.wheel * self.price
#         print('길동님 자전거 바퀴 가격 총액은 {}원 입니다.'.format(Pay))
#
# gildong = Bicycle('길동', 2, 50000) 
# gildong.display()
        
# i = 1        
# while i <= 10:
#     j = 1
#     res =''
#     while j <= i:
#         res = res + "*" 
#         j += 1 
#     print(res)
#     i += 1
        
    
for i in range(10,0,-1):
    print('*' * i)


        
    