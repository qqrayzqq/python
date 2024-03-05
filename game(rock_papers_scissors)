
import random

cnt_player = 0
cnt_computer = 0

while cnt_player < 5 or cnt_computer < 5:
    List_ = ['rock', 'paper', 'scissors']
    computer = random.choice(List_)
    player = None
    while player not in List_:
        player = input(str('Write your choice: rock, paper or scissors\n'))
    if player == computer:
        print("Draw!")
    elif player == 'rock' and computer == 'scissors':
        cnt_player += 1
        print("Player wins. Score is {}:{}".format(cnt_player, cnt_computer))
    elif player == 'paper' and computer == 'rock':
        cnt_player += 1
        print("Player wins. Score is {}:{}".format(cnt_player, cnt_computer))
    elif player == 'scissors' and computer == 'paper':
        cnt_player += 1
        print("Player wins. Score is {}:{}".format(cnt_player, cnt_computer))
    elif player == 'scissors' and computer == 'rock':
        cnt_computer += 1
        print("Computer wins. Score is {}:{}".format(cnt_player, cnt_computer))
    elif player == 'paper' and computer == 'scissors':
        cnt_computer += 1
        print("Computer wins. Score is {}:{}".format(cnt_player, cnt_computer))
    elif player == 'rock' and computer == 'paper':
        cnt_computer += 1
        print("Computer wins. Score is {}:{}".format(cnt_player, cnt_computer))
    if cnt_player == 5 or cnt_computer == 5:
        if cnt_computer == 5:
            print("Computer wins!")
        else:
            print("Player wins!")
        answerList = ['yes', 'no']
        answer = None
        while answer not in answerList:
            answer = input(str("You want one more game?(yes or no)\n"))
        if answer == 'yes':
            cnt_player = 0
            cnt_computer = 0
        else:
            break
print("GG!")
