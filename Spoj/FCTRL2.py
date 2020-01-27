fact = [1] * 101
for i in range(1,101):
    fact[i] = i * fact[i - 1]

if __name__ == "__main__":

    for i in range(int(input())):
        n = int(input())
        print(fact[n])