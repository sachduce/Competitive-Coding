import math;
from sys import stdin;

MAX = 10**4 +1;

factor = [0] * (MAX + 1);

def generatePrimeFactors():
    factor[1] = 1;

    for i in range(2, MAX):
        factor[i] = i;

    for i in range(4, MAX, 2):
        factor[i] = 2;

    i = 3;
    while (i * i < MAX):

        if (factor[i] == i):

            j = i * i;
            while (j < MAX):

                if (factor[j] == j):
                    factor[j] = i;
                j += i;
        i += 1;




def calculateNoOFactors(n):
    if (n == 1):
        return 1;

    ans = 1;

    dup = factor[n];


    c = 1;


    j = int(n / factor[n]);


    while (j > 1):

        if (factor[j] == dup):
            c += 1;

        else:
            dup = factor[j];
            ans = ans * (c + 1);
            c = 1;


        j = int(j / factor[j]);


    ans = ans * (c + 1);

    return ans;



def getFactors(num):
    count =0
    for x in range(4, num+1):
        ff = calculateNoOFactors(x) -2
        if(ff%2 ==1):
            ff = (ff-1)//2 +1
        else:
            ff = ff//2
        count += ff
    return count


if __name__ == "__main__":
    generatePrimeFactors()
    print(factor[0:25])
    # while(True):
    #     try:
    #         n = int(stdin.readline())
    #         if(n< 1):
    #             break
    #         print(getFactors(n) + n)
    #     except:
    #         break

