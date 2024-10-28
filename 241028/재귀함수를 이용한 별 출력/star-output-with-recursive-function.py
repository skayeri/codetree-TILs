def print_ast(n):
    if n == 0:
        return

    print_ast(n-1)
    print("*" * n)

n = int(input())

print_ast(n)