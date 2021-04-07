dp = [0]*101;
dp[0] =1;
dp[1] = 1;
lastComputed = [1];

def catalan(n, ):
    if(dp[n]):
        return dp[n];
    for i in range(lastComputed[0] +1 , n+1):
        for j in range(i):
            dp[i] += dp[i-j-1]* dp[j];

    lastComputed[0] = max(lastComputed[0], n);
    return dp[n];


if __name__ == "__main__":
    for i in range(int(input())):
        n = int(input());
        print(catalan(n));
