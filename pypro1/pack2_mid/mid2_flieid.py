# 파일 입출력 

import os
from sqlalchemy.sql.coercions import expect

print(os.getcwd()) # C:\work\psou\pypro1\pack2_mid 현재 경로를 알려준다.

try:
    print('텍스트 파일 읽기') 
    # mode = 'r'읽기 ,'w'쓰기,'a' 추가하기 , 'b' 바이너리 처리함. b는 혼자 사용되어지지 못한다.
    # f1 = open(r'C:\work\psou\pypro1\pack2_mid\mid2sample.txt', mode='r' , encoding= 'utf-8') # 열고 작업하고
    # 파일처리 오류 'cp949' codec can't decode byte 0xec in position 0: illegal multibyte sequence  => 한글 깨짐이다
    f1 = open(os.getcwd() + r'\mid2sample.txt', mode='r' , encoding= 'utf-8')  # 파일을 열때 기본적으로 인코딩이 윈도우의 기본 인코딩 형식을 따르기에 
                                                                               # utf-8의 변환이 필요하다.
    print(f1)
    print(f1.read())
    f1.close() # 항상 작업이 끝나면 닫아준다.
    
    print('택스트 파일 저장')
    f2 = open('mid2sample2.txt', mode = 'w', encoding ='utf-8')
    f2.write('때가 되었군 ')
    f2.write('광합성 후 만나기로\n')
    f2.close()
    print('저장완료')
    
    print('텍스트 파일 추가')
    f2 = open('mid2sample2.txt', mode = 'a', encoding ='utf-8')
    f2.write('결국 만나게')
    f2.write('\n되었다.')
    f2.close()
    print('파일 추가' )
    
    print('텍스트 파일 읽기')
    f3 = open('mid2sample2.txt', mode = 'r' , encoding ='utf-8')
    print(f3.read()) # 전체 읽기
    f3.close()
    print()
    f4 = open('mid2sample2.txt', mode = 'r' , encoding ='utf-8')
    li2 = f4.readline()
    print(f4.readline()) #한줄 읽기, 단순이 읽어서 콘솔창에 추가한다.
    print(type(li2)) # readline은 str 타입이다.
    li = f4.readlines() # 여러 줄을 읽어서 list에 저장. (여러 줄을 읽기에 list에 저장) 위에서 첫 번째 줄을 읽었음으로 그 다음 줄부터 읽어 배열에 저장함.
    print(type(li)) 
    f4.close() # 파일이나 DB등을 열고서는 항상 닫아주어야 한다.
    
except Exception as e: 
    print('파일처리 오류',e)
    

    
    
    
    