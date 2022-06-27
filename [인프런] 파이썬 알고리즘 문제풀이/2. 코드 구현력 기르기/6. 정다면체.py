import sys
sys.stdin = open("input.txt", "r")
a, b = list(map(int, input().split()))

cnt = [0]*(a+b+1)

for i in range(1, a+1):
    for j in range(1, b+1):
        cnt[i+j] += 1

maxn = float('-inf')
for i in range(a+b+1):
    if cnt[i] > maxn:
        maxn = cnt[i]

for i in range(a+b+1):
    if cnt[i] == maxn:
        print(i, end=' ')