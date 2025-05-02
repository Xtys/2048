# -*- coding: utf-8 -*-
"""
Caesar cypher script

Encode and decode messages by scrambling the letters in your message

Created on Fri Feb  1 23:06:50 2019

@author: shakes
"""
import string

letters = string.ascii_letters #contains 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

message = "Hi I am brandon and I am a com sci student" #type your message here
print("Message:", message)

#create the Caesar cypher
offset = 10 #choose your shift
totalLetters = 26
keys = {} #use dictionary for letter mapping
invkeys = {} #use dictionary for inverse letter mapping, you could use inverse search from original dict
for index, letter in enumerate(letters):
    # cypher setup
    if index < totalLetters: #lowercase
        #INSERT CODE HERE
        #letters to ASCII 97 - 122, value then normalize the range to 0–25
        # wrap around the alphabet if the shift exceeds 'z' : integers' congruence property
        shift_letter = chr((ord(letter) + offset - 97 )% totalLetters + 97)
        keys[letter] = shift_letter
    else: #uppercase
        #INSERT CODE HERE
       shift_letter = chr((ord(letter)  + offset - 65) % 26 + 65)
       keys[letter] = shift_letter

#creates the inverse mapping of the keys
# reverse lookup v: k for k,
invkeys = {v: k for k, v in keys.items()}

print("Cypher Dict:", keys)

#encrypt
encryptedMessage = []
for letter in message:
    if letter == ' ': #spaces
        encryptedMessage.append(letter)
    else:
        encryptedMessage.append(keys[letter])
print("Encrypted Message:", ''.join(encryptedMessage)) #join is used to put list inot string

#decrypt
decryptedMessage = []
for letter in encryptedMessage:
    if letter == ' ': #spaces
        decryptedMessage.append(letter)
    else:
        decryptedMessage.append(invkeys[letter])
print("Decrypted Message:", ''.join(decryptedMessage)) #join is used to put list inot string
