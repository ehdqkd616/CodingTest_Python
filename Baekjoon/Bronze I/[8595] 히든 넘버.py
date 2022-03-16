import re                # re : regex , 정규 표현식용 내장 모듈
import sys

cnt = int(sys.stdin.readline().rstrip())  # int로 형변환하여 받으면 개행문자가 사라짐
st = sys.stdin.readline().rstrip()   # 입력문자열
str = list(st)  # 문자를 리스트로 반환
temp = ''
result = 0

for i in st:
    if i >= '0' and i <= '9':  # 내가 받은 문자열이 숫자면
        temp += i               # 그 숫자를 temp에 더함
    else:
        if temp:                # temp가 공백이 아니면
          #  e = float(temp)     # 실수로 변환 후
            result += int(temp)    # 정수로 변환하여 result에 더한다
            temp = ''           # 다음 수를 받기 위해 공백으로 초기화

if temp:                        # 마지막에 숫자가 나왔을 경우를 예외처리
    e = float(temp)
    result += int(e)

print(result)


# <Second>

n = input()              # 단어의 길이 Input
string = input()         # 단어 Input

# findall : 문자열 중 패턴과 일치하는 모든 부분 탐색(반환 : list)
numbers = re.findall("\d+", string)
numbers = list(map(int, numbers))    # list 요소를 정수형으로 변환

print(sum(numbers))                 # 합 출력
