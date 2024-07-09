y = int(input())

def is_yun(x):
    if x % 4 == 0:
        return 'true'
    if x % 100 == 0 and x % 400 != 0:
        return 'false'

print(is_yun(y))