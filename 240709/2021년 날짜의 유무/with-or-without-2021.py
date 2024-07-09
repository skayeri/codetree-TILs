m, d = map(int, input().split())

def is_exist(m, d):
    if m > 12 or d > 31:
        return False
    else:
        if m in [1, 3, 5, 7, 8, 10, 12]:
            if d <= 31:
                return True
        elif m == 2:
            if d <= 28:
                return True
        elif m in [4, 6, 9, 11]:
            if d <= 30:
                return True
        else:
            return False

if is_exist(m, d):
    print("Yes")
else:
    print("No")