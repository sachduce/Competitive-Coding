import math
from functools import reduce
from collections import defaultdict
def pr():
    l=[2]
    for i in range(2,100):
        flag=True
        for j in range(2,math.ceil(math.sqrt(i))+1):
            if(i%j==0):
                flag=False
                break
        if(flag):
            l.append(i)
    return l
def dfsutil(d,visited,value,p,curr,l):
    visited[curr-1]=True
    l.append(curr)
    value[curr-1]=(value[p-1]+1)%4 if(p!=-1) else 0
    for i in d[curr]:
        if not visited[i-1]:
            dfsutil(d,visited,value,curr,i,l)
            # l.append(None)
def main():
    for _ in range(int(input())):
        r=pr()

        a=reduce(lambda x,y: x*y,r[:len(r)//2])
        b=reduce(lambda x,y: x*y,r[len(r)//2:2*len(r)//3])
        c=reduce(lambda x,y: x*y,r[2*len(r)//3:])

        n=int(input())
        d=defaultdict(list)
        for i in range(n-1):
            u,v=list(map(int,input().split()))
            d[u].append(v)
            d[v].append(u)
        visited=[False]*n
        value=[-1]*n
        l=[]
        dfsutil(d,visited,value,-1,1,l)
        w=[a,b,c]
        for i in range(n):
            if(value[i]%2==0):
                value[i]=w[0]
            elif(value[i]==1):
                value[i]=w[1]
            else:
                value[i]=w[2]
        print(*value)
main()