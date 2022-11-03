from playsound import playsound
import time
#Morse Alphabet Dictionary
morse_alphabet = {
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "a": ".-",
    "b": "-...",
    "c": "-.-.",
    "d": "-..",
    "e": ".",
    "f": "..-.",
    "g": "--.",
    "h": "....",
    "i": "..",
    "j": ".---",
    "k": "-.-",
    "l": ".-..",
    "m": "--",
    "n": "-.",
    "o": "---",
    "p": ".--.",
    "q": "--.-",
    "r": ".-.",
    "s": "...",
    "t": "-",
    "u": "..-",
    "v": "...-",
    "w": ".--",
    "x": "-..-",
    "y": "-.--",
    "z": "--..",
    ".": ".-.-.-",
    ",": "--..--",
    "?": "..--..",
    "!": "-.-.--",
    "-": "-....-",
    "/": "-..-.",
    "@": ".--.-.",
    "(": "-.--.",
    ")": "-.--.-",
    " ": " "
}

#Invert Dictionary
alphabet = {value: key for (key,value) in morse_alphabet.items()}

#Available characters
characters = []
for char in morse_alphabet:
    characters.append(char)

#Boolean for loop
is_on = True

#Define Functions
def encrpyt(message):
    encrypted_message = ""
    for char in message:
        if char in characters:
            if char != " ":
                encrypted_message += morse_alphabet[char] + " "

            else:
                encrypted_message += " "
        else:
            print(f"Character not defined!\nHere is a list of all characters: {characters}")

    return encrypted_message


#Test message to decrypt "my test"
#-- -.--  - . ... - 
def decrypt(message):
    decrypted_message = ""
    letter = ""

    for char in message:
        if char != " ":
            letter += char
            spaces = 0
        
        else:
            spaces += 1

            if spaces == 1:
                character = alphabet[letter]
                decrypted_message += character
                letter = ""
            
            elif spaces == 2:
                decrypted_message += " "
                spaces = 0
            
    return decrypted_message


#def play_morse(code):
#    for sign in code:
#        if sign == ".":
#            playsound("dot.mp3")
#        
#        elif sign == "-":
#            playsound("dash.mp3")
#
#        else:
#            time.sleep(0.5)

#Convert Loop
while is_on:

    mode = input("Choose your mode: 'E' for Encrypt, 'D' for decrypt and 'S' to stop the converter!\n").lower()

    if mode == "s":
        is_on = False
        print("Converter stopped!")
    
    elif mode == "e":
        text = input("What do you want to encrypt?\n").lower()
        encrpyted_text = encrpyt(text)
        print(encrpyted_text)
        #play_morse(encrpyted_text)

    elif mode == "d":
        text = input("What do you want to decrypt?\n")
        print(decrypt(text))

    else:
        print("Method not defined! Please try again!")

