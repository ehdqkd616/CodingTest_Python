############################ 문제 ############################
# 단어 시계는 시각을 단어를 이용해서 표현하는 시계이다. 다음은 몇 가지 예시이다.

# 5:00 → five o' clock
# 5:01 → one minute past five
# 5:10 → ten minutes past five
# 5:15 → quarter past five
# 5:28 → twenty eight minutes past five
# 5:30 → half past five
# 5:40 → twenty minutes to six
# 5:45 → quarter to six
# 5:47 → thirteen minutes to six
# 분 = 0이면 "o' clock"을 사용하고, 1 ≤ 분 ≤ 30은 "past"를, 30 < 분이면 "to" 를 사용한다.

# 시각이 주어졌을 때, 단어 시계에서 사용하는 표현으로 출력해보자.
##############################################################

############################ 입력 ############################
# 첫째 줄에 시를 나타내는 h(1 ≤ h ≤ 12),
# 둘째 줄에 분을 나타내는 m(0 ≤ m < 60)이 주어진다.
##############################################################

############################ 입력 ############################
# 첫째 줄에 입력으로 주어진 시각을 단어 시계에서 사용하는 표현으로 출력한다.
##############################################################

############################ 예제 ############################
# 예제 입력 1
# 5
# 47

# 예제 출력 1
# thirteen minutes to six

# 예제 입력 2
# 3
# 0

# 예제 출력 2
# three o' clock

# 예제 입력 3
# 7
# 15

# 예제 출력 3
# quarter past seven

# 예제 입력 4
# 12
# 41

# 예제 출력 4
# nineteen minutes to one
##############################################################

import sys

h = int(sys.stdin.readline())
m = int(sys.stdin.readline())

h_list = ['zero', 'one', 'two', 'three', 'four', 'five',
          'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'one']
# 시간 부분 리스트

m_list = ['o\' clock', 'one', 'two', 'three', 'four', 'five', 'six', 'seven',
          'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen',
          'quarter', 'sixteen', 'seventeen', 'eighteen', 'nineteen', 'twenty',
          'twenty one', 'twenty two', 'twenty three', 'twenty four', 'twenty five',
          'twenty six', 'twenty seven', 'twenty eight', 'twenty nine', 'half']
# 분 부분 리스트


def define(minute, hour, o_past_to, time_set):
    if minute == 1:  # 1일떄는 minute로 출력 나머지는 minutes로 출력
        print('%s minute %s %s' %
              (m_list[minute], o_past_to, h_list[hour + time_set]))
    elif minute == 15 or minute == 30:
        print('%s %s %s' %
              (m_list[minute], o_past_to, h_list[hour + time_set]))
    else:
        print('%s minutes %s %s' %
              (m_list[minute], o_past_to, h_list[hour + time_set]))


if m == 0:
    print('%s %s' % (h_list[h], m_list[m]))
elif 1 <= m and m <= 30:
    define(m, h, 'past', 0)
else:
    m = 60 - m
    define(m, h, 'to', 1)
