import random as r
# 0 -> Rock
# 1 -> Paper
# 2 -> Scissor

# Rules :-
# Paper wins against rock
# Scissor wins against paper
# Paper wins against Rock

game_mapping = {
    0:"Rock",
    1:"Paper",
    2:"Scissor"
}
win_conditions = {
    (0, 2),  # Rock beats Scissor
    (1, 0),  # Paper beats Rock
    (2, 1)   # Scissor beats Paper
}
try:
    userChoice = int(input("Enter 0. for Rock \n 1. for Paper \n 2. for Scissor :\n ->"))

    if userChoice > 2 or userChoice < 0:
        print("You Have Entered an Invalid Number")
    else:
        computerChoice = r.randint(0,2)
        print("So Your Choice is :",game_mapping[userChoice])
        print("And Computer's Choice is: ",game_mapping[computerChoice])

        if computerChoice == userChoice:
            print("It is a draw!!")
        elif (userChoice,computerChoice) in win_conditions:
            print("You Win!!")
        else:
            print("You Lose!!")
except ValueError:
    print("Please enter a valid integer number")
except Exception as e:
    print(e)
    