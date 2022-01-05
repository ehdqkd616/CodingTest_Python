# 6078 : [기초-종합] 원하는 문자가 입력될 때까지 반복 출력하기(py)

# 본 문제는 python 의 빠른 기초 학습을 위해 설계된 문제로서 python 코드 제출을 기준으로 설명되어 있습니다.
# ------

# 영문 소문자 'q'가 입력될 때까지
# 입력한 문자를 계속 출력하는 프로그램을 작성해보자.

arr = []
char = ''

while(1):
    char = input()
    arr.append(char)

    if(char == 'q'):
        break

for arr_char in arr:
    print(arr_char)
