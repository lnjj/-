def BuildTree(L=None):
    if not L:
        L = []
    n = int(input())
    if n > 0:
        check = [0 for i in range(n)]
        for i in range(n):
            l = input().split()  # element,left,right
            if l[1] != '-':
                l[1] = int(l[1])
                check[int(l[1])] = 1
            else:
                l[1] = -1
            if l[2] != '-':
                l[2] = int(l[2])
                check[int(l[2])] = 1
            else:
                l[2] = -1
            L.append(l)
        for i in range(n):
            if not check[i]:
                break
    else:
        i = -1  # empty
    return i, L


def isomorphic(tree1, tree2):
    head1, head2 = tree1[0], tree2[0]
    if tree1[0] == -1 and tree2[0] == -1:  #empty
        return True
    if tree1[0] == -1 and tree2[0] != -1:  #only one empty
        return False
    if tree1[0] != -1 and tree2[0] == -1:  #only one empty
        return False
    lefthead1, righthead1 = tree1[1][head1][1], tree1[1][head1][2]
    lefthead2, righthead2 = tree2[1][head2][1], tree2[1][head2][2]
    if tree1[1][head1][0] != tree2[1][head2][0]:
        #first element not equal
        return False
    if lefthead1 == -1 and lefthead2 == -1:
        #both left empty,compare right
        return isomorphic((righthead1, tree1[1]), (righthead2, tree2[1]))
    if (lefthead1 != -1 and lefthead2 != -1) and (
            tree1[1][lefthead1][0] == tree2[1][lefthead2][0]):
        #both left not empty and left element equals
        return isomorphic((righthead1, tree1[1]),
                          (righthead2, tree2[1])) and isomorphic(
                              (lefthead1, tree1[1]), (lefthead2, tree2[1]))
    else:  #swap left and right
        return isomorphic((lefthead1, tree1[1]),
                          (righthead2, tree2[1])) and isomorphic(
                              (righthead1, tree1[1]), (lefthead2, tree2[1]))


tree1 = BuildTree()
tree2 = BuildTree()
if isomorphic(tree1, tree2):
    print('Yes')
else:
    print('No')
