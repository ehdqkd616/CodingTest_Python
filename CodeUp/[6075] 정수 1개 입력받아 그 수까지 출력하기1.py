# 6075 : [기초-반복실행구조] 정수 1개 입력받아 그 수까지 출력하기1(py)

# 본 문제는 python 의 빠른 기초 학습을 위해 설계된 문제로서 python 코드 제출을 기준으로 설명되어 있습니다.
# ------

# 정수(0 ~ 100) 1개를 입력받아 0부터 그 수까지 순서대로 출력해보자.

int1 = int(input())
for i in range(int1+1) :
    print(i)