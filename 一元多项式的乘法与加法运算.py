l1 = list(map(eval, input().split()))
l2 = list(map(eval, input().split()))


def d_to_s(d): # 字典转为列表，排序，转为输出时字符串的格式返回。
    ls = list(d.items())
    ls.sort(reverse=True)
    s = ''
    for l in ls:
        if l[1]:
            s = s + ' ' + str(l[1]) + ' ' + str(l[0])
    if s:
        return s.lstrip()
    return '0 0'


def myadd2(l1, l2):
    d = {}
    for i in range(2, len(l1), 2):
        d[l1[i]] = l1[i - 1]
    for j in range(2, len(l2), 2):
        d[l2[j]] = d.get(l2[j], 0) + l2[j - 1]
    return d_to_s(d)


def mymultiply(l1, l2):
    d = {}
    for i in range(2, len(l1), 2):
        for j in range(2, len(l2), 2):
            d[l1[i] + l2[j]] = d.get(l1[i] + l2[j], 0) + l1[i - 1] * l2[j - 1]
    return d_to_s(d)


print(mymultiply(l1, l2))
print(myadd2(l1, l2))
