from sys import stdin

if __name__ == "__main__":
    for i in range(int(input())):
        n = int(input());
        s = stdin.readline();
        xMove = False;
        yMove = False;
        x = 0;
        y = 0;
        for v in s:
            if v == 'L':
                if not xMove:
                    x -= 1
                xMove = True
                yMove = False
            elif v == 'R':
                if not xMove:
                    x += 1
                xMove = True
                yMove = False
            elif v == 'U':
                if not yMove:
                    y += 1
                xMove = False;
                yMove = True;
            elif v == 'D':
                if not yMove:
                    y -= 1
                xMove = False;
                yMove = True;

        print("{} {}".format(x, y))