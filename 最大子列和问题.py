n = int(input())
l = list(map(eval, input().split()))


def maxl(l, suml=0):
    maxsum = 0
    for i in l:
        suml += i
        if suml < 0:
            suml = 0
        if suml > maxsum:
            maxsum = suml
    return maxsum


print(maxl(l))
