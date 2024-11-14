a, b = tuple(map(int, input().split()))
numbers = list(map(int, input().split()))
numbers.sort()

print(numbers[b-1])