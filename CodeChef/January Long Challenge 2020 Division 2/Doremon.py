# cook your dish here

def isPalindrome(arr, i_x, i_y, temp_max):
    mid = (temp_max + 1) // 2 - 1;
    subArr1 = arr[mid + i_x][i_y: i_y + temp_max];
    lenSub1 = len(subArr1);
    for i in range(lenSub1 // 2):
        if subArr1[i] != subArr1[lenSub1 - i - 1]:
            return False

    subArr2 = [sublist[i_y + mid] for sublist in arr[i_x: i_x + temp_max]];
    lenSub2 = len(subArr2);
    for i in range(lenSub2 // 2):
        if subArr2[i] != subArr2[lenSub2 - i - 1]:
            return False

    if (subArr2 == subArr1):
        return True

    return False


if __name__ == '__main__':
    t = int(input());
    for i in range(t):
        n, m = [5,6]

        arr =[
            [2, 3, 4, 5, 6,4],
            [3, 4, 5, 6, 4,3],
            [4, 5, 6, 4,3,2 ],
            [5, 6,4,3, 2,5],
            [ 6, 4, 3, 2, 5,6],
        ]

        count = n * m;

        temp_max = 3;

        while (temp_max <= n and temp_max <= m):
            for i_y in range(m - temp_max + 1):
                for i_x in range(n - temp_max + 1):
                    flag = False
                    mid = (temp_max + 1) // 2 - 1;
                    for k in range(temp_max):
                        if(arr[i_x +k][mid + i_y] == arr[i_x + temp_max - k -1][mid + i_y] and
                                arr[i_x +k][mid + i_y] == arr[i_x +mid][k + i_y] and
                                arr[i_x +k][mid + i_y] == arr[i_x +mid][i_y + temp_max -1-k]):

                            flag = True;
                        else:
                            flag =False
                    if(flag):
                        count +=1


            temp_max += 2;

        print(count);

for i in range(5, -1, -1):
     print(i)

     for l in range(n):
         lastNot = 0;
         curvDict[l].left = lastNot
         if (curvDict[l].curve != 0):
             lastNot = l

         for r in range(l + 1, n):
             if (curvDict[r].curve != 0):
                 curvDict[l].right = r;
                 break;

for i in range(n - 1):
    if (i == 0):
        if (arr[i + 1] > arr[i]):
            flag = 'asc'
        else:
            flag = 'desc'
        curvDict[i].curve = 0;
    else:
        if (arr[i + 1] > arr[i] and flag == 'desc'):
            curvDict[i].curve = -1;
            flag = 'asc'
        if (arr[i + 1] < arr[i] and flag == 'asc'):
            curvDict[i].curve = 1
            flag = 'desc'

            for r in range(l + 1, n):
                if (curvDict[r].curve != 0):
                    curvDict[l].right = r;
                    break;



