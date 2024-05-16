A = [
    list(map(int, input().split()))
    for _ in range(3)
]
z = input()
B = [
    list(map(int, input().split()))
    for _ in range(3)
]

for i in range(3):
    for j in range(3):
        print(A[i][j]*B[i][j], end=' ')
    print()