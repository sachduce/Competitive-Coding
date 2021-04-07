from sys import stdin;
if __name__ == "__main__":
    for _ in range(int(input())):
        N, M = list(map(int, stdin.readline().split()));
        initialRating = list(map(int, stdin.readline().split()));
        rating = [[0 for _ in range(M)] for _ in range(N)];
        player =  [[0 for _ in range(2)] for _ in range(N)];
        ans = 0;
        for i in range(N):
            tempRating = 0;
            month = list(map(int, stdin.readline().split()));
            for j in range(M):
                if j ==0:
                    rating[i][j] = initialRating[i] + month[j];
                else:
                    rating[i][j] = rating[i][j-1] + month[j];
                if(rating[i][j] > tempRating):
                    tempRating = rating[i][j];
                    player[i][0] = j;

        ranking = [[-1 for _ in range(M)] for _ in range(N)];
        for j in range(M):
            monthyRatings = [];
            for i in range(N):
                monthyRatings.append(rating[i][j]);
            s = sorted(range(N), key=lambda k: -monthyRatings[k]);

            temp = float('inf');
            for i in range(N):
                if(monthyRatings[s[i]] == temp):
                    ranking[s[i]][j] = ranking[s[i-1]][j];
                else:
                    temp = monthyRatings[s[i]];
                    ranking[s[i]][j] = i+1;

        for i in range(N):
            player[i][1] = ranking[i].index(min(ranking[i]));

        for p in player:
            if(p[0] != p[1]):
                ans += 1;
        print(ans);


