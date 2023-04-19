# 사용자 정의 함수
 
def DoFunc1():
    print('DoFunc1 수행')

DoFunc1() # 함수를 실행하라
DoFunc1
print(type(DoFunc1)) # <class 'function'> 모든 것이 전부 클래스이다.
print(DoFunc1, id(DoFunc1))  # <function DoFunc1 at 0x0000021ED8453E20> 2331500690976

print()
def DoFunc2(para1, para2): # 함수명(매개변수,,) parameter
    su1 = para1 # 5
    imsi = su1 + para2 # 12
    result = DoFunc3(imsi) # DoFunc3 호출함.  return "성공"
    print(result + ' DoFunc2 수행')
    
def DoFunc3(imsi):
    print(imsi)
    return "성공"

DoFunc2(5,7) # 함수명(인수) argument


