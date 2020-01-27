from sys import stdin

if __name__ == "__main__":
    while(True):
        col = int(input())
        if(col <= 0):
            break
        inputString = stdin.readline().rstrip()
        rows = len(inputString) // col +1;
        if(len(inputString) % col == 0):
            rows = len(inputString) // col;


        inputArr = [['' for i in range(col)] for j in range(rows)]
        i =0;
        j=0
        for ele in inputString:
            inputArr[i][j] = ele
            if(i%2 == 0 and j== col -1):
                i += 1
            elif(i %2 ==0):
                j += 1
            elif(i% 2 ==1 and j == 0):
                i+=1
            elif(i%2 ==1):
                j -= 1


        for column in range(col):
            for row in range(rows):
                print(inputArr[row][column], end='')
        print("")