from sys import stdin

if __name__ == "__main__":
    for i in range(int(input())):
        n= int(stdin.readline())
        s = stdin.readline()
        a = 0
        b = 0
        remA = n
        remB= n
        ans = 2*n

        for i in range(2*n):
            if(i %2 == 0):
                if(s[i] == '1'):
                    a += 1
                remA -= 1


            else:
                if (s[i] == '1'):
                    b += 1
                remB -=1

            if (remB < a - b or remA < b - a):
                ans = i + 1
                break

        print(ans)

