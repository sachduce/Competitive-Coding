from sys import stdin

if __name__ == "__main__":
    for i in range(int(input())):
        n = int(input());
        line = list(map(int, stdin.readline().split()))
        last = -1;
        flag = False
        for j in range(n):
            if line[j] == 1:
                if last != -1:
                    if(j - last <= 5):
                        flag = True;
                        break;

                last =j;

        if(flag):
            print("NO");
        else:
            print("YES");



