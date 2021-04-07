from sys import stdin
from math import ceil, log2
N=100005;
seg = [0] * (4*N)
lazy = [0] * (4*N)

def getMid(s, e):
    return s + (e -s)//2


def updateValue(low, high, lq, hq, node, val) :

    if(lazy[node]):
        seg[node]+=(high-low+1)*lazy[node];

        if(high!=low):
            lazy[2*node+1]+=lazy[node];
            lazy[2*node+2]+=lazy[node];

        lazy[node]=0;

    if(low>hq or high<lq):
        return;

    if(lq<=low and high<=hq):

        seg[node]+=(high-low+1)*val;
        if(high!=low):

            lazy[2*node+1]+=val;
            lazy[2*node+2]+=val;

        return

    mid= getMid(low, high)
    updateValue(low,mid,lq,hq,2*node+1,val);
    updateValue(mid+1,high,lq,hq,2*node+2,val);
    seg[node]=seg[2*node+1]+seg[2*node+2];



def updateValueUtil(st, ss, se, i, diff, si):

    if (i < ss or i > se):
        return;

    st[si] = st[si] + diff;

    if (se != ss):
        mid = getMid(ss, se);
        updateValueUtil(st, ss, mid, i,
                        diff, 2 * si + 1);
        updateValueUtil(st, mid + 1, se, i,
                        diff, 2 * si + 2);


def query(low, high, lq, hq, node):
    if (lazy[node]):
        seg[node] += (high - low + 1) * lazy[node];

        if (high != low):
            lazy[2 * node+1] += lazy[node];
            lazy[2 * node+2] += lazy[node];

        lazy[node]=0;

    if (low > hq or high < lq):
        return 0;

    if (lq <= low and high <= hq):
        return seg[node];

    mid= getMid(low, high)
    return query(low, mid, lq, hq, 2 * node + 1) + query(mid + 1, high, lq, hq, 2 * node + 2);




def getSumUtil(st, ss, se, qs, qe, si):

    if (qs <= ss and qe >= se):
        return st[si];

    if (se < qs or ss > qe):
        return 0;

    mid = getMid(ss, se);

    return getSumUtil(st, ss, mid, qs, qe, 2 * si + 1) + getSumUtil(st, mid + 1, se, qs, qe, 2 * si + 2);

if __name__ == "__main__":
    for i in range(int(input())):
        N,C = list(map(int, stdin.readline().split()))

        height = (int)(ceil(log2(N)));
        first = (2 ** height) -1
        max_size = 2 * (first +1) - 1


        for j in range(C):
            x = list(map(int, stdin.readline().split()))
            if(x[0] == 0):
                updateValue(0, N-1, x[1]-1, x[2] -1, 0, x[3])
            else:
                print(query(0,N-1,x[1]-1, x[2]-1, 0))



