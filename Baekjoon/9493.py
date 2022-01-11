# 문제
# 기차보다 빠른 비행기를 타기 위해 더 많은 돈을 지불하는것이 과연 그만한 가치가 있는 것일까?

# 거리 M(Km)이 주어졌을때 기차의 속도 A(Km/h)와 비행기의 속도 B(Km/h)로 달렸을때 발생하는 시간의 차를 계산하여라.

# 입력
# 한 줄에 테스트 케이스가 하나씩 주어진다. 각 테스트 케이스는 세 개의 정수 M(1 ≤ M ≤ 10,000), A 그리고 B(1 ≤ A < B ≤ 1000)로 이루어져 있다. 정수는 공백으로 구분되어 있다.

# 마지막 테스트 케이스는 0 세 개로 나타내며, 따로 처리하지 않고 프로그램을 종료한다.

# 출력
# 각 테스트 케이스마다 다음 형식으로 시간을 출력한다.

# H:MM:SS
# 분(MM)과 초(SS)는 모두 2자리로 표현되며 그렇기에 필요에 따라 0을 출력하는 경우도 존재한다. 초(Second)는 반올림하고, 시(Hour)는 최소 자리로 나타낸다. 출력에 공백은 없으며 테스트 케이스 사이에 빈 줄은 출력하지 않는다.

# 거리 = 속도 * 시간
# 시간 = 속도 / 거리

while 1:    
    length_M, speed_A, speed_B = map(int, input().split())
    
    if length_M == speed_A == speed_B == 0 :
        break
    
    time = round(abs(length_M/speed_A - length_M/speed_B) * 3600)
    hour = time // 3600
    minute = (time % 3600) // 60
    second = time % 60
    print(f'{hour}:{minute:02}:{second:02}')