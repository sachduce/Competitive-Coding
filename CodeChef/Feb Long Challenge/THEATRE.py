from sys import stdin
hashM ={
    'A' : 0,
    'B' :1,
    'C' : 2,
    'D' :3
}
hashT = {
    '12' : 0,
    '3' : 1,
    '6' : 2,
    '9' : 3,
}

if __name__ == "__main__":
    sumCounter = 0
    for i in range(int(input())):
        n = int(input())
        arr = [[0 for x in range(4)] for y in range(4)]
        counter = -10**9

        for j in range(n):
            m, t =  stdin.readline().split()
            arr[hashM[m]][hashT[t]] += 1

        for a in range(4):
            for b in range(4):
                if(b != a):
                    for c in range(4):
                        if(c != b and c!= a):
                            for d in range(4):
                                if(d!= a and d!=b and d!=c):

                                    x = sorted([arr[a][0] , arr[b][1], arr[c][2], arr[d][3]], reverse=True)

                                    mul = 100
                                    temp = 0
                                    for v in x:
                                        if(v > 0):
                                            temp += mul*v
                                            mul -= 25

                                        else:
                                            temp -= 100

                                    counter = max(counter, temp)



        sumCounter += counter
        print(counter)
    print(sumCounter)