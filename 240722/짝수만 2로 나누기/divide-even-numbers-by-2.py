n = int(input())
list_ = input().split()
list_ = [int(i) for i in list_]

def div():
    for i in range(n):
        if list_[i] % 2 == 0:
            list_[i] //= 2
            
div()
print(*list_)