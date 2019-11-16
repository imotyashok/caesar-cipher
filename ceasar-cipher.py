# Caesar Cipher

def encode(plaintext, shift):
    coded_message = ''
    charSet= "ABCDEFGHIJKLMNOPQRSTUVWXYZ 0123456789abcdefghijklmnopqrstuvwxyz!@#$%^&*()_+{}|:-=[]\;,.<>?/"
    for symbol in plaintext:
        if symbol in charSet:
            number = charSet.find(symbol)-charSet.find('A')
            code_number = (number + shift) % 92
            code_letter = charSet[code_number + charSet.find('A')]
            coded_message = coded_message + code_letter
        else:
            coded_message = coded_message + symbol
    return coded_message
    
def decode(codetext, shift):
    decoded_message = ''
    charSet= "ABCDEFGHIJKLMNOPQRSTUVWXYZ 0123456789abcdefghijklmnopqrstuvwxyz!@#$%^&*()_+{}|:-=[]\;,.<>?/"
    for symbol in codetext:
        if symbol in charSet:
            number = charSet.find(symbol) - charSet.find('A')
            decode_number = (number - shift) % 92
            decode_letter = charSet[decode_number + charSet.find('A')]
            decoded_message = decoded_message + decode_letter
        else:
            decoded_message = decoded_message + symbol
    return decoded_message


def main():

    choice = input(">>> Would you like to encode or decode a message? \n"
          "(Type \"e\" for encode, \"d\" for decode): ").lower()

    if choice == 'e':
        secretMessage = input(">>> Type the secret message: ")
        shift = int(input(">>> Type a random positive integer shift value: "))
        print("(NOTE: if you want to decode the secret message later, you will need"
              " to use the same shift value!)")

        codedMessage = encode(secretMessage, shift)
        print(">>> The encoded message is : ", codedMessage)

    elif choice == "d":

        decodeInput = input(">>> Please type the message you would like to decode: ")
        decodeShift = int(input(">>> Please enter the shift value associated with the message: "))
        decodedMessage = decode(decodeInput,decodeShift)
        print(">>> The decoded message is : ", decodedMessage)
    else:
        print("Sorry, the choice \"%s\" is not recognized." % choice)

main()
