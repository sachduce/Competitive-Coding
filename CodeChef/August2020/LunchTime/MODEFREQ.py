from sys import stdin;
if __name__ == "__main__":
    for _ in range(int(input())):
        n = int(input());
        A = list(map(int, stdin.readline().split()));
        Adict = {};
        for a in A:
            if a in Adict:
                Adict[a] += 1;
            else:
                Adict[a] = 1;
        fDict = {};
        maxf = 0;
        ans = 0;
        for key in Adict:
            if Adict[key] in fDict:
                fDict[Adict[key]] += 1;
            else:
                fDict[Adict[key]] = 1;
            if(maxf < fDict[Adict[key]] or (maxf == fDict[Adict[key]] and Adict[key] < ans )):
                ans = Adict[key];
                maxf = fDict[Adict[key]]
        print(ans);

