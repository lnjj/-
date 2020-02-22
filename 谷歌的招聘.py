def isPrime(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def findOdd(L, K, N):
    if K > L:
        return '404'
    for i in range(L - K + 1):
        if isPrime(int(N[i:i + K])):
            return N[i:i + K]
    return '404'


L, K = input().split()
L = int(L)
K = int(K)
N = input()


print(findOdd(L, K, N))
