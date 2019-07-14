import random

def close():
    exit = input("Press space to close or enter tto play again")
    if exit == "k" or exit == "K":
        return 0
    if exit == "":
        start()
    else:
        close()
def start():
    def game():
        bot = random.randint(1, 3)
        if bot == intro:
            print("The bot chose the same as you!\n")
            print("It is a Tie!")
            close()
        elif bot == 1 and intro == 2:
            print("The bot chose Rock!\n")
            print("You win!")
            close()
        elif bot == 2 and intro == 1:
            print("The bot chose Paper!\n")
            print("The bot wins!")
            close()
        elif bot == 3 and intro == 2:
            print("The bot chose Scissors!\n")
            print("The bot wins!")
            close()
        elif bot == 2 and intro == 3:
            print("The bot chose Paper!\n")
            print("You win!")
            close()
        elif bot == 1 and intro == 3:
            print("The bot chose Rock!\n")
            print("The bot wins!")
            close()
        elif bot == 3 and intro == 1:
            print("The bot chose Scissors!\n")
            print("You Win!")
            close()



    intro = input("Rock, Paper, Scissors\n")
    if intro == "Rock" or intro == "rock":
        print("\n")
        intro = 1
        game()
    elif intro == "Paper" or intro == "paper":
        print("\n")
        intro = 2
        game()
    elif intro == "Scissors" or intro == "scissors":
        print("\n")
        intro = 3
        game()
    else:
        print("Retry")
        start()



start()
