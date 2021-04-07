from sys import stdin


def coinChange(coins, amount, dp):
    for coin in coins:
        for x in range(coin, amount + 1):
            if(not dp[x]):
                dp[x] =  dp[x - coin]

    return dp[amount]

def findCoinChange(coins, amount, dp,  n, ans, p, max_amount):
    i = n - 1

    while (i >= 0):
        while (amount >= coins[i] and dp[amount - coins[i]]):
            if(max_amount - coins[i] >=p):
                return False
            amount -= coins[i]
            if(coins[i] in ans):
                ans[coins[i]] += 1
            else:
                ans[coins[i]] =1
        i -= 1
    return True


if __name__ == "__main__":
    for i in range(int(input())):
        n, p = list(map(int, stdin.readline().split()))
        d = list(map(int, stdin.readline().split()))

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
        else:
            max_amount = p + d[-1] -1
            dp = [False] * (p + 1)
            dp[0] = True

            cc = coinChange(d, p, dp)
            print("dp : {}".format(dp))
            amount = p+1

            ans = {}
            while(amount <= max_amount):
                flag = False

                for coin in d:
                    ans = {}
                    if(amount - coin < p and amount-coin >=0 and dp[amount -coin]):
                        ans[coin] = 1
                        flag = findCoinChange(d, amount-coin, dp, n, ans, p, amount)

                    if(flag):
                        break
                if(flag):
                    break
                amount += 1

            print("YES", end= ' ')
            for i in range(n):
                if d[i] in ans:
                    print(ans[d[i]], end = ' ')
                else:
                    print(0, end= ' ')

            print('')