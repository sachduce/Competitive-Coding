from sys import stdin;

dp = {
        0 : 0,
        1: 1,
        2: 2,
        3: 3,
        4: 4,
        5: 5,
        6 : 6,
        7: 7,
        8: 8,
        9: 9,
        10: 10,
        11 : 11
    }

def solve(n):
    if(n in dp):
        return dp[n]

    dp[n] = solve(n//2) +solve(n//3) + solve(n//4)
    return dp[n]

if __name__ =="__main__":

    while(True):
        try:
            n = int(stdin.readline())
            if (n < 0):
                break;
            print(solve(n))
        except:
            break