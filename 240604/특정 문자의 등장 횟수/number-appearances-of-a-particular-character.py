s = input()
a = 0
b = 0
idx = 0

while 'ee' in s[idx:]:
    idx = s.find('ee') + 1
    a += 1

idx = 0
while 'eb' in s[idx:]:
    idx = s.find('eb') + 1
    b += 1

print(a, b)