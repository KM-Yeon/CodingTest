import sys
sys.stdin = open("input.txt", "r")
n = int(input())
a = list(map(int, input().split()))

def digit_sum(x):
    sum = 0
    while x>0:
        sum += x % 10
        x = x // 10
    return sum

maxn = float('-inf')
for x in a:
    tot = digit_sum(x)
    if tot > maxn:
        maxn = tot
        res = x

print(res)