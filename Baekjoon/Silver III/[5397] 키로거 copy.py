N = int(input())

for i in range(N):
    left = []
    right = []
    pwd = input()

    for j in pwd:
        if j == "-":
            if left:
                left.pop()
        elif j == "<":
            if left:
                right.append(left.pop())
        elif j == ">":
            if right:
                left.append(right.pop())
        else:
            left.append(j)

    left.extend(reversed(right))
    print("".join(left))
