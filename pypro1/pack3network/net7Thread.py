# 공유자원 충돌방지 / 스레드 활성화,비활성화 
import threading,time

bread_plate = 0; # 빵 접시 : 공유자원
lock = threading.Condition() # lock을 위한 조건변수이다.

class Maker(threading.Thread): # 빵 생산자 클래스
    def run(self):
        global bread_plate
        for i in range(1,31):
            lock.acquire() # 공유자원 충돌방지, 락 생성함.
            while bread_plate >= 10:
                print('빵 생산 초과, 생산을 대기합니다.')
                lock.wait() # 스레드 비활성화.
            bread_plate += 1 
            print('빵 생산: ', bread_plate)
            lock.notify() # 스레드 활성화
            lock.release() # 락 해제

            

class Consumer(threading.Thread): # 빵 소비자 클래스
    def run(self):
        global bread_plate
        for i in range(1,31):
            lock.acquire() # 공유자원 충돌방지
            while bread_plate < 1: # 
                print('빵이 없어서 기다리는 중.')
                lock.wait() # 스레드 비활성화.
            bread_plate -= 1 
            print('빵 소비: ', bread_plate)
            lock.notify() # 스레드 활성화
            lock.release() # 락 해제
           
            
mak = []; con=[]
for i in range(1,6): # 빵 생산자 수           
        mak.append(Maker())

for i in range(1,6): # 빵 소비자 수       
        con.append(Consumer())

for th1 in mak:
    th1.start()
            
for th2 in con:
    th2.start()
    
for th1 in mak:
    th1.join()
    
for th2 in con:
    th2.join()          
            
print('장사 끝')
            
            
            