def number_asc(n):
    if n == 0:
        return

    number_asc(n-1)
    if n == m:
       print(n)
    else:
        print(n, end=" ")

def number_desc(n):
    if n == 0:
        return
 
    print(n, end=" ")
    number_desc(n-1)
    
m = int(input())

number_asc(m)
number_desc(m)