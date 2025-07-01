alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']


def encryption(text,shift):
    cipherText = ""
    for char in text:
        if char in alphabets:
            position = alphabets.index(char)
            newPosition = (position+shift) % 26
            cipherText += alphabets[newPosition]
        else:
            cipherText += char
    print("Here's the text after encryption: ",cipherText)

def decryption(cipherText,shift):
    plainText = ""
    for char in cipherText:
        if char in alphabets:
            position = alphabets.index(char)
            oldPosition = (position-shift) % 26
            plainText += alphabets[oldPosition]
        else:
            plainText += char
    
    print(f"The decrypted text is: {plainText}")


over = False
while not over:
    task = input("Type 'encrypt' for encryption purposes and 'decrypt' for decryption purpose: ").lower()
    if task not in ['encrypt','decrypt']:
        print("Please enter a valid command!! Try again")
        continue
    text = input("Type your message:\n").lower()
    try:
        shift = int(input("Enter the shift value (integer): \n"))
    except ValueError:
        print("The shift value must be an integer")
        continue

    if task == 'encrypt':
        encryption(text,shift)
    elif task == 'decrypt':
        decryption(text,shift)
    
    again = input("Enter 'yes' to continue and 'no' to exit ")
    
    if again.strip().lower() == 'no':
        over = True
        print("Bye! Game is over now")