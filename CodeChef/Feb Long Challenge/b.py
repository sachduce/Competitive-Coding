from sys import stdin
import math

def binarySearch(arr, start, end, s):
    if(start > end):
        return False
    if(start == end):
        if(arr[start] ==s):
            return True
        return False
    mid = (start +end)//2
    if(arr[mid] ==s):
        return True
    if(arr[mid] >s):
        return binarySearch(arr, start, mid-1, s)
    elif (arr[mid] <s):
        return binarySearch(arr, mid+1, end, s)


if __name__ == "__main__":
    for i in range(int(input())):
        n, m = list(map(int, stdin.readline().split()))
        posX = []
        negX = []
        hasXZero = False
        for v in stdin.readline().split():
            intV = int(v)
            if(intV == 0):
                hasXZero = True
            elif(intV > 0):
                posX.append(intV)
            else:
                negX.append(intV)

        posX = sorted(posX)
        negX = sorted(negX)


        posY = []
        negY = []
        hasYZero = False
        for v in stdin.readline().split():
            intV = int(v)
            if (intV == 0):
                hasYZero = True
            elif (intV > 0):
                posY.append(intV)
            else:
                negY.append(intV)

        posY = sorted(posY)
        negY = sorted(negY)
        counter = 0

        lenPosX  = len(posX)
        lenNegX = len(negX)
        lenPosY = len(posY)
        lenNegY = len(negY)

        for i in range(lenPosX):
            for j in range(lenNegX):
                temp = math.sqrt(-1*posX[i] * negX[j])
                if(temp -math.floor(temp) ==0):
                    if(binarySearch(posY, 0, lenPosY-1, temp)):
                        counter +=1
                    if (binarySearch(negY, 0, lenNegY - 1, -temp)):
                        counter += 1




        for i in range(lenPosY):
            for j in range(lenNegY):

                temp = math.sqrt(-1*posY[i]*negY[j])
                if (temp - math.floor(temp) == 0):
                    if (binarySearch(posX, 0, lenPosX - 1, temp)):
                        counter += 1
                    if (binarySearch(negX, 0, lenNegX - 1, -temp)):
                        counter += 1


        if(hasXZero and hasYZero):
            counter += (m-1) *(n-1)
        elif(hasXZero):
            counter += (m) * (n - 1)
        elif(hasYZero):
            counter += (m-1) * (n)
        print(counter)

