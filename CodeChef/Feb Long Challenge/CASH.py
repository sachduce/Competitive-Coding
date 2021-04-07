from sys import stdin

if __name__ == "__main__":
    for i in range(int(input())):
        n, k = list(map(int, stdin.readline().split()))
        a = list(map(int, stdin.readline().split()))
        counter  = 0
        for val in a:
            counter += val%k

        print(counter%k)
