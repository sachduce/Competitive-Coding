from sys import stdin;
if __name__ == "__main__":
    for _ in range(int(input())):
        s = stdin.readline().rstrip();
        p = stdin.readline().rstrip();
        stringDict = {};
        for v in s:
            if v in stringDict:
                stringDict[v] += 1;
            else:
                stringDict[v] = 1;

        for v in p:
            stringDict[v] -= 1;

        if p in stringDict:
            stringDict[p] += 1;
        else:
            stringDict[p] = 1;
        ans = '';
        sortedKeys = sorted(stringDict.keys());
        for s in sortedKeys:
            ans += s*stringDict[s];
        print(ans);