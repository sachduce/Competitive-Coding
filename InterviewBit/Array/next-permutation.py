
def nextPermutation( A):
    n = len(A);
    flag = True;
    i = n- 2;
    while (i >= 0 and A[i] >= A[i + 1]):
        i -= 1;
    if (i != -1):
        flag = False
    j = i + 1;
    while j < n and A[j] > A[i]:
        print("{} {} {} {}".format(A[j], A[i], j, i))
        j += 1
    print("{} {}".format(i, j));
    j -= 1
    A[i], A[j] = A[j], A[i]
    left = i + 1
    right = n - 1
    while left < right:
        A[left], A[right] = A[right], A[left]
        left += 1
        right -= 1

    if (flag):
        A.reverse();
    return A;
if __name__ == "__main__":
    A = [1, 91, 102, 1, 1]
    nextPermutation(A);
    print(A);
