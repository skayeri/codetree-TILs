n = int(input())

def print_chr(n):
    if n == 0:
        return
    print_chr(n-1)
    print("HelloWorld")

print_chr(n)