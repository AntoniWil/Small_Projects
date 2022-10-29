
import random
print()
print("THIS IS RANDOM DICE ROLL!!\n\n")


def roll_die(max_value):
    num = random.randint(1, max_value)
    return (num)

def determine_winner(player1, player_roll, cm1, cm1roll):
    if player_roll > cm1roll:
        print(player1 + " Wins")
    if cm1roll > player_roll:
        print(cm1 + " Wins") 
    if player_roll == cm1roll:
        print("TIE")   
def clear_screen():
    print("\033[H\033[J", end="")       

first_player = input("Enter your name? ")
sec_player = input("What is the name of the second player? ")


def main():
    human_roll = roll_die(20)
    computer_roll = roll_die(20)
    human_player = (first_player)
    computer_player = (sec_player)
    


    clear_screen()
    
    print(human_player + " rolled: " + str(human_roll))
    print(computer_player + " rolled: " + str(computer_roll))
    determine_winner(human_player, human_roll, computer_player, computer_roll)
    




main()







