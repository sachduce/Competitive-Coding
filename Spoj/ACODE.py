from sys import stdin

def comb(n,r):
    if(n<r):
        return 0
    num =1
    den =1
    for i in range(r+1, n+1):
        num *= i
    for j in range(2, n-r+1):
        den *= j
    # print("{} {}".format(num, den))
    return num//den

def calculateCombination(solve):
    count =1
    for key in solve:
        if(key == 2):
            count *= pow(2,solve[key])
            # print("count: {}".format(count))

        else:
            x =1
            for n in range(2,key):
                x += comb(n, key-n)
            count *= pow(x, solve[key])

    return count
if __name__ == "__main__":
    while(True):
        source = {}
        n = stdin.readline().rstrip()
        if(n == '0'):
            break

        length = len(n)
        # print(length)
        i =1
        x= 1
        while(i < length):
            # print("i: {}  n-i:{}".format(i, n[i]))

            if(n[i-1]=='1' and n[i] != '0'):
                x += 1
                # print("case 1: {}".format(x))
            elif(n[i-1] == '2' and n[i] in ['1', '2', '3', '4', '5', '6'] ):
                x += 1
                # print("case 2: {}".format(x))
            else:
                if (x > 1):
                    if (x in source):
                        source[x] += 1
                    else:
                        source[x] = 1
                x = 1

            if (i != length-1 and  n[i + 1] == '0'):
                if (x > 1):
                    x -= 1;
                    if (x > 1):
                        if (x in source):
                            source[x] += 1
                        else:
                            source[x] = 1
                x = 1

            i += 1

        if (x > 1):
            if (x in source):
                source[x] += 1
            else:
                source[x] = 1
        # print(source)
        print(calculateCombination(source))