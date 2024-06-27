def Cal(x):
    sum_val = 0
    for i in range(1, x + 1):
        sum_val += i
    return sum_val // 10

n = int(input())
print(Cal(n))