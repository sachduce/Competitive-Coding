from sys import stdin;
if __name__ == "__main__":
    for _ in range(int(input())):
        n = int(input());
        A = list(map(int, stdin.readline().split()));
        length = len(A);
        check = set();
        flag = True
        for i in range(length):
            for j in range(length -i):
                val = 0;
                for k in range(j, j+i+1):
                    val = val | A[k];

                if val in check:
                    flag = False;
                    break;
                else:
                    check.add(val);
            if (not flag):
                break

        if(flag):
            print("YES")
        else:
            print("NO")