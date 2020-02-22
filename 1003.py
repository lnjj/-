def judge(s):
    a = b = c = p = t = 0
    for ch in s:
        if ch not in 'APT':
            return 'NO'
    for ch in s:
        if ch == 'A':
            if p == 0:
                a += 1
            elif p == 1 and t == 0:
                b += 1
            elif p == 1 and t == 1:
                c += 1
        elif ch == 'P':
            p += 1
        elif ch == 'T':
            t += 1

    if a * b == c and b > 0 and p == 1 and t == 1:
        return 'YES'
    else:
        return 'NO'


n = int(input())
L = []
for i in range(n):
    L.append(input())
for s in L:
    print(judge(s))
