def number_asc(n):
    if n == 0:
        return

    number_asc(n-1)
    print(n, end=" ")

def number_desc(n):
    if n == 0:
        return

    print(n, end=" ")
    number_desc(n-1)
    
n = int(input())

number_asc(n)
print()
number_desc(n)