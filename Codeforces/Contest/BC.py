from sys import stdin;

if __name__ == "__main__":
    for _ in range(int(input())):
        n = int(input());
        weightMap = {};
        weights = list(map(int, stdin.readline().split()));
        for w in weights:
            if w in weightMap:
                weightMap[w] += 1;
            else:
                weightMap[w] = 1;
        possiblePair = {};
        keys = list(weightMap.keys());
        ans = 0;
        for i in range(len(keys)):
            p = keys[i];
            if(weightMap[keys[i]] > 0):
                if 2*p in possiblePair:
                    possiblePair[2*p] += weightMap[keys[i]]//2;
                else:
                    possiblePair[2*p] = weightMap[keys[i]]//2;
                ans = max(possiblePair[2*p], ans);
            for j in range(i+1, len(keys)):
                p = keys[i] + keys[j]
                add = min(weightMap[keys[i]],weightMap[keys[j]])
                if p in possiblePair:
                    possiblePair[p] += add;
                else:
                    possiblePair[p] = add;
                ans = max(ans, possiblePair[p]);
        print(ans);





