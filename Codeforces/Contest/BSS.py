from sys import stdin;

if __name__ == "__main__":
    for _ in range(int(input())):
        n = int(input());
        group = {};
        ans = [-1]*n;
        start = 1
        bs = stdin.readline();
        group[start] = None;
        for i in range(n):
            start = len(group);
            while (start >= 1 and group[start] == bs[i]):
                start -= 1;
            if(start == 0):
                start = len(group) + 1;
            group[start] = bs[i];
            ans[i] = start;

        print(len(group));
        print(*ans, sep=" ");












