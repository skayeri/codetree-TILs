a, b, c = input().split()
a, c = int(a), int(c)

def four_arth(a, b, c):
    if b == '+':
        print(a, b, c, '=', a + c)
    elif b == '-':
        print(a, b, c, '=', a - c)
    elif b == '*':
        print(a, b, c, '=', a * c)
    elif b == '/':
        print(a, b, c, '=', a // c)
    else:
        print(False)

four_arth(a, b, c)