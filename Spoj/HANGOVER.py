from sys import stdin

if __name__ == "__main__":
    while(True):
        k = float(stdin.readline())

        if(k == 0):
            break
        step =1
        while(k > 0):
            step +=1
            k =  k-1.0/step
        print("{} card(s)".format(step-1))

