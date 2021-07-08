import random

def game():
    user=print(input("what is you choice?'r' for rock,'p' for paper,'s' for scissors........."))
    computer=random.choice(['r','p','s'])
    if (user==computer):
        print("match is tie")

    if is_win(user,computer):
        print ("you won")
        
    print("you lost!")  


def is_win(player,opp):
    if((player=='s'and opp=='p') or( player=='r'and opp=='s') or (player=='p' and opp=='r')):
        return True

game()