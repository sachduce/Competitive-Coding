from sys import stdin

if __name__ == "__main__":
    for i in range(int(input())):
        s = stdin.readline().rstrip()
        length = len(s)
        if(len(s) >=4):
            lastF = s[-4:]
            if(lastF == '1000'):
                print("YES")
            else:
                print("NO")

        else:
            print("NO")







