# 6064 : [기초-3항연산] 정수 3개 입력받아 가장 작은 값 출력하기(설명)(py)

# 본 문제는 python 의 빠른 기초 학습을 위해 설계된 문제로서 python 코드 제출을 기준으로 설명되어 있습니다.
# ------

# 입력된 세 정수 a, b, c 중 가장 작은 값을 출력하는 프로그램을 작성해보자.
# 단, 3항 연산을 사용한다.

# 참고
# 프로그래밍언어 소스코드 작성시 모든 요소들은
# "순서에 따라 한 단계씩 실행"
# "미리 정해진 순서에 따라 하나씩 연산 수행"
# "그 때까지 연산된 결과를 이용해 다시 순서에 따라 하나씩 연산"
# ...
# 등의 원리가 적용된다.

# 따라서 3항 연산을 중첩해(괄호로 묶는 등..) 이용하면 여러 값들을 순서대로 비교해 가장 큰/작은 값을 계산할 수 있다.

# 예를 들어
# (a if a>b else b) if ((a if a>b else b)>c) else c
# 와 같은 계산식은 a, b, c 의 값 중 가장 큰 값으로 계산된다.

# 잘 이해가 되지 않는다면 어떤 순서에 따라 계산될 지 생각해보고
# 여러 가지 연산자가 동시에 사용된 식이 있을 때, 어떤 우선순위에 따라 순서대로 계산이 되는지 찾아보도록 한다.
# “연산자 우선순위”를 검색하면 우선순위와 결합방향이 나온다.
# 예를 들어 변수에 어떤 값을 대입하는 대입(assign) 연산자 = 의 우선순위는 가장 낮고, 오른쪽에서 왼쪽의 결합방향을 가진다.

# ** 3항 연산은 자주 사용되지는 않지만,
# 복잡한 계산식이나 조건 처리, 비교 구조를 간단히 표현할 수 있게 해준다.

int1, int2, int3 = map(int, input().split())
if (int1 < int2 and int1 < int3):  # int1이 int2와 int3보다 작은 경우
    min_int = int1
else:  # int1이 가장 작지 않은 경우
    if(int2 < int3):  
        min_int = int2
    else:  
        min_int = int3

# min_int = min(int1, int2, int3)
print(min_int)
