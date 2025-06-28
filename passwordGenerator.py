import random as rn

# We are considering letters, numbers and specialChar as password digits
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

numbers = ['0','1','2','3','4','5','6','7','8','9']
specialChar = ['@','#','&','*','+','!','&']

print("Welcome to Password Generator!")

noLetter = int(input("Enter how many letters you want: "))
noSymbols = int(input("Enter how many symbols you want: "))
noNumbers = int(input("Enter how many numbers you want: "))
password = []
finalPass = "" 

#randomly choosing from the letters, symbols and numbers
for i in range(noLetter):
    password += rn.choice(letters)

for i in range(noSymbols):
    password += rn.choice(specialChar)

for i in range(noNumbers):
    password += rn.choice(numbers)
rn.shuffle(password) # shuffling the password
print("".join(password)) # converting the list to string