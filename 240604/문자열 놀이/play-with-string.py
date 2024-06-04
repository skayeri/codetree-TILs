s, q = input().split()
q = int(q)
q_list = []
s_list = list(s)

for _ in range(q):
    q_list.append(input().split())

for i in q_list:
    if i[0] == '1':
        t1 = s_list[int(i[1]) - 1]
        t2 = s_list[int(i[2]) - 1]
        s_list[int(i[1]) - 1] = t2
        s_list[int(i[2]) - 1] = t1
        print(''.join(s_list))
    else:
        for idx, j in enumerate(s_list):
            if j == i[1]:
                s_list[idx] = i[2]
        print(''.join(s_list))