# 6035 : [기초-산술연산] 실수 2개 입력받아 곱 계산하기(설명)(py)

# 본 문제는 python 의 빠른 기초 학습을 위해 설계된 문제로서 python 코드 제출을 기준으로 설명되어 있습니다.
# ------

# 실수 2개(f1, f2)를 입력받아 곱을 출력하는 프로그램을 작성해보자.

# 예시
# ...
# m = float(f1) * float(f2)
# print(m)

# 참고
# 수 * 수는 곱(multiplication)이 계산된다.



float1, float2 = input().split()
result = float(float1)*float(float2)
print(result)

# impoart math
# print(math.prod(map(float, input().split())))