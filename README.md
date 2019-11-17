# Caesar Cipher 

## What is a Caesar Cipher?
The Caesar cipher is one of the simplest encryption techniques. It involves encoding a given message by "shifting" each character by a certain shift value, and decrypting the message by shifting each character in the message back by the same shift value. To learn more about Caesar ciphers, check out these links:
- http://practicalcryptography.com/ciphers/caesar-cipher/
- https://www.khanacademy.org/computing/computer-science/cryptography/crypt/v/caesar-cipher

## Program Description
This program implements a Caesar cipher that can encode and decode messages containing capital letters, lowercase letters, numbers, spaces, and symbols (for now, the symbols it can encode and decode are the following: **!@#$%^&*()_+{}|:-=[]\;,.<>?/** ). The program asks you if you want to encode or decode a message, and by inputting the shift value and message, the user can encode or decode it. Here is what a sample run of the program looks like: 
```
[Encoding]

>>> Would you like to encode or decode a message? 
(Type "e" for encode, "d" for decode): e
>>> Type the secret message: 3nC0dED m355@gE!
>>> Type a random positive integer shift value: 18
(NOTE: if you want to decode the secret message later, you will need to use the same shift value!)
>>> The encoded message is :  l^UivWVh%lnn]yW[

[Decoding]

>>> Would you like to encode or decode a message? 
(Type "e" for encode, "d" for decode): d
>>> Please type the message you would like to decode: l^UivWVh%lnn]yW[
>>> Please enter the shift value associated with the message: 18
>>> The decoded message is :  3nC0dED m355@gE!

```

So, what can you use this cipher for? Just about anything you can think of! I was inspired to write this program when I got tired of forgetting which usernames and passwords belong to which one of the dozens accounts I have, and realized that I'd be much better off just writing everything down. However, I'm not comfortable with having a physical document that has all my login information to all my important accounts plainly written down for any plebeian to find and read. So, why not encrypt it! If you forget your information, you can decrypt it using the cipher (so long as you don't forget the original shift value you used). This way, it's safe to write it down and you won't have to worry about some random person getting access to your information. 

## Safety 
After doing some reading on the Caesar cipher, your inquisitive self might be questioning how safe using this cipher really is, since all it takes to break the code is knowing the shift value and doing some frequency analysis. The traditional cipher only uses the 26 letters of the English alphabet, so to decode a message you simply need to take each letter, subtract the shift value from it, and find the remainder when divided by 26 (mod 26). So, you can brute force your way through the solution by testing just 25 possible shift values. With this program, you'd have to brute force your way through 92 possible shift values, since letters, numbers, and various symbols are also incorporated into it. Someone who's very determined will still be able to break the cipher (it's still a pretty simple cipher as far as encryption techniques go), but for most general purposes, this cipher is pretty secure. 

## Ideas for Future Implementation 
#### Adding more symbols and characters 
Currently, the cipher can encode and decode messages that consist of 92 characters. To make it more interesting (and harder to break into), I will consider adding more special characters to it (for example, accented letters, Greek letters, etc.). 
#### Error Handling
Since we're dealing with user input and specific values and options, the program needs a bit more error handling than what it has now. For example, if the user accidentally mistypes a non-integer for the shift value, the program fails with an error message. It'll be better if the program intercepted that message and exited gracefully.
#### GUI 
Currently, the program can only be run through a python IDE/compiler. I'd like to implement a GUI for this program just to make it more easily accessible and to make it look prettier.
