from sys import stdin
centuryCodes ={
        0: 6,
        1: 4,
        2: 2,
        3: 0
    }

def getDay(y, isLeap):
    monCode  =3
    if(isLeap):
        monCode =2

    cy = (y//100) % 4
    cenCode = centuryCodes[cy]
    lastTwoDigits = y%100
    oddDays = (1 + monCode + lastTwoDigits + lastTwoDigits//4 + cenCode) % 7
    return oddDays

def isLeapYear(y):
    if(y % 400 == 0):
        return True
    if(y % 100 == 0):
        return False
    if( y % 4 == 0):
        return True
    return False
if __name__ == "__main__":

    for i in range(int(input())):
        m1, y1 = list(map(int, stdin.readline().split()))
        m2, y2 = list(map(int, stdin.readline().split()))
        start = y1
        end = y2
        count =0
        if(m1 > 2):
            start = y1+1
        if(m2 < 2):
            end = y2 -1

        diff = end - start +1
        if(diff >= 400):
            quotient = diff//400

            rem = diff % 400
            count += quotient*101

            start = quotient*400 +start
            end = start + rem -1


        for j in range(start, end +1):
            isLeap = isLeapYear(j)
            day = getDay(j, isLeap)
            if(day == 6):
                count += 1
            if(day == 0):
                if(not isLeap):
                    count +=1
        print(count)




