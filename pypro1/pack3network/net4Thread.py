# thread : light weigth process라고도 함.
# process 내에서 수행되며 같은 실행단위를 공유한다.
# multi thread로  mulit tasking 효과 (병렬처리)
# 동시에 작업하는 것 처럼 보이나 그건 아니다 빠른속도로 여러작업을 번갈아가며 처리하는것
# 네트워크 등의 작업에 많이 쓰이고 있다.
# thread는 랜덤하게 수행된다 (스레드 스케줄러에 의해서)... 모든 스레드가 종료되어야 프로세스가 종료되어진다.
# 프로세스는 스레드에 의해 처리된다.

import threading, time

def run(id): # 자바에서는 run을 사용해야 하지만 파이썬에서는 상관이 없다.
    for i in range(1,51):
        print('id :{}-->{}'.format(id,i) )
        # time.sleep(0.1) 지연시간을 부여함.

# thread를 사용하지 않은 경우
# run(1) # 순차적으로 실행되어진다.
# run(2) # 

# thread를 사용한 경우
# threading.Thread(targer=실행함수이름, args=...) args는 줄 수도 그렇지 않을 수도 있다.

th1 = threading.Thread(target=run, args=('일',)) # 사용자 정의 스레드
th2 = threading.Thread(target=run, args=('둘',)) # 사용자 정의 스레드
th1.start() # thread 대상함수가 실행되어진다.
th2.start() # thread 대상함수가 실행되어진다.


th1.join() # 사용자 스레드가 종료될 때 까지 메인 스레드의 대기를 요청하는 것
th2.join() # 즉 사용자 스레드가 끝나고 메인스레드 작업이 처리되는 것
print('프로그램 종료') # 메인 스레드