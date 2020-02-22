n = int(input())
cnt = 0


def my(n):
    global cnt
    if n == 1:
        return cnt
    cnt += 1
    if n % 2:
        return my((3 * n + 1) / 2)
    return my(n / 2)


print(my(n))
