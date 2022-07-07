import sys
sys.stdin = open("input.txt", "r")
n = int(input())

a = list(map(int, input().split()))

sum = 0 #총합
cnt = 0 #누적합

for x in a:
    if x == 1:
        cnt += 1
        sum += cnt
    else:
        cnt = 0