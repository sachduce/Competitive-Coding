from math import log2, floor
from sys import stdin;

def subsequence(s, binary):
    maxVal = 0;
    maxkey = 0;
    subDict = {};

    while (binary > 0):
        pos = floor(log2(binary & -binary) + 1);
        sVal = s[pos - 1];
        if(sVal in subDict):
            subDict[sVal] += 1;
        else:
            subDict[sVal] = 1;

        if(subDict[sVal] > maxVal or (subDict[sVal] == maxVal and sVal < maxkey) ):
            maxVal = subDict[sVal];
            maxkey = sVal;
        binary = (binary & ~(1 << (pos - 1)))

    return int(maxkey)


def possibleSubsequences(s, n):

    limit = 2 ** n
    ans = [0]*n;
    for i in range(1, limit):
        sub = subsequence(s, i)
        ans[sub-1] += 1;
    return ans

if __name__ == "__main__":
    for _ in range(int(input())):
        n = int(input());
        str = stdin.readline().split();
        val = possibleSubsequences(str, n);
        print(*val, sep=' ');


