from sys import stdin, stdout

def countSetBits(n):
    n ^= n >> 32;
    n ^= n >> 16;
    n ^= n >> 8;
    n ^= n >> 4;
    n ^= n >> 2;
    n ^= n >> 1;
    return (n & 1) == 1;


if __name__ == "__main__":

    for i in range(int(input())):
        n, q = list(map(int, stdin.readline().split()))

        countOdd = 0


        for v in stdin.readline().split():
            if(countSetBits(int(v))):
                countOdd +=1

        countEven = str(n -countOdd)
        countOdd = str(countOdd)

        for j in range(q):
            p = int(stdin.readline())

            if(countSetBits(p)):
                stdout.write(countOdd +' '+ countEven+ '\n')
            else:
                stdout.write(countEven+' '+ countOdd+ '\n' )
