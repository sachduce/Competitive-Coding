
def gcdExtended(a, b, x, y):

    if a == 0 :
        x = 0
        y = 1
        return b

    x1 = 1
    y1 = 1
    gcd = gcdExtended( b %a, a, x1, y1)

    x = y1 - ( b /a) * x1
    y = x1

    return gcd

if __name__ == "__main__":
    lastVal = 2;
    for i in range(int(input())):
        n = int(input());
        sets = [];
        hasCommon = False;

        for j in range(lastVal , n+1):
            for set in sets:
                hasCommon = gcdExtended(set[0], j,1,1) > 1;
                if (not hasCommon):
                    set.append(j)
                    set[0] *= j;
                    break;
            if(hasCommon or not len(sets) ):
                sets.append([j ,j]);
        if(len(sets)):
            sets[0].append(1);
        else:
            sets.append([1, 1]);

        print(len(sets));
        for set in sets:
            set[0] = len(set) -1;
            print(*set, sep=' ')

