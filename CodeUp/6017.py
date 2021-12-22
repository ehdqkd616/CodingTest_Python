# 6017 : [기초-입출력] 문장 1개 입력받아 3번 출력하기(설명)(py)

# 본 문제는 python 의 빠른 기초 학습을 위해 설계된 문제로서 python 코드 제출을 기준으로 설명되어 있습니다.
# ------

# 정수(integer), 실수, 문자(character), 문자열(string) 등 1개만 입력받아 한 줄로 3번 출력해보자.

# 예시
# s = input()
# print(s, s, s)  #공백으로 구분해 한 줄로 출력한다.
# 와 같은 방법으로 3번 출력할 수 있다.

# 참고
# python 언어에서는 문자/정수/실수/문자열 등 특별한 구분이 없이도 원하는 변수에 저장시켜 출력 할 수 있다.
# 하지만, 저장된 값을 이용해 계산하거나 서로 붙여 연결시키거나 잘라내는 작업을 한다면?
# 반드시 저장되어있는 값의 종류(문자/정수/실수/문자열 등)를 구분해 주어야 한다.

str = input()
print((str+' ') * 3)
