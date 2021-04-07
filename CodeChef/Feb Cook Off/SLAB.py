from sys import stdin


if __name__ == "__main__":
    for i in range(int(input())):
        income = int(stdin.readline())
        temp = income
        tax = 0
        if(temp > 1500000):
            tax += 30* (temp -1500000) //100
            temp =1500000

        if(temp > 1250000):
            tax += 25 * (temp - 1250000) // 100
            temp = 1250000

        if(temp > 1000000):
            tax += 20 * (temp - 1000000) // 100
            temp = 1000000

        if (temp > 750000):
            tax += 15 * (temp - 750000) // 100
            temp = 750000

        if (temp > 500000):
            tax += 10 * (temp - 500000) // 100
            temp = 500000

        if (temp > 250000):
            tax += 5 * (temp - 250000) // 100
            temp = 250000


        print(income -tax)