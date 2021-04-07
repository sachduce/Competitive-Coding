from sys import stdin;
from copy import deepcopy;
if __name__ == "__main__":
    for _ in range(int(input())):
        s = list(stdin.readline().rstrip());
        p = list(stdin.readline().rstrip());
        for j in p:
            s.remove(j);
        s.sort();
        copys = deepcopy(s);
        copys.append(p[0]);
        copys = sorted(copys, reverse= True);
        ans = ''.join(s[0: len(copys) - copys.index(p[0]) -1]) + ''.join(p) + ''.join(s[len(copys) - copys.index(p[0])-1:]);
        if(p[0] in s):
            compare = ''.join(s[0: s.index(p[0])]) + ''.join(p) + ''.join(s[s.index(p[0]):]);
            ans = min(ans, compare);
        print(ans);
