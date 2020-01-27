if __name__ == "__main__":
    for i in range(int(input())):
        p = 1
        div = 5
        n = int(input())
        count = 0
        while (n >= div):
            count += n // div
            p += 1;
            div = pow(5, p)

        print(count)