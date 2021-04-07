from sys import stdin;
questions = [
1048574,
1048573,
1048571,
1048567,
1048559,
1048543,
1048511,
1048447,
1048319,
1048063,
1047551,
1046527,
1044479,
1040383,
1032191,
1015807,
983039,
917503,
786431,
1048575
]


if __name__ == "__main__":
    for _ in range(int(input())):
        n = int(input());
        hidden_array = list(map(int, stdin.readline().split()));
        answers = [];
        setBits = [0]* 20;
        final = 0;
        for q in questions:
            print("1 {}".format(q));
            xor = 0;
            for h in hidden_array:
                xor += h^q;
            # answers.append(int(input()));
            answers.append(xor);
        for i in range(19):
            setBits[i] = (n + (answers[i] - answers[19])// pow(2, i))//2;
            final += (n- setBits[i])*pow(2, i);
        setBits[19] = (n + (final -answers[19])// pow(2, 19));
        ans = 0
        for i in range(20):
            ans += pow(2, i)*(setBits[i] %2);
        print("2 {}".format(ans));
        reply = 0;
        print("answers: {} final: {}".format(answers, final))
        for h in hidden_array:
            reply ^= h;
            print("h: {} hb: {}".format(h, bin(h).replace("0b", "") ))
        binaryReply = bin(reply).replace("0b", "")
        print("r: {} br: {} sb: {}".format(reply, binaryReply, setBits));
        # reply = int(input());
        # if(reply != ans):
        #     break;
