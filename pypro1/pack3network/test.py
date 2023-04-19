# i = 0
# while True:
#     if i % 10 != 3: # 일의 자리가 3이 아닌 수만 
#         i += 1
#         continue    # 건너뛴다.   즉 일의 자리가 3인 수만 남는다.
             
#     if i > 100: break # i가 100 이상이면 반복문을 중지한다.
               
#     print(i, end=' ')
#     i += 1

i = 10
while  i < 1:
    star =(11 - i) * '*'
    i-=1
    print(star)

# # i = 10
# # while i <1:
# #     j=1
# #     if 
# for i in range(10,0,-1):
#     print(""*(10-i) +'*'*(i))
i = 10
while i > 0:
    print( ' ' * (10-i) +'*' * i)
    i -=1
    # i가 10일 때 고이
    
# 빈 공백문자열을 먼저 출력하고 그 뒤에 별을 출력하는 방법이다.
# 즉 빈 공백문자열 크기만큼 별을 출력하면된다.