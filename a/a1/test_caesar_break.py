# -*- coding: utf-8 -*-
"""
Determine the shift of the Caesar Cypher

Created on Sat Feb  2 23:03:02 2019

@author: shakes
"""
from collections import Counter
import string

message =  "Pbqf xob qeb ybpq qefkdp fk qeb tloia"
#"Zyp cpxpxmpc ez wzzv fa le esp delcd lyo yze ozhy le jzfc qppe Ehz ypgpc rtgp fa hzcv Hzcv rtgpd jzf xplytyr lyo afcazdp lyo wtqp td pxaej hteszfe te Escpp tq jzf lcp wfnvj pyzfrs ez qtyo wzgp cpxpxmpc te td espcp lyo ozye esczh te lhlj Depaspy Slhvtyr"
# "Qefp fp x obxi tloia tfqe dlob xka xq qeb pxjb qfjb qexq f exsb ybba qlooba qeb obxi tloia fp qeb obxi tloia"
# "Pbqf xob qeb ybpq qefkdp fk qeb tloia"
# "Khoor zruog"

#frequency of each letter
letter_counts = Counter(message)
#print(letter_counts)

#find max letter
maxFreq = -1
maxLetter = None
for letter, freq in letter_counts.items():
    print(letter, ":", freq)
    #INSERT CODE TO REMEMBER MAX
    # idea here is, if empty skip, if freq bigger than maxFreq, set
    if letter != " ":
        if freq > maxFreq:
            maxFreq = freq
            maxLetter = letter
print("Max Ocurring Letter:", maxLetter)

#predict shift
letters = string.ascii_letters #contains 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
#assume max letter is 'e'
def shifter(maxLetter):
    shift = (ord(maxLetter) - 101) % 26
    print("Predicted Shift:", shift)
    return shift

shift = shifter(maxLetter)

totalLetters = 26
keys = {}
#part c, only work well with words have 'e'
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
