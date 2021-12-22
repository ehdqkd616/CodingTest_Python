# 6034 : [기초-산술연산] 정수 2개 입력받아 차 계산하기(설명)(py)

# 본 문제는 python 의 빠른 기초 학습을 위해 설계된 문제로서 python 코드 제출을 기준으로 설명되어 있습니다.
# ------

# 정수 2개(a, b)를 입력받아 a에서 b를 뺀 차를 출력하는 프로그램을 작성해보자.

# 예시
# ...
# c = int(a) - int(b)
# print(c)

# 참고
# 수 - 수는 차(subtraction)가 계산된다.

int1, int2 = input().split()
result = int(int1)-int(int2)
print(result)
