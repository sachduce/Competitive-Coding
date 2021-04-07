from sys import stdin;
if __name__ == "__main__":
    for _ in range(int(input())):
        n = int(input());
        stringDict = {};
        for i in range(n):
            s = stdin.readline().rstrip();
            for c in s:
                if c in stringDict:
                    stringDict[c] += 1;
                else:
                    stringDict[c] = 1;

        ans = 'YES';
        for c in stringDict:
            if stringDict[c]%n != 0:
                ans = 'NO';
                break;
        print(ans)
