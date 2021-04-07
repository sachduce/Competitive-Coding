def modInverse(a, m) :
    a = a % m;
    for x in range(1, m) :
        if ((a * x) % m == 1) :
            return x
    return 1

if __name__ == "__main__":
    print( modInverse(866666673, 10**9 +7))