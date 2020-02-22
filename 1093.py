a = input()
b = input()
s = ''
for i in a + b:
    if i not in s:
        s += i
print(s)
