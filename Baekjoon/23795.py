# 당신은 폴리매스 왕국의 암호 개발자 친구로부터 개발을 요청받아 암호 제작을 돕기로 했습니다.
# 친구가 고안한 암호는 다음과 같이 작동합니다. 1에서 9까지의 숫자로 이루어진 문자열 $A$와 $B$가 있을 때, 이 둘이 공통으로 가지는 부분 문자열 중 길이가 $K$인 것이 비밀번호가 됩니다. (부분문자열의 정의는 다음 페이지에 있습니다.) 예를 들어, $A=1122$, $B=1223$, $K=2$라면, 비밀번호로 가능한 문자열은 $12$, $22$입니다.
# 친구는 문자열 $A$와 암호 $P$를 이미 정해 놓았고, $B$를 정하려고 합니다. 비밀번호로 가능한 문자열이 여러 개일 경우 보안이 약해질 수 있기 때문에, $P$ 이외에 다른 비밀번호가 나와서는 안 됩니다. 친구를 도와 이 조건을 모두 만족하는 $B$를 아무거나 하나 찾아 주도록 합시다. 문자열이 너무 길면 힘들기 때문에, $B$의 길이는 100 이하여야 합니다.
# 조건을 만족하는 문자열 $B$가 항상 존재함이 보장됩니다.

A = input()
P = input()