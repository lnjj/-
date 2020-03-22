'''先创建数，再遍历，后序打印'''


def CreatTree():
    '''给出了前序和中序，。以后每次'''
    n = int(input())
    stack = []
    L = [{'left': 0, 'right': 0} for i in range(n + 1)]  # 树存在从下标1开始之后的位置
    root = False
    for i in range(n * 2):
        l = input().split()
        if len(l) == 2:
            if not root:  # 第一个入栈的是根节点
                root = True
                rootindex = int(l[1])
            elif not L[index]['left']:  # 每次入栈时保存树信息
                L[index]['left'] = int(l[1])
            elif not L[index]['right']:
                L[index]['right'] = int(l[1])
            index = int(l[1])  # 作为下次保存树信息L的下标

            stack.append(int(l[1]))
        else:
            index = stack.pop()  #出栈时只要记住下次保存树信息时L的下标
    return L, rootindex


def PrintTree(tree, n=1):
    global firstprintflag
    if not n:
        return
    PrintTree(tree, tree[n]['left'])
    PrintTree(tree, tree[n]['right'])
    if firstprintflag:
        print(n, end='')
        firstprintflag = False
    else:
        print('', n, end='')


tree, root = CreatTree()
firstprintflag = True
PrintTree(tree, root)
