# 6021 : [기초-입출력] 단어 1개 입력받아 나누어 출력하기(설명)(py)

# 본 문제는 python 의 빠른 기초 학습을 위해 설계된 문제로서 python 코드 제출을 기준으로 설명되어 있습니다.
# ------

# 알파벳과 숫자로 이루어진 단어 1개가 입력된다.
# 입력받은 단어의 각 문자를 한 줄에 한 문자씩 분리해 출력한다.

# 예시
# s = input()
# print(s[0])
# print(s[1])
# ...

# 참고
# s[0] 은 첫 번째 문자를 의미한다.

variable = input()
length = len(variable)
for i in range(0, length):
    print(variable[i])
