from sys import stdin

if __name__ == "__main__":
    for i in range(int(input())):
        n = int(input())
        men = sorted(list(map(int, stdin.readline().split())))
        women = sorted(list(map(int, stdin.readline().split())))
        sum = 0
        for j in range(n):
            sum += men[j]* women[j]
        print(sum)