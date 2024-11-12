# a, b의 최소공배수 : a * b / (a, b의 최대공약수)

n = int(input())
arr = list(map(int, input().split()))

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def lcm(a, b):
    return a * b // gcd(a, b)

def sol(arr, n):
    if len(arr) == 1:
        return arr[0]
    return lcm(arr[n-1], sol(arr[:n-1], n - 1))

print(sol(arr, n))