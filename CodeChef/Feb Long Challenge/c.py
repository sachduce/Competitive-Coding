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
        count =0
        for j in range(y1, y2+1):
            start = 2
            end = 2
            if(j == y1):
                start = m1
            if(j == y2):
                end = m2
            if(start <=2 and end>=2):
                isLeap = isLeapYear(j)
                day = getDay(j, isLeap)
                if(day == 6):
                    count += 1
                if(day == 0):
                    if(not isLeap):
                        count +=1
        print(count)

