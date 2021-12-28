# 6070: [기초-조건/선택실행구조] 월 입력받아 계절 출력하기(설명)(py)

# 본 문제는 python 의 빠른 기초 학습을 위해 설계된 문제로서 python 코드 제출을 기준으로 설명되어 있습니다.
# ------

# 월이 입력될 때 계절 이름이 출력되도록 해보자.

# 월: 계절 이름
# 12, 1, 2: winter
# 3, 4, 5: spring
# 6, 7, 8: summer
# 9, 10, 11: fall

# 예시
# ...
# if n//3 == 1:
#     print("spring")
# ...

# 참고
# 때때로 수들의 특징을 관찰하고 이용하면 매우 간단히 해결할 수도 있다.

month = int(input())
if month//3 == 1 :      # 몫이 1
    print("spring") 
elif month//3 == 2 :    # 몫이 2
    print("summer")
elif month//3 == 3 :    # 몫이 3
    print("fall")
else :
    print("winter")     # 몫이 0 혹은 4