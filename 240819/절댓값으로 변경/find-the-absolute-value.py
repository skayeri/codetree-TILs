n = int(input())
list_ = input().split()

def abs(List):
    n_list = []
    for i in List:
        if int(i) > 0:
            n_list.append(int(i))
        else:
            n_list.append(-int(i))
    print(*n_list)

abs(list_)