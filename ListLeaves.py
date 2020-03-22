import queue


def BuildTree(L=None):
    if not L:
        L = []
    n = int(input())
    if n > 0:
        check = [0 for i in range(n)]
        for i in range(n):
            d = {}
            l = input().split()  # element,left,right
            if l[0] != '-':
                d['left'] = int(l[0])
                check[int(l[0])] = 1
            else:
                d['left'] = -1
            if l[1] != '-':
                d['right'] = int(l[1])
                check[int(l[1])] = 1
            else:
                d['right'] = -1
            L.append(d)
        for i in range(n):
            if not check[i]:
                break
    else:
        i = -1  # empty
    return i, L


firstprint = True


def PrintLeaves(head, tree):
    global firstprint
    q = queue.Queue()
    q.put(head)
    while not q.empty():
        num = q.get()
        if tree[num]['right'] == -1 and tree[num]['left'] == -1:
            if firstprint:
                print(num, end='')
                firstprint = False
            else:
                print(' {:d}'.format(num), end='')
        if tree[num]['left'] != -1:
            q.put(tree[num]['left'])
        if tree[num]['right'] != -1:
            q.put(tree[num]['right'])


head, tree = BuildTree()
PrintLeaves(head, tree)
