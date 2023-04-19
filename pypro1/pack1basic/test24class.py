# 클래스는 새로운 타입(형)을 만든다.
print(type(1))
print(type(1.5))

# 가수라는 직업을 가진 사람들의 공통점 : 노래를 함, ... 

# bts, IU..... 

class Singer: # Singer라는 새로운 타입을 생성함.
    titleSong = '화이팅 코리아'
    #....
    
    def sing(self):
        msg = '노래는'
        print(msg, self.titleSong,'랄랄라~')
    #...

bts = Singer()   # Singer클래스의 멤버를 전부 갖는다.
print(type(bts)) # <class '__main__.Singer'>
bts.sing() # 노래는 화이팅 코리아 랄랄라~
bts.titleSong = '작은 것을 위한 시'  # 멤버변수의 값을 새로이 생성함 기존의 titleSong 값은 은닉되어진다.
bts.sing() # 노래는 작은 것을 위한 시 랄랄라~
bts.co = 'kbs' # 새로운 멤버변수 추가함
bts.person ='7'
print('bts 소속사', bts.co)
print(bts.person)

print()
IU = Singer()
print(type(IU))
IU.sing()
# print('IU 소속사:' , IU.co) # co는 현재 bts만 가지고 있다.
