fruits =  ["apple", "banana", "grape", "blueberry", "orange"]

word = input()
cnt = 0

for fruit in fruits:
    if word in fruit[2:4]:
        print(fruit)
        cnt += 1
print(cnt)