from sys import stdin, stdout;


if __name__ == "__main__":
    t, s = list(map(int, stdin.readline().split()))
    for i in range(t):
        n = int(stdin.readline())

        A = sorted(list(map(int, stdin.readline().split())))
        B = sorted(list(map(int, stdin.readline().split())))

        flag = False
        for j in range(n):
            if(A[j] >= B[j] ):
                flag = True;
                break;

        if(not flag):
            dicA = {}
            dicB = {}

            for v in A:
                if v in dicA:
                    dicA[v] +=1
                else:
                    dicA[v] =1

            for v in B:
                if v in dicB:
                    dicB[v] +=1
                else:
                    dicB[v] =1

            for k in dicA:
                if(k!= A[0] and k not in dicB):
                    flag = True
                    break

        if(flag):
            print("NO")
        else:
            print("YES")
