# Caesar Cipher

CHAR_SET = "AMNBVCXZLKJHGFDSPOIUYTREWQ `~!@#$%^&*()_+|{}|:\'\"-=[]\;,.<>?/amnbvcxzlkjhgfdspoiuytrewq0192837465"

def encode(plaintext, shift):
    coded_message = ''
    for symbol in plaintext:
        if symbol in CHAR_SET:
            number = CHAR_SET.find(symbol) - CHAR_SET.find('A')
            code_number = (number + shift) % 96
            code_letter = CHAR_SET[code_number + CHAR_SET.find('A')]
            coded_message = coded_message + code_letter
        else:
            coded_message = coded_message + symbol
    return coded_message
    
def decode(codetext, shift):
    decoded_message = ''
    for symbol in codetext:
        if symbol in CHAR_SET:
            number = CHAR_SET.find(symbol) - CHAR_SET.find('A')
            decode_number = (number - shift) % 96
            decode_letter = CHAR_SET[decode_number + CHAR_SET.find('A')]
            decoded_message = decoded_message + decode_letter
        else:
            decoded_message = decoded_message + symbol
    return decoded_message

def restart():
    answer = input(">>> Would you like to run the program again? (y/n) ").lower()
    if  answer == "y" or answer == "yes":
        return True
    elif answer == "n" or answer == "no":
        print("Thank you for using the Caesar Cipher!")
        return False
    else:
        print("Sorry, that option isn't recognized. ")
        return False

def main():
    yes = True
    while yes:
        choice = input(">>> Would you like to encode or decode a message? \n"
              "(Type \"e\" for encode, \"d\" for decode): ").lower()

        if choice == 'e':
            secretMessage = input(">>> Type the secret message: ")
            shift = int(input(">>> Type a random positive integer shift value: "))
            print("(NOTE: if you want to decode the secret message later, you will need"
                  " to use the same shift value!)")

            codedMessage = encode(secretMessage, shift)
            print(">>> The encoded message is : ", codedMessage)

            yes = restart()

        elif choice == "d":

            decodeInput = input(">>> Please type the message you would like to decode: ")
            decodeShift = int(input(">>> Please enter the shift value associated with the message: "))
            decodedMessage = decode(decodeInput,decodeShift)
            print(">>> The decoded message is : ", decodedMessage)

            yes = restart()

        else:
            print("Sorry, the choice \"%s\" is not recognized." % choice)
            yes = False

main()
