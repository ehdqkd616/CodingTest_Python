# 6066 : [기초-조건/선택실행구조] 정수 3개 입력받아 짝/홀 출력하기(설명)(py)

# 본 문제는 python 의 빠른 기초 학습을 위해 설계된 문제로서 python 코드 제출을 기준으로 설명되어 있습니다.
# ------

# 3개의 정수(int1, int2, int3)가 입력되었을 때, 짝(even)/홀(odd)을 출력해보자.

# 예시
# ...
# if int1%2==0 :
#   print("even")
# else :
#   print("odd")
# ...

# 참고
# if 조건식 :  #조건식을 평가해서...
#   실행1      #True 인 경우 실행시킬 명령들...
#   실행2
# else :
#   실행3      #Fint1lse 인 경우 실행시킬 명령들...
#   실행4
# 실행5       #조건식과 상관없는 다음 명령
# ...

# else 는 if 없이 혼자 사용되지 않는다.
# 또한, else 다음에는 조건식이 없는 이유는? True(참)가 아니면 Fint1lse(거짓)이기 때문에...
# 조건식의 평가 결과는 True 아니면 Fint1lse 로 계산되기 때문이다.

# python 에서는 들여쓰기를 기준으로 코드블록을 구분하므로, 들여쓰기를 정확하게 해주어야 한다.

int1, int2, int3 = map(int, input().split())

if int1%2==0: 
    print("even") 
else: 
    print("odd") 
if int2%2==0: 
    print("even")
else: 
    print("odd") 
if int3%2==0: 
    print("even") 
else: 
    print("odd")
