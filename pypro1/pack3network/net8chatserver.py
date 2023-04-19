# 멀티 채팅 서버 - socket, thread가 필요하다.

import socket
import threading

ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # 
ss.bind(('192.168.0.8',5555)) # ip주소 포트번호를 소캣에 바인드한다. ipconfig으로 ip 확인해보기 
# socket.listen(backlog)
# backlog 파라미터는 동시에 대기할 수 있는 최대 연결 요청 수를 지정합니다.
ss.listen()
print('채팅 서버 서비스 시작....')

users = [] # 클라이언트 정보를 list로 받는다.

def chatUser(conn): # 멀티태스킹 진행중....
    name = conn.recv(1024) # 아이디를 받는 역할
    data = '^^ ' + name.decode('utf-8') + '님 입장'
    print(data)
    
    try: 
        for p in users: # 접속자들에게 알림, 
            p.send(data.encode('utf_8'))
        while True: 
            msg = conn.recv(1024) # 클라이언트의 메세지를 받음
            if not msg:continue # 없으면 반복문 다시 시작
            chat_data = name.decode('utf_8') + '님 메세지' + msg.decode('utf_8')
            print('수신 자료 : ' , chat_data)
            
            for p in users: # 접속
                p.send(data.encode('utf_8'))
                
                
        
    except:
        users.remove(conn) # 클라이언트의 접속 해제인 경우
        data = 'ㅠㅠ ' + name.decode('utf-8') + '님 퇴장~'
        print(data)
        if users:
            for p in users:
                p.send(data.encode('utf-8'))
        else: 
            print('exit')
            
while True: # 클라이언트의 접속을 계속 기다린다. (무한루프를 통해서)
    conn, addr = ss.accept() # 소캣정보와, 클라이언트 정보(주소) 콜백함수
    users.append(conn) # 해당 클라이언트의 소캣을 list에 저장한다.
    th = threading.Thread(target=chatUser,args=(conn,)) # 사용자 스레드를 생성한다. 
    th.start()
    
    
    
    
    
    
# Multi Chating Server - socket, thread
#
# import socket 
# import threading
#
# ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# ss.bind(('192.168.0.82', 5555))
# ss.listen()
# print('채팅 서버 서비스 시작...')
#
# users = []
#
# def chatUser(conn):
#     name = conn.recv(1024)
#     data = '^^ ' + name.decode('utf-8') + '님 입장~'
#     print(data)  # 안찍어도 되지만 서버에 찍어봄
#
#     try:  
#         for p in users:     # users에 모든 사람에게 입장한 사실 알려주기
#                 p.send(data.encode('utf-8'))
#         while True:
#             msg = conn.recv(1024)
#             if not msg:continue
#             chat_data = name.decode('utf-8') + '님 메세지:' + msg.decode('utf-8')
#             print('수신 자료: ',chat_data) 
#             for p in users:     # users에 모든 사람에게 입장한 사실 알려주기
#                 p.send(chat_data.encode('utf-8'))
#
#     except:
#         users.remove(conn)  # 클라이언트에 접속 해제인 경우
#         data = 'ㅠㅠ ' + name.decode('utf-8') + '님 퇴장~'
#         print(data)
#         if users:
#             for p in users:
#                 p.send(data.encode('utf-8'))
#         else:
#             print('exit')
#
# while True:  # 클라이언트의 접속 무한대기
#     conn, addr = ss.accept()        
#     users.append(conn)  # 해당 클라이언트의 소켓을 list에 저장
#     th = threading.Thread(target=chatUser , args=(conn,))
#     th.start()
    
    
    
    
    