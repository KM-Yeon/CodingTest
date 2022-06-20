import sys
sys.stdin = open("input.txt", "r")
n = int(input())
a = list(map(int, input().split()))

ave = int(sum(a)/n + 0.5)
#round는 round_half_even 방식을 택한다.
# 따라서 round는 논리적 오류가 발생할 수 있으므로 0.5를 더하여 int로 씌우는 방법을 택한다.

min = float('inf')

for idx, x in enumerate(a):
    tmp = abs(x - ave)
    if tmp < min:
        min = tmp
        score = x
        res = idx+1
    elif tmp == min:
        if x > score:
            score = x
            res = idx+1

print(ave, res)