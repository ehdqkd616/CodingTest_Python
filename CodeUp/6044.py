# 6044 : [기초-산술연산] 정수 2개 입력받아 자동 계산하기(py)

# 본 문제는 python 의 빠른 기초 학습을 위해 설계된 문제로서 python 코드 제출을 기준으로 설명되어 있습니다. 
# ------

# 정수 2개(a, b)를 입력받아 합, 차, 곱, 몫, 나머지, 나눈 값을 자동으로 계산해보자.
# 단 0 <= a, b <= 2147483647, b는 0이 아니다.

 
int1, int2 = input().split()
result_plus = int(int1)+int(int2)
result_minus = int(int1)-int(int2)
result_multiply = int(int1)*int(int2)
result_quotient = int(int1)//int(int2)
result_remainder = int(int1)%int(int2)
result_divide = float(int1)/float(int2)

print(result_plus)
print(result_minus)
print(result_multiply)
print(result_quotient)
print(result_remainder)
print(f'{result_divide:.2f}')