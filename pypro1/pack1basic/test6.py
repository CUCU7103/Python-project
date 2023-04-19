 # 정규표현식 : 특정한 규칙을 가진 문자열의 집합을 표현하는데 사용하는 형식 언어.
 # re는 정규 표현식을 사용하기 위한 파이썬의 내장 모듈 
import re
  
ss = "1234 abc가나다abcABC_1234555_66'Python is fun'"
print(ss)
# findall() 함수는 정규 표현식 패턴과 대상 문자열을 받아, 패턴과 일치하는 모든 문자열을 리스트로 반환

print(re.findall(r'123', ss)) # ['123', '123'] r은 이스케이프 문자를 사용하지 않도록 설정한다.
print(re.findall(r'[0,1,2]', ss)) # ['1', '2', '1', '2']
print(re.findall(r'[0-9]', ss)) # 모든 숫자를 하나하나 찾아낸다. ['1', '2', '3', '4', '1', '2', '3', '4', '5', '5', '5', '6']
print(re.findall(r'[0-9]+', ss)) # ['1234', '1234555', '6'] 문자열에 있는 그대로의 숫자를 출력한다
print(re.findall(r'[0-9]{2}', ss)) # ['12', '34', '12', '34', '55', '66'] 2개씩 묶어 출력한다.
print(re.findall(r'[0-9]{3}', ss)) #  ['123', '123', '455'] 문자열에 있는 숫자들의 집합에서 각각 3개씩 뽑아낸다 이때 3번째 이후이거나 3개가 되지 않으면 출력x,
print(re.findall(r'[0-9]{2,3}', ss))  # ['123', '123', '455', '66'] ss에서 2자리 또는 3자리의 연속된 숫자를 모두 찾아 리스트로 반환

print(re.findall(r'[a,b]', ss)) # ['a', 'b', 'a', 'b']
print(re.findall(r'[a-bA-Z]', ss)) # ['a', 'b', 'a', 'b', 'A', 'B', 'C', 'P'] 
# 해당 문자열에서  a에서b까지 그리고 대문자 A-Z까지의 문자를 출력한다.
print(re.findall(r'[a-bA-Z]+', ss))# ['ab', 'ab', 'ABC', 'P']
print(re.findall(r'[가-힣]+', ss)) # ['가나다'] 한글 출력하기
print(re.findall(r'[^가-힣]+', ss)) # ['1234 abc', "abcABC_1234555_66'Python is fun'"]
# 한글을 제외하고 출력하기
p = re.compile('abc') # 정규식 객체를 지정한다. 즉 해당 문자열을 찾거나 정규표현식을 적용함.
print(re.findall(p ,ss)) # ['abc', 'abc']

print(re.findall(r'^123+',ss)) # 첫 글자가 1  ['123'] 
print(re.findall(r'[^123]+',ss)) # 대괄호 안의 ^는 부정, 첫 글자가 1이 아닌것 ['4 abc가나다abcABC_', "4555_66'Python is fun'"]
print(re.findall(r'[^123].',ss)) #
print(re.findall(r'a...',ss)) # a로 시작하고 아무거나 3글자

print(re.findall(r'[0-9]',ss)) # 숫자만
print(re.findall(r'\d',ss)) # 숫자만
print(re.findall(r'\D',ss)) # 숫자만 빼고
print(re.findall(r'\s',ss)) # 공백만
print(re.findall(r'\S',ss)) # 공백을 제외한 나머지

print(re.findall(r'\d+',ss))
print(re.findall(r'\d{3}',ss))

print()
p = re.compile('the', re.IGNORECASE) # flag 사용함. re.IGNORECASE 대소문자 구분하지 않는다.
print(p.findall("The Dog the dog"))  # ['The', 'the']


