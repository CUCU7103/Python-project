# Python에서 thread는 GIL을 따르므로 완전한 멀티태스킹이 불가능하다.
# multiprocessing으로 위의 문제를 해결할 수 있다.
# multiprocessing : 비동기적, 비결정적이다. 부분작업에 효과적이다. 주로 네트워크 작업에서 사용되어진다.
# Pool, Process를 즐겨 사용한다.

# Pool : 입력값에 대해 process들을 건너건너 분배하여 함수를 실행하는 병렬처리 수단을 제공함.

from multiprocessing import Pool
import time
import os # 시스템 영역을 사용하게 해준다.

def func(x):
    print('값', x, '에 대한 작업 pid:', os.getpid())
    time.sleep(1) # 작업시간 1초 부여함.
    return x * x

if __name__=='__main__':

    # 방법 1: 함수를 순차적으로 처리하고 있음. 프로세스 아이디 한개 사용함. 소요시간 10초
    '''
    startTime = int(time.time()) # 처리시간 체크용
   
    for i in range(1,11):
        print(func(i))
    
    endTime = int(time.time())
    '''
    
    # 방법 2 : 함수를 병렬로 처리한다. 프로세스 3개 ~ 5개아이디 사용함. 소요시간 4~5초
     
    startTime = int(time.time())
    p = Pool(processes=3) # process 3개를 사용 ( 3 ~ 5개가 적당하다)
    print(p.map(func, range(1,11))) # 10번 반복 진행함. 함수의 return 값은 list type이다.
    endTime = int(time.time())
    print('총 작업시간 :', endTime - startTime)

    
    
    
    
    
    
    
    
    
    