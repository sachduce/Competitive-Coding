from sys import stdin;

def calculateComb(coins, amount):
    dp = [0]*(amount +1);
    dp[0] =1;
    for coin in coins:
        for j in range(coin, amount+1):
            dp[j] += dp[j- coin];
        print(dp);
    return dp[amount];

if __name__ == "__main__":
    for _ in range(int(input())):
        m = int(input());
        coins = list(map(int, stdin.readline().split()));
        n = int(input());
        ans = calculateComb(coins, n);
        print(ans);