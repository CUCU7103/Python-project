# 다수의 그래픽 지원모듈(라이브러리중) turtle로 도형그리기
import turtle # import 진행함.
#
# p = turtle.Pen()
#
# p.forward(100)  # 기본적으로 이동방향은 오른쪽으로 설정되어져 있다.
# p.right(90)
# p.forward(100) 
# p.right(90) 
# p.forward(100) 
# p.right(90) 
# p.forward(100) 
# input()
#
# if __name__ == '__main__': # main 모듈임을 알려준다. 메인 모듈은 import를 하는 곳이라고 생각하자.
    # go()

from turtle import *
p = turtle.Pen()
p.color('red', 'yellow')
p.begin_fill()
while True:
    p.forward(200)
    p.left(170)
    if abs(p.pos()) < 1:
        break
p.end_fill()
#done()
input()