from sys import stdin

if __name__ == "__main__":
    for i in range(int(input())):
        n,k = list(map(int, stdin.readline().split()))
        coins = stdin.readline().split()
        switch = 0
        heads =0
        for x in range(k):
            if(coins[n-1-x]=='H' and switch%2 ==0):
                switch += 1
            if(coins[n-1-x]=='T' and switch%2 ==1 ):
                switch +=1

        f = switch%2
        for j in range(n-k):
            if((coins[j] == 'H' and f ==0) or (coins[j] == 'T' and f ==1)):
                heads += 1

        print(heads)




