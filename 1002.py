d = {
    '0': 'ling',
    '1': 'yi',
    '2': 'er',
    '3': 'san',
    '4': 'si',
    '5': 'wu',
    '6': 'liu',
    '7': 'qi',
    '8': 'ba',
    '9': 'jiu',
}
n = input()


def printTheNumber(n):
    sumn = 0
    for i in n:
        sumn += int(i)
    s = ''
    for i in str(sumn):
        s += d[i] + ' '
    return s.rstrip()


print(printTheNumber(n))
