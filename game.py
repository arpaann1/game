import random

choices = [ 1, 2, 3 ]
s = 0
print(" 1 for rock \n 2 for paper \n 3 fro scissors")
n = int(input("enter nummber of round you want to play ="))
for i in range(n):
    print("round", i + 1)
    p = int(input("choose ROCK(1) PAPER(2) SCISSORS(3): \t"))
    c = random.choice(choices)
    print("computer chose",c)

    if p == c:
        print(" OOPSss  It's a tie")
    elif p == 1 and c == 3:                                   
        print("You win (congratulation)")
        s = s + 1
    elif p == 2 and c == 1:
        print("You win (congratulation)")
        s = s + 1
    elif p == 3 and c == 2:
        print("You win (congratulation)")
        s = s + 1
    else:
        print("You lose (better luck next time) \n")
print("your score is")
print(s)
print(f"yours Win rate: {s / n * 100:.2f}%")
print(f"bot Win rate: {100 - (s / n * 100):.2f}%")
if (i / 2 < s):
    print("score is less then half")
    print("need improvement")