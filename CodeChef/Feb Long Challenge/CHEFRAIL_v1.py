from sys import stdin
import math

if __name__ == "__main__":
    for i in range(int(input())):
        n, m = list(map(int, stdin.readline().split()))

        dicX = {}
        hasXZero = False

        for v in stdin.readline().split():
            intV = int(v)
            if(intV == 0):
                hasXZero = True
            elif(intV > 0):
                if( intV in dicX):
                    dicX[intV] += 1
                else:
                    dicX[intV] =1
            else:
                if (-intV in dicX):
                    dicX[-intV] -= 1
                else:
                    dicX[-intV] = -1


        dicY = {}
        hasYZero = False

        for v in stdin.readline().split():
            intV = int(v)
            if (intV == 0):
                hasYZero = True
            elif (intV > 0):
                if (intV in dicY):
                    dicY[intV] += 1
                else:
                    dicY[intV] = 1
            else:
                if (-intV in dicY):
                    dicY[-intV] -= 1
                else:
                    dicY[-intV] = -1


        counter = 0

        dicXKeys = list(dicX.keys())
        dicYKeys = list(dicY.keys())

        lenX = len(dicXKeys)
        lenY = len(dicYKeys)


        for i in range(lenX):
            for j in range(i+1, lenX):
                x1 = dicX[dicXKeys[i]]
                x2 = dicX[dicXKeys[j]]
                mul =1

                if( (x1== -1 and x2 >=0) or (x1 ==1 and x2 <=0) or (x1 ==0) ):
                    temp = math.sqrt(dicXKeys[i] * dicXKeys[j])
                    if(temp - math.floor(temp) == 0):
                        intT = int(temp)
                        if(intT in dicY):
                            if(x1 ==0 and x2 ==0):
                                mul =2
                            if(dicY[intT] == 0):
                                counter += 2*mul
                            else:
                                counter += 1*mul

            if(x1 == 0):
                if(dicXKeys[i] in dicY):
                    if(dicY[dicXKeys[i]] == 0):
                        counter += 2
                    else:
                        counter +=1

        for i in range(lenY):
            for j in range(i+1, lenY):
                y1 = dicY[dicYKeys[i]]
                y2 = dicY[dicYKeys[j]]
                mul =1
                if( (y1== -1 and y2 >=0) or (y1 ==1 and y2 <=0) or (y1 ==0) ):
                    temp = math.sqrt( dicYKeys[i] * dicYKeys[j])
                    if(temp - math.floor(temp) == 0):
                        intT = int(temp)
                        if(intT in dicX):
                            if(y1 ==0 and y2 ==0):
                                mul =2
                            if(dicX[intT] == 0):
                                counter += 2*mul
                            else:
                                counter +=1*mul
            if (y1 == 0):
                if (dicYKeys[i] in dicX):
                    if (dicX[dicYKeys[i]] == 0):
                        counter += 2
                    else:
                        counter += 1


        if(hasXZero and hasYZero):
            counter += (m-1) *(n-1)
        elif(hasXZero):
            counter += (m) * (n - 1)
        elif(hasYZero):
            counter += (m-1) * (n)
        print(counter)

