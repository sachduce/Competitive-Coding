from sys import stdin

MAXM = 10**9 +7

fact = [1]* (10**5 +1)

for i in range(2,10**5 +1 ):
    fact[i] = i* fact[i-1] % MAXM



if __name__ == "__main__":

    for i in range(int(input())):
        n, m = list(map(int, stdin.readline().split()))
        maxCom = pow(m, n, MAXM)
        limit = min(n,m)
        subtract = 0
        for j in range(3, limit+1):
            x = 1
            x = (x* m) %MAXM
            temp = m-1
            for k in range(1,limit-j):
                x = (x* temp) %MAXM
                if(x %2 ==0):
                    temp -= 1

            x =  (fact[n-j +1]*x) %MAXM
            subtract += x
        ans = (maxCom -subtract +MAXM)%MAXM

        print(ans)

