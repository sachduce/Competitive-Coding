from sys import stdin;
from bisect import bisect_left;
mod = 10**9 +7;
sysMax = 10**10 +1;
g= [0,1];
ans = [0, 1];
pre = [0, 1];
i = 2;

def add(a, b):
    global mod;
    return (a%mod + b%mod)%mod;

def mul(a,b):
    global mod;
    return (a%mod * b%mod)%mod;

while(True):
    g.append(1+g[i-g[g[i-1]]])
    pre.append(pre[i-1] + g[i]);
    ans.append(add(ans[i-1], mul(mul(i,i), g[i])));
    if(pre[i] > sysMax):
        break;
    i +=1;

if __name__ == "__main__":
    for _ in range(int(input())):
        l,r = list(map(int, stdin.readline().split()));
        sm1, sm2 = 0, 0

        if l == 1:
            sm1 = 0
        else:
            l -= 1
            tl = bisect_left(pre, l)
            sm1 = add(ans[tl - 1], mul(l - pre[tl - 1], mul(tl, tl)))
        tr = bisect_left(pre, r)
        sm2 = add(ans[tr - 1], mul(r - pre[tr - 1], mul(tr, tr)))
        print((sm2 - sm1) % mod)
