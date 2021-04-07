from sys import stdin;
N = 10**3 +1;
R = 10**3 +1;
modulo = 10**9 + 7;
dp = [[0 for i in range(R)] for j in range(N)];

def coefficient(n, r, dp):
    if(dp[n][r]):
        return dp[n][r];
    if(n == r or r == 0):
        dp[n][r] = 1;
        return dp[n][r];

    dp[n][r] = (coefficient(n-1, r-1, dp)% modulo+ coefficient(n-1, r, dp)% modulo)
    return dp[n][r]% modulo;

if __name__ == "__main__":
    for i in range(int(input())):
        n, r = list(map(int, stdin.readline().split()));
        if(n< r):
            print(0);
        else:
            print(coefficient(n,r , dp));
