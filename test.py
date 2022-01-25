N, W, H = map(int, input().split())
D = ((W ** 2) + (H ** 2)) ** 0.5
Answer = []

for i in range(N):
    stick = int(input())
    if stick <= W or stick <= H:
        Answer.append("DA")
    elif stick <= D:
        Answer.append("DA")
    else:
        Answer.append("NE")

for a in Answer:
    print(a)