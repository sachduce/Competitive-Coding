from sys import stdin;
from collections import Counter;

def solve():
    n, k = list(map(int, stdin.readline().split()));
    l = list(map(int, stdin.readline().split()));
    i = 0;
    ans1 = float('inf');
    while(i < n):
        x, y = 0, 0
        dl = Counter(l[:i]);
        dr = Counter(l[i:]);
        for j in dl:
            if dl[j] > 1:
                x += dl[j]
        for j in dr:
            if dr[j] > 1:
                y += dr[j];
        if(i == 0):
            c = k + y;
        elif(i == n):
            c = k + x;
        else:
            c = 2*k +x + y;
        ans1 = min(ans1, c);
        i += 1;
    a = set();
    p = 1;
    for i in l:
        if i in a:
            a = {i};
            p += 1;
        else:
            a.add(i);
    ans2 = p * k

    ans = min(ans1, ans2)
    print(ans)

if __name__ == "__main__":
    for _ in range(int(input())):
        solve()
