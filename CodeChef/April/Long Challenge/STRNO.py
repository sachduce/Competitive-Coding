from sys import stdin;
import math;

def primeFactors(n):
    pf = 0;
    while(n % 2 == 0):
        pf +=1;
        n = n / 2;

    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            pf += 1;
            n = n / i
    if(n >2):
        pf +=1;
    return pf;

if __name__ == "__main__":
    for i in range(int(input())):
        x,k = list(map(int, stdin.readline().split()));
        pf= primeFactors(x);
        if(pf >= x):
            print(1)
        else:
            print(0);