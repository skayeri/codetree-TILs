n = int(input())
arr = list(map(int, input().split()))
    
group = [] 
for i, a in enumerate(arr):
    group.append((i, a))

group.sort(key=lambda x: x[1])

num_to_rank = [0] * n

for rank, (idx, num) in enumerate(group, start=1):
    num_to_rank[idx] = rank

print(*num_to_rank)