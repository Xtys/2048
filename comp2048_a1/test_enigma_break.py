# -*- coding: utf-8 -*-
"""
Create and test an Enigma machine encryption and decoding machine

This code is based on the implementation of the Enigma machine in Python
called pyEnigma by Christophe Goessen (initial author) and Cédric Bonhomme
https://github.com/cedricbonhomme/pyEnigma

Created on Tue Feb  5 12:17:02 2019

@author: uqscha22
"""
import string
import enigma
import rotor
import time

letters = string.ascii_letters #contains 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
capitalLetters = letters[-26:]
#print(capitalLetters)

ShakesHorribleMessage = "Xm xti ca idjmq Ecokta Rkhoxuu! Kdiu gm xex oft uz yjwenv qik parwc hs emrvm sfzu qnwfg. Gvgt vz vih rlt ly cnvpym xtq sgfvk jp jatrl irzru oubjo odp uso nsty jm gfp lkwrx pliv ojfo rl rylm isn aueuom! Gdwm Qopjmw!"
crib = "Hail Shakes!"
crib_substring = ""
print(crib_substring)

##Break the code via brute force search

def shakes_enigma(ShakesHorribleMessage, crib, crib_substring):

    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    #initialize counter
    counter = 0

    if not crib_substring:
        target = crib
    else:
        target = crib_substring


    for rotor1 in alphabet:
        for rotor2 in alphabet:
            for rotor3 in alphabet:
                key = f"{rotor1}{rotor2}{rotor3}"
                #part d, counter
                counter += 1
                engine = enigma.Enigma(
                    rotor.ROTOR_Reflector_A,
                    rotor.ROTOR_I,
                    rotor.ROTOR_II,
                    rotor.ROTOR_III,
                    key=key,
                    plugs="AA BB CC DD EE"
                )

#Print the Decoded message
                decrypted = engine.encipher(ShakesHorribleMessage)

                if target in decrypted:
                    print(f"Found key: {key}")
                    print(f"Decrypted message: {decrypted}")
                    print(f"Attempts: {counter}")
                    #else increase counter, by the process of elimination
                    if crib_substring and crib in decrypted:
                        print(f"Full crib '{crib}' also matches!")
                    return key, decrypted

    # print("No key found with this rotor setup.")
    return None, None

#part d,  add timer
start_time = time.time()

key, decrypted = shakes_enigma(ShakesHorribleMessage, crib, crib_substring)

end_time = time.time()

duration = end_time - start_time

print(f"Brute force attack completed in {round(duration,2)} seconds on AMD ryzen 7")


#part e, 5 rotors
# def shakes_enigma_upgrade(ShakesHorribleMessage, crib, crib_substring):

#     alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

#     #initialize counter
#     counter = 0

#     if not crib_substring:
#         target = crib
#     else:
#         target = crib_substring


#     for rotor1 in alphabet:
#         for rotor2 in alphabet:
#             for rotor3 in alphabet:
#                 for rotor4 in alphabet:
#                     for rotor5 in alphabet:
#                         key = f"{rotor1}{rotor2}{rotor3}{rotor4}{rotor5}"

#                         #part d, counter
#                         counter += 1
#                         engine = enigma.Enigma(
#                             rotor.ROTOR_Reflector_A,
#                             rotor.ROTOR_I,
#                             rotor.ROTOR_II,
#                             rotor.ROTOR_III,
#                             rotor.ROTOR_IV,
#                             rotor.ROTOR_V,
#                             key=key,
#                             plugs="AA BB CC DD EE"
#                         )
#                 #Print the Decoded message
#                         decrypted = engine.encipher(ShakesHorribleMessage)

#                         if target in decrypted:
#                             print(f"Found key: {key}")
#                             print(f"Decrypted message: {decrypted}")
#                             print(counter)
#                                     #else increase counter, by the process of elimination
#                                     # If crib_substring was used, also check full crib
#                             if crib_substring and crib in decrypted:
#                                 print(f"Full crib '{crib}' also matches!")
#                                 return decrypted

#     print("No key found with this rotor setup.")
#     return None, None

# #part d,  add timer
# start = time.time()

# key, decrypted = shakes_enigma_upgrade(ShakesHorribleMessage, crib, crib_substring)

# end= time.time()

# duration2 = end - start

# print(f"Brute force attack completed in {round(duration2,2)} seconds on AMD ryzen 7")
