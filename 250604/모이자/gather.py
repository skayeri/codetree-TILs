import sys

n = int(input())
A = list(map(int, input().split()))

INT_MAX = sys.maxsize

min_sum = INT_MAX

for i in range(n):
    diff_sum = 0
    for j in range(n):
        diff_sum += A[j] * abs(j - i)
    min_sum = min(min_sum, diff_sum)

print(min_sum)