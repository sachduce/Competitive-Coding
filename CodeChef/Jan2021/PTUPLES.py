def SieveOfEratosthenes(n):
    lastP, count = 3, 0;
    prime = [True for i in range(n + 1)]
    p = 2
    while (p * p <= n):
        if (prime[p] == True):
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1

    for p in range(5, n + 1):
        if prime[p]:
            if(p - lastP == 2):
                count += 1
            lastP = p;
    return count;


if __name__ == '__main__':
    t = int(input());
    for _ in range(t):
        n = int(input());
        v = SieveOfEratosthenes(n);
        print(v);


            