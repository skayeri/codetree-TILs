word = input()

encoded = ''

curr_char = word[0]
num_char = 1
for target in word[1:]:
    if target == curr_char:
        num_char += 1
    else:
        encoded += curr_char
        encoded += str(num_char)
        curr_char = target
        num_char = 1

encoded += curr_char
encoded += str(num_char)

print(len(encoded))
print(encoded)