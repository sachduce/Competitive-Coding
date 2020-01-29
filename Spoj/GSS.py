from sys import stdin
from math import ceil, log2

def getMid(s, e):
    return s + (e-s)//2


def constructSTUtil(arr, ss, se, st, si):

    if (ss == se):
        st[si] = arr[ss];
        return arr[ss];

    mid = getMid(ss, se);

    left =constructSTUtil(arr, ss, mid, st, si * 2 + 1)
    right = constructSTUtil(arr, mid + 1, se, st, si * 2 + 2)
    if(left and right):
        st[si] = max(left, right, left+ right)
    elif(left):
        st[si] = left
    else:
        st[si] = right

    return st[si];


def constructST(arr, n):

    x = (int)(ceil(log2(n)));


    max_size = 2 * (int)(2 ** x) - 1;


    st = [None] * max_size;

    constructSTUtil(arr, 0, n - 1, st, 0);
    return st;


def getSumUtil(st, ss, se, qs, qe, si):

    if (qs <= ss and qe >= se):
        return st[si];

    if (se < qs or ss > qe):
        return None

    mid = getMid(ss, se);
    left = getSumUtil(st, ss, mid, qs, qe, 2 * si + 1)
    right = getSumUtil(st, mid + 1, se, qs, qe, 2 * si + 2);
    if(left and right):
        return max(left,right, left+right)
    elif(left):
        return left
    else:
        return right





def getSum(st, n, qs, qe):
    return getSumUtil(st, 0, n - 1, qs, qe, 0);

if __name__ == "__main__":
    n = int(input())
    arr  = list(map(int, stdin.readline().split()))
    st = constructST(arr, n)

    for i in range(int(input())):
        x, y = list(map(int, stdin.readline().split()))
        print(getSum(st,n, x-1, y-1))
