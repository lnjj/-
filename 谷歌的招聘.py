def isodd(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
            break
    return True


L, K = input().split()
L = int(L)
K = int(K)
N = input()


def findOdd(L, K, N):
    if K > L:
        return '404'
    for i in range(L - K + 1):
        if isodd(int(N[i:i + K])):
            return N[i:i + K]
    return '404'


print(findOdd(L, K, N))
