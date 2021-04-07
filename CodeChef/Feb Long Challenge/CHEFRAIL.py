from sys import stdin
from collections import defaultdict

import math

def calculate(xVal, dic1, dic2 ):
    count = 0
    if(xVal in dic1 ):
        count +=1
    if(-xVal in dic2):
        count +=1
    return count

def add_edge(fKey, addDic, searchSet):


    for key in searchSet:
        temp = math.sqrt(key * fKey)
        if(temp.is_integer()):
            if(fKey > 0):
                addDic[-fKey].append(temp)
            else:
                searchSet[key].append(temp)



if __name__ == "__main__":
    for i in range(int(input())):
        n, m = list(map(int, stdin.readline().split()))

        negDicX = {}
        posSetX = set()
        hasXZero = False

        for v in stdin.readline().split():
            intV = int(v)
            if (intV == 0):
                hasXZero = True
            elif (intV > 0):
                posSetX.add(intV)
                add_edge(-intV,posSetX , negDicX)
            else:
               negDicX[intV] = []
               add_edge(-intV, negDicX, posSetX)


        negDicY = {}
        posSetY = set()
        hasYZero = False

        for v in stdin.readline().split():
            intV = int(v)
            if (intV == 0):
                hasYZero = True
            elif (intV > 0):
                posSetY.add(intV)
                add_edge(-intV,posSetY , negDicY)
            else:
                negDicY[intV] = []

                add_edge(-intV, negDicY, posSetY)

        counter = 0

        for xVal in negDicX:
            for v in negDicX[xVal]:
                counter += calculate( v, posSetY, negDicY )



        for yVal in negDicY:
            for v in negDicY[yVal]:
                counter += calculate(v, posSetX, negDicX)




        if(hasXZero and hasYZero):
            counter += (m-1) *(n-1)
        elif(hasXZero):
            counter += (m) * (n - 1)
        elif(hasYZero):
            counter += (m-1) * (n)

        print(int(counter))

