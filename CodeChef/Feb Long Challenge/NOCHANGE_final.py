from sys import stdin

if __name__ == "__main__":
    for i in range(int(input())):
        n, p = list(map(int, stdin.readline().split()))
        d = list(map(int, stdin.readline().split()))

        ans = [0]*n
        isNotFactors = -1
        isNotDivP = -1
        for i in range(n):
            if(p % d[i] != 0):
                isNotDivP = i
                break

            if(i < n-1 and d[i+1] % d[i] != 0):
                isNotFactors = i

        if(isNotFactors == -1 and isNotDivP == -1):
            print("NO")
        elif(isNotDivP > -1):
            x = p // (d[isNotDivP]) +1
            ans[isNotDivP] = x
            ansStr = ' '.join(map(str, ans))
            print("YES {}".format(ansStr))
        elif(isNotFactors > -1):
            x = d[isNotFactors+1] // d[isNotFactors] +1
            ans[isNotFactors] = x
            ans[isNotFactors +1] = p//d[isNotFactors+1] -1
            ansStr = ' '.join(map(str, ans))
            print("YES {}".format(ansStr))