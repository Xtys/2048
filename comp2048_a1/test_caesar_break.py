# -*- coding: utf-8 -*-
"""
Determine the shift of the Caesar Cypher

Created on Sat Feb  2 23:03:02 2019

@author: shakes
"""
from collections import Counter
import string

message = "vod eco Dbi kxydrob yxo"
# "yxo dgy drboo pyeb psfo csh cofox osqrd xsxo dox"
# "Zyp cpxpxmpc ez wzzv fa le esp delcd lyo yze ozhy le jzfc qppe Ehz ypgpc rtgp fa hzcv Hzcv rtgpd jzf xplytyr lyo afcazdp lyo wtqp td pxaej hteszfe te Escpp tq jzf lcp wfnvj pyzfrs ez qtyo wzgp cpxpxmpc te td espcp lyo ozye esczh te lhlj Depaspy Slhvtyr"

#frequency of each letter
letter_counts = Counter(message)
#print(letter_counts)

#find max letter
maxFreq = -1
maxLetter = None
for letter, freq in letter_counts.items():
    print(letter, ":", freq)
    #INSERT CODE TO REMEMBER MAX
    if letter != " ":
        if freq > maxFreq:
            maxFreq = freq
            maxLetter = letter
print("Max Ocurring Letter:", maxLetter)

#predict shift
#assume max letter is 'e'
letters = string.ascii_letters #contains 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
# shift = ((ord(maxLetter) - 97) - ord('e') - 97) % 26

#part c
shift = (ord(maxLetter) - 101) % 26
print("Predicted Shift:", shift)

totalLetters = 26
keys = {}
for index, letter in enumerate(letters):
    if index < totalLetters:  # lowercase
        og_letter = chr((ord(letter) - 97 - shift) % 26 + 97)
        keys[letter] = og_letter
    else:  # uppercase
        og_letter = chr((ord(letter) - 65 - shift) % 26 + 65)
        keys[letter] = og_letter

decryptedMessage = []
for letter in message:
    if letter == ' ':
        decryptedMessage.append(letter)
    else:
        decryptedMessage.append(keys[letter])
decrypted_result = ''.join(decryptedMessage)
print("Decrypted Message:", decrypted_result)
