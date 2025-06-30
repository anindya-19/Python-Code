import random as rn
word_list = ["apple","banana","mango","potato","strawberry"]

lives = 6 #6 lives is provided to the user
chosenWord = rn.choice(word_list) #computer chooses a random word from the list
display = [] 
#print(chosenWord)
for i in range(len(chosenWord)): #to initialize the blank spaces
    display += '_'
print(display)
counter = 0 # to keep track of same words getting repeated or not

gameOver = False

while not gameOver:
    guessedLetter = input("Enter a letter: ").lower()
    if counter > 0 and guessedLetter in display:
        print("____Try with some different letter____")
        lives -= 1
        print(f"{lives} lives remaining!!")
        continue
    for position in range(len(chosenWord)):
        letter = chosenWord[position] #to get the letter at the given position
        if letter == guessedLetter:
            display[position] = guessedLetter
            
    print(display)
    if guessedLetter not in chosenWord:
        lives -= 1
        print(f"{lives} lives remaining!")
        if lives == 0:
            gameOver = True
            print("You lose!")
    if '_' not in display:
        gameOver = True
        print("You Win!!")
    counter += 1