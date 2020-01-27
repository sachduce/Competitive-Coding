from sys import stdin

def getNextPalindrome(num):
    length = len(num)
    hasChanged = False;
    for i in range(length//2-1, -1, -1):
        if(hasChanged):
            num[length - i-1] = num[i]
        else:
            if(num[i] > num[length - i-1]):
                num[length - i - 1] = num[i]
                hasChanged = True

            elif(num[i] < num[length - i-1]):
                if(length %2 ==1):
                    num[length//2] += 1
                else:
                    num[length//2 -1] += 1
                    num[length//2] = num[length//2 -1]

                num[length - i -1] = num[i]
                hasChanged = True

    if(not hasChanged):
        if (length % 2 == 1):
            num[length // 2] += 1

        else:
            num[length // 2 - 1] += 1
            num[length // 2] = num[length // 2 - 1]


    if(num[length // 2] == 10):
        mid = length//2
        if(length %2 == 0):
            mid -= 1
        for i in range(mid, 0, -1):
            if(num[i] == 10):
                num[i] = 0
                num[length -i-1] =num[i]
                num[i-1] +=1
                num[length -i] =num[i-1]
                if(num[i-1] != 10):
                    break
        if(num[0] == 10):
            num[length -1] =1
            if(length == 1):
                num.append(1)

    return "".join(map(str, num))


if __name__ == "__main__":
    for i in range(int(input())):
        inputString = stdin.readline()
        x = []
        first = True
        for ele in inputString:
            try:
                if(ele == '0' and first):
                    pass
                else:
                    x.append(int(ele))
                    first = False
            except:
                pass
        if(first):
            x.append(0)
        print(getNextPalindrome(x))
