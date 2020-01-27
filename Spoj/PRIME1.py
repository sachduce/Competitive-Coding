from sys import stdin
import math

commposites = {}

if __name__ == "__main__":

    for i in range(int(input())):
        m, n = list(map(int, stdin.readline().split()))
        for k in range(2, int(math.sqrt(n)) +1):
            start = max(2*k, ((m +k-1)//k) *k )
            for l in range(start, n+1, k):
                commposites[l] = 1

        for x in range(m, n+1):
            if(x not in commposites and x!=1):
                print(x)

        print("")