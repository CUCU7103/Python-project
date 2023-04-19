# Thread를 이용해 동적으로 시간을 출력한다
import time
import threading

# 이렇게 시간을 출력하면 실행시킨 당시의 시간만 찍힌다 
now = time.localtime() # 시간을 출력하기 위한 객체 선언
print('현재는 {}일 {}시 {}분 {}초'.format(now.tm_mday,now.tm_hour,\
                                   now.tm_min,now.tm_sec))

# Thread를 사용해서 지속적으로 시간을 출력한다.
def show_data():
    now = time.localtime() 
    print('현재는 {}년 {}월 {}일'.format(now.tm_year,now.tm_mon,now.tm_mday))
    print('현재는 {}시 {}분 {}초'.format(now.tm_hour,now.tm_min,now.tm_sec))

def myrun():
    while True:
        now2 = time.localtime()
        if now2.tm_min == 28:
            break
        show_data()
        time.sleep(1) # 지연시간을 부여한다. 1초단위로 찍히도록 함.

th = threading.Thread(target=myrun()) #  사용자 정의 스레드 생성
th.start() # 스레드를 작동시킨다.

th.join() # 사용자 스레드 작업 후 메인스레드 작업 실행한다.
print('프로그램 종료')