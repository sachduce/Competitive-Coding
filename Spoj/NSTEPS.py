from sys import stdin

if __name__ == "__main__":
    for i in range(int(input())):
        x,y =  list(map(int,stdin.readline().split()))
        ans = "No Number"
        if(x == y):
            weight = y//2
            ans = 3*(weight) + 1*(y - weight)
        elif(x-y ==2):
            weight = y // 2
            ans = 2 + 3 * (weight) + 1 * (y - weight)


        print(ans)

