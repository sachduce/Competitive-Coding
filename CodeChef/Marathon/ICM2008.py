from sys import stdin

if __name__ == "__main__":
    for i in range(int(input())):
        a, b, c,d = list(map(int, stdin.readline().split()))

        x = abs(a-b)
        y = abs(c-d)

        if(x==0 and y ==0):
            print("YES")
        elif(y!=0 and x% y == 0):
            print("YES")
        else:
            print("NO")





