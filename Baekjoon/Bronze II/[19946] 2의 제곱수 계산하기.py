############################ 문제 ############################
# 태영이의 취미는 2의 제곱수를 계산하는 것이다.

# 태영이는 2^64 = 18,446,744,073,709,551,616 이라는 것을 알고 있고 직접 2^0부터 2씩 곱해서 2^64을 구할 것이다.
# 하지만 태영이는 2씩 곱하는 와중에 1을 빼버리는 실수를 딱 한 번 해버리고 말았다.
# (실수는 단 한 번만 하며, 그 후에는 2로 곱하는 계산을 정확하게 수행한다.)

# 예를 들어, 2^1 = 2로 계산을 잘 하다가 2^2 = 3으로 계산해버리는 어이없는 실수를 해버리는 것이다.
# 그렇게 된다면 2^3 = 6 , 2^4 = 12 ... 로 계산하여 점점 오차가 커진다.
# 태영이가 구한 2^64인 N이 주어졌을 때, 태영이가 처음으로 실수한 구간을 찾아주자.
##############################################################

############################ 예제 ############################
# 예제 입력 1
# 18446744073709551615

# 예제 출력 1
# 64

# 2^63 = 9,223,372,036,854,775,808 까지는 계산을 잘 하다가
# 2^64를 (2^64)-1인 18,446,744,073,709,551,615로 계산을 잘못해버렸다.

# 예제 입력 2
# 56

# 예제 출력 2
# 3

# 2^2 = 4 까지는 계산을 잘 하다가
# 2^3을 (2^3)-1인 7로 계산을 잘못해버렸다.
# 그 뒤로 2^4 = 14, 2^5 = 28, 2^6 = 56이 되었다.
##############################################################

########################## 문제 풀이 ##########################
# 2^64를 하나 하나 곱하겠다는 뜻인데 계산하던 중간에 값에 실수로 1을 빼서 계산을 이어갔다는 것
# N = N*2, N은 2부터 시작, 그러다 실수로 중간에 N = (N*2)-1을 한 후, N = N*2를 계속해서 구했다는 뜻
# 예를 들어, 2^1 = 2로 계산을 잘 하다가 2^2 = 3으로 계산해버리는 어이없는 실수를 해버린 것
# 그렇게 된다면 2^3 = 6 , 2^4 = 12 ... 로 계산하여 점점 오차가 커진다.

# 태영이가 구한 2^64 값은 N이다.
# K를 64부터 시작하여 N을 2로 반복적으로 나누면서 K값을 1씩 빼주며 검사한다.
# N을 2로 나누었을 때 나머지가 1이 되었을 때의 K 값을 구하면 된다.

# 예를 들어 태영이가 2^6를 잘못 구한 경우 N의 값이 56라고 해보자
# K는 6부터 시작하여 검사할 것이고, N을 2로 반복적으로 나누어 보자.

# K   ==   6    |   K   ==   5   |   K   ==   4   |   K   ==   3   |
# N   ==   56   |   N   ==   28  |   N   ==   14  |   N   ==   7   |
# N%2 ==   0    |   N%2 ==   0   |   N%2 ==   0   |   N%2 ==   1   |

# 제대로 계산 되었을 때의 값
# K   ==   6    |   K   ==   5   |   K   ==   4   |   K   ==   3   |
# N   ==   64   |   N   ==   32  |   N   ==   16  |   N   ==   8   |
# N%2 ==   0    |   N%2 ==   0   |   N%2 ==   0   |   N%2 ==   0   |

# 반대로 검산을 해보면
# 2^1 = 2, 2^2 = 4, 2^3 = 8-1, 2^4 = 14, 2^5 = 28, 2^6 = 56 이런식으로 계산을 했다는 것
##############################################################

N = int(input())
K = 64

while (1):
    if(N % 2 == 1):
        break
    N //= 2
    K -= 1

print(K)
