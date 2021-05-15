## Rock Paper Scissors game - CLI Interface
## Created 2021/05/07
## Version 1.0

choice = ["rock", "paper", "scissors"]

def Game():
    print("====================")
    print("***      RPS     ***")
    print("====================")
    
    Player = PlayerChoice()
    Computer = AiChoice()

    if(DetermineWinner(Player, Computer)): print("You Win!")
    else: print("Sorry, you lost!")

def PlayerChoice():
    User = input("Please pick Rock, Paper, or Scissors: ").lower()
    while User not in choice:
        User = input("Input invalid. Type Rock, Paper, or Scissors: ").lower()
    return User

def AiChoice():
    import random
    return random.choice(choice)

def DetermineWinner(Player, Computer):
    while Player == Computer:
        print("Tie! Try again.")
        Player = PlayerChoice()
        Computer = AiChoice()
    print("The computer chose: " + Computer)
    Player = choice.index(Player)
    Computer = choice.index(Computer)
    if  (Player == 0) and (Computer == 2): return True
    elif(Player == 1) and (Computer == 0): return True
    elif(Player == 2) and (Computer == 1): return True
    return False

Game()
