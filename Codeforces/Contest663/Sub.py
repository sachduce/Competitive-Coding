if __name__ == "__main__":
    for _ in range(int(input())):
        n = int(input());
        ans = [i for i in range(1, n+1)];
        print(*ans, sep=' ');