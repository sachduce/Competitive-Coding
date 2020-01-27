from sys import stdin

hash ={
    0 : [0,0 , 0, 0],
    1 : [1,1,1,1],
    2: [2,4,8,6],
    3 : [3,9,7,1],
    4: [4,6,4,6],
    5: [5,5,5,5],
    6: [6,6,6,6],
    7: [7, 9,3,1],
    8 : [8,4,2,6],
    9: [9, 1,9,1]
}

if __name__ == "__main__":
        for i in range(int(input())):
            a,b = stdin.readline().split()

            a = int(a[-1])
            b = int(b)
            if(b ==0):
                print(1)
            else:
                print(hash[a][(b -1)%4 ])
