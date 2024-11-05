n = int(input())

def number(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return number(n // 3) + number(n - 1)

print(number(n))