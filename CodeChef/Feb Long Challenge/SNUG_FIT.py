from sys import stdin

if __name__ == "__main__":
    for i in range(int(input())):
        n = int(input())
        a = sorted(list(map(int, stdin.readline().split())))
        b = sorted(list(map(int, stdin.readline().split())))
        counter  = 0
        for j in range(n):
            counter += min(a[j], b[j])

        print(counter)
