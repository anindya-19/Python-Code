alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']


def encryption(text,shift):
    cipherText = ""
    for char in text:
        position = alphabets.index(char)
        newPosition = (position+shift) % 26

        cipherText += alphabets[newPosition]
    print("Here's the text after encryption: ",cipherText)

def decryption(text,shift):
    pass




task = input("Type 'encrypt' for encryption purposes and 'decrypt' for decryption purpose: ")

text = input("Type your message:\n")
shift = int(input("Enter the shift value: \n"))

if task == 'encrypt':
    encryption(text,shift)
elif task == 'decrypt':
    decryption(text,shift)