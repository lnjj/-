def fun(l1, l2):
    if len(l2) != len(l1):
        return False
    if len(l1) <= 1 and l1 == l2:
        return True
    if len(l1) <= 1 and l1 != l2:
        return False
    if l1[0] != l2[0]:
        return False
    head1, head2 = l1[0], l2[0]
    big1 = []
    big2 = []
    small1 = []
    small2 = []

    for i in l1[1:]:
        big1.append(i) if i > head1 else small1.append(i)
    for i in l2[1:]:
        big2.append(i) if i > head2 else small2.append(i)

    return fun(big1, big2) and fun(small1, small2)


Lprint = []
while True:
    s = input()
    if s == '0':
        break
    N, line = map(int, s.split())
    l0 = list(map(int, input().split()))
    L = []
    for i in range(line):
        L.append(list(map(int, input().split())))
    for l in L:
        Lprint.append("Yes") if fun(l, l0) else Lprint.append("No")
for l in Lprint:
    print(l)
