# with 구문이 있다.
'''
리소스를 with문법을 통해 with 절 내에서만 액세스를 가능하게 하고, 블록을 나가는 경우 어떤 이유든간에 리소스를 해제하게 된다.
즉 close()의 별도 사용이 필요없다.
다음과 같은 구조로 사용한다.

with {expression} as {variable}:
    block..
'''

try:
    # 파일로 저장
    with open('mid3sample.txt', mode ='w', encoding ='utf-8') as f1:
        f1.write('파이썬으로 문서 저장')
        f1.write('with 구문 사용\n')
        f1.write('close() 자동 처리')
    
    print('저장완료') # close가 생략되기에 파일 처리에서 많이 사용한다.
      
    # 파일 읽기
    with open('mid3sample.txt', mode = 'r', encoding ='utf-8') as f2:      
        print(f2.read())
    


        
except Exception as e:
    print('파일처리 오류 :' , e)
    
print("------------------------------------------") 
# 객체를 파일로 저장 - pickling
# pickle
# 별도의 객체를 파일로 저장한다.
# 텍스트 상태의 데이터가 아닌 파이썬 객체 자체를 바이너리 파일로 저장하는 것이라고 한다 
# 텍스트 형태로 파일을 저장하는 것이 아니라 dictionary, list, tuple과 같은 형태로 필요한 부분을 저장하는 것이다
import pickle

try:
    dictdata = {'tom':'111-1111' , '길동':'222-2222'}
    listdata = ['마우스', '키보드']
    tupledata = (dictdata, listdata)
    
    # 저장작업이다.
    with open('mid3hi.dat', mode='wb') as f3: # b는 혼자서 사용이 불가함.
        pickle.dump(tupledata,f3)
        pickle.dump(listdata,f3)
        
    print('객체를 파일로 저장 성공')
    
    # 읽기
    with open('mid3hi.dat', mode='rb') as f4:
        a,b = pickle.load(f4) # 파일 읽기를 진행합니다. 값
        c = pickle.load(f4)
        print(a) # {'tom': '111-1111', '길동': '222-2222'}
        print(b) # ['마우스', '키보드']
        print(c) # ['마우스', '키보드']
        
except Exception as e:
    print('err : ', e)















    
    
    
    
    
    
    
    