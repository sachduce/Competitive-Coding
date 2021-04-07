dp = [0]* 10**4;
dp[1] = 1;
lastComputed = [1];
ic = [1, 1,  1];
next = [2, 3 ,5];


def getNthUglyNumber(n, next, ic, lastComputed):
    if(dp[n]):
        return dp[n];
    for i in range(lastComputed[0]+1, n+1):
        dp[i] = min(next);
        if(dp[i] == next[0]):
            ic[0] += 1;
            next[0] = dp[ic[0]] * 2;
        if(dp[i] == next[1]):
            ic[1] += 1;
            next[1] = dp[ic[1]] * 3;
        if (dp[i] == next[2]):
            ic[2] += 1;
            next[2] = dp[ic[2]] * 5;
    lastComputed[0] =  max(lastComputed[0], n);
    return  dp[n];



if __name__ == "__main__":
    for i in range(int(input())):
        n = int(input());
        print(getNthUglyNumber(n, next, ic, lastComputed));


