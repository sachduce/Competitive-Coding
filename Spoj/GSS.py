from sys import stdin


def calculateMax(n, arr):
    dp = [0]*n
    for i in range(n):
        if(i==0):
            dp[i] = arr[i]
        elif(arr[i] < 0):
            if(arr[i] > dp[i-1]):
                dp[i] = arr[i]
            else:
                dp[i] = dp[i-1]
        else:
            if(dp[i-1] >0):
                dp[i]  = arr[i] +dp[i-1]
            else:
                dp[i] = arr[i]

    return dp

def process(start, end, dp, arr):
    if (dp[end] <= 0):
        return max(arr[start: end + 1])
    if (start == 0 or dp[start -1] <0):
        return dp[end]

    return dp[end] - dp[start - 1]




if __name__ == "__main__":
    n = int(input())
    arr  = list(map(int, stdin.readline().split()))
    source = calculateMax(n, arr)
    print("{}".format(source))
    q  = int(input())
    for i in range(q):
        x, y = list(map(int, stdin.readline().split()))
        if(x == y):
            print(arr[x-1])
        else:
            print(process(x-1, y-1, source, arr))
