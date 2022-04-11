import sys

input = sys.stdin.readline

for _ in range(int(input())):
    sL, sR = [], []
    for i in input().strip():
        if i == '<':
            if sL:
                sR.append(sL.pop())
        elif i == '>':
            if sR:
                sL.append(sR.pop())
        elif i == '-':
            if sL:
                sL.pop()
        else:
            sL.append(i)
    print(''.join(sL)+''.join(sR)[::-1])
