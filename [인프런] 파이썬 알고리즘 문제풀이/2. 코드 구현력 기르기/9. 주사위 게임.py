import sys
sys.stdin = open("input.txt", "r")
n = int(input())

maxn = float('-inf')
for i in range(n):
    tmp = input().split()
    tmp.sort()
    a, b, c = map(int, tmp)

    if a == b == c:
        cost = 10000 + a * 1000
    elif (a == b) or (b == c): # 정렬되어 있으므로 2가지값이 같은경우만 구현
        cost = 1000 + b * 100
    else:
        cost = c * 100

    if cost > maxn:
        maxn = cost

print(maxn)