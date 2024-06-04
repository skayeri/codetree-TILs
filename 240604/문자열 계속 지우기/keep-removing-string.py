A = input()
B = input()

while A.find(B) != -1:
    i = A.find(B)
    A = A[:i] + A[i+len(B):]

print(A)