n = int(input())
l = list(map(eval, input().split()))


def maxl(l, suml=0):
    maxsum = 0
    flag = 1
    havebeginflag = False
    for i in l:
        if i >= 0:
            havebeginflag = True
        if flag:
            begin_pre = i
            flag = 0
        suml += i
        if suml < 0:
            suml = 0
            flag = 1
        elif suml > maxsum:
            maxsum = suml
            begin = begin_pre
            end = i
        elif suml == 0 and maxsum == 0 and i == 0:
            maxsum = suml
            begin = begin_pre
            end = i
    if not havebeginflag:
        maxsum = 0
        begin = l[0]
        end = l[-1]
    return maxsum, begin, end


maxsum, beginnum, endnum = maxl(l)
print('%d %d %d' % (maxsum, beginnum, endnum))
