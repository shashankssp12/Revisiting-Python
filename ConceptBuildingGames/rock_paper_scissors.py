# TODO:
'''
# random pick by computer
# player input
# compare result -Tell who won
# ask if the player wants play again
'''
import random

choices = ['rock','paper','scissors']
computer = random.choice(choices);
player_score =0
computer_score=0
total_rounds = 1
while True:
    player = None
    counter =0
    while player not in choices:
        if counter>0 :
            print("You cannot choose that, try again!")
        counter=counter+1
        player = input("rock,paper or scissors-->").lower()
    #Show inputs:
    print("Player:",player)
    print("Computer:",computer) 
    # Result --Win or Lose 
    if computer == player:
        print("It's a tie.")
        computer_score,player_score=computer_score+1,player_score+1;
    elif computer == "rock":
        if player == "paper":
            print("You Won!")
            player_score=player_score+1
        else :
            print("You lost.")
            computer_score = computer_score + 1
     
    elif computer == "paper":
        if player == "scissors":
            print("You Won!")
            player_score=player_score+1

        else :
            print("You lost.")
            computer_score = computer_score + 1

    elif computer == "scissors":
        if player == "rock":
            print("You Won!")
            player_score=player_score+1
        else :
            print("You lost.")
            computer_score = computer_score + 1
    total_rounds= total_rounds+1
    ###################################
    #Score Board
    ###################################
    replay = input("Press 'y' to play again:").lower()
    if replay != 'y':
        print("""
---------------Score Board----------------
Total Rounds:{2}
Computer:{0} | Player:{1}
------------------------------------------
              """
              .format(computer_score,player_score, total_rounds))
        if computer_score == player_score:
            print("It's a Tie!")
        elif player_score > computer_score:
            print("YOU WON!")
        else:
            print("YOU LOST.")
        break
    