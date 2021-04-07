from sys import stdin

if __name__ == "__main__":
    while(True):
        profit = list(map(int, stdin.readline().split()))
        start = 0
        curr = 0
        for v in profit:
            curr = curr + v
            expSum = start + curr

            if(expSum <= 0 ):
                start += -expSum +1

        print(start)