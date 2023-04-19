# 예외 처리 : 파일, 키보드, 네트워크, DB등의 외부 장치와의 작업 시 예기치 않은 에러 대처
# 자바와 달리 강요는 아니다.

def divide(a,b):
    return a / b

print('뭔가를 하다가...')

# 
# c = divide(5,2)
# c = divide(5,0)  ZeroDivisixxxxxxonError

try: # .java의 try-catch
    c = divide(5,2)
    # c = divide(5,0)
    aa = [1,2]
    print(aa[2])
    
    # f = open(r'c:/work/nice.xt')  # 파일 열기 진행 
    # print(f)
    
except ZeroDivisionError: # 해당 에러 발생시 수행되어진다.
    print('두번째 수는 0을 주지 마세요')
    
except IndexError as e: 
    print('인덱스 에러: ',e) # IndexError 인덱스 에러:  list index out of range
    
except Exception as err:
    print('에러 : ', err)
    
finally:
    print("에러 유무에 따라 상관없이 반드시 수행한다.")

print('---------------------------------------------------------------------------------------------------------------------------------------------')

def PositiveDivide(a,b):
    if(b < 0):
        raise NegativeDivideErr(b) # 에러발생 시킴
# 개발을 하다보면 사용자의 입력이나, 프로그램이 돌아가다가 우리가 의도하지 않게 돌아가는 것을 방지하기 위해서 
# 일부러 에러를 발생시켜야 하는 경우 에러를 발생시킨다.
    return a / b

class NegativeDivideErr(Exception): # 발생된 에러를 처리하는 클래스
                                   
    def __init__(self,value):
        self.value = value
try:
    imsi = PositiveDivide(10, 2)
    imsi2 = PositiveDivide(10, -2) # 오류발생 
    
except NegativeDivideErr as e :  # 클래스에서 처리된 값을 출력하는 역할을 진행한다.
    print('에러 : 두번째 값이 ' ,e.value)
    
except Exception as e:
    print('와우 에러 :',e)



print('프로그램 종료')
