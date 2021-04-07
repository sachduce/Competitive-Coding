from sys import stdin

if __name__ == "__main__":
    for i in range(int(input())):
        n,k = list(map(int, stdin.readline().split()))
        flavors = list(map(int, stdin.readline().split()))
        maxValue = 0
        flavDict = {}
        start = 0
        for fi in range(n):
            if(flavors[fi] in flavDict):
                flavDict[flavors[fi]] += 1
            else:
                flavDict[flavors[fi]] = 1

            if(len(flavDict) == k):
                for x in range(start, fi):
                    if(flavDict[flavors[x]] == 1):
                        del flavDict[flavors[x]]
                        start = x +1
                        break
                    else:
                        flavDict[flavors[x]] -= 1

            else:
                maxValue = max(maxValue, fi - start + 1)


        print(maxValue)










