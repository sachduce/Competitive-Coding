from sys import stdin

if __name__ == "__main__":
    for i in range(int(input())):
        n = int(input())
        palString = list(stdin.readline().rstrip())
        swapCount = 0
        mid = n//2
        flag = False
        left = 0

        la = True
        ra = True

        right = n-1


        while(left <= mid and right >= mid):
            if(palString[left] == palString[right]):
                left += 1
                right -= 1
                la = True
                ra = True
            elif(right == mid and palString[right] != palString[left]):
                flag = True
                break
            elif(left+1 <= mid and palString[left+1] == palString[right] and la):
                palString[left+1], palString[left] = palString[left], palString[left+1]
                left +=1
                la = False
                ra = True
                right -= 1
                swapCount +=1

            elif(right-1 >= mid and palString[right-1] == palString[left] and ra):
                palString[right - 1], palString[right] = palString[right], palString[right - 1]
                right -=1
                left +=1
                ra = False
                la = True
                swapCount += 1
            else:
                flag = True
                break


        if(flag):
            print('NO')
        else:
            print('YES')
            print(swapCount)




