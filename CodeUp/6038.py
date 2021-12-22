# 6038 : [기초-산술연산] 정수 2개 입력받아 거듭제곱 계산하기(설명)(py)

# 본 문제는 python 의 빠른 기초 학습을 위해 설계된 문제로서 python 코드 제출을 기준으로 설명되어 있습니다.
# ------

# 정수 2개(a, b)를 입력받아
# a를 b번 곱한 거듭제곱을 출력하는 프로그램을 작성해보자.

# 예시
# ...
# c = int(a)**int(b)
# print(c)

# 참고
# python 언어에서는 거듭제곱을 계산하는 연산자(**)를 제공한다.
# 일반적으로 수학 식에서 거듭제곱을 표현하는 사용하는 서컴플렉스/케릿 기호(^)는 프로그래밍언어에서 다른 의미로 쓰인다.

int1, int2 = input().split()
result = int(int1)**int(int2)
print(result)

# import math
# print(math.pow(int(int1), int(int2)))