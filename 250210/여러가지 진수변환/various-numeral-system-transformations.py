N, B = map(int, input().split())

# Write your code here!

nums = []

while True:
    if N < B:
        nums.append(N)
        break
        
    nums.append(N % B)
    N //= B

for n in nums[::-1]:
    print(n, end='')