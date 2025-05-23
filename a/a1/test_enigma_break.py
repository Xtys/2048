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
# How long do you think it would’ve taken for a computer in the 1940s?!
# Answer: By scaling 11,772 attempts at 1 second per attempt = 11,772 seconds.
# Convert to hours: 11,772 / 3,600 ≈ 3.27 hours.


## part e, 3 rotors, additional 2 more rotor
# rotor = 5 * 4 * 3 = 60
# There are 60 ways you can put in 3 rotors from a choice of 5
# starting position of each rotors = 26 * 26 * 26 = 17,576

# plugboard = (26!/6! * 10! * 2^10) = 150 738 274 937 250

# total = 158 962 555 217 826 360 000
# tatal ways can set enigma machine

# it uses a cheat sheet

# Cracking time estimate on AMD Ryzen 7:
# Original attempts: 11,772, time: 10.77 seconds
# New configurations: 158,962,555,217,826,360,000 / 17,576 ≈ 9.04 * 10^15 times more
# New attempts (scaled): 11,772 * 9.04 * 10^15 ≈ 1.06 * 10^17 attempts
# Time per attempt: 10.77 / 11,772 ≈ 0.000915 seconds
# Total time: 1.06 * 10^17 * 0.000915 ≈ 9.7 * 10^13 seconds
# Convert to years: 9.7 * 10^13 / (365 * 24 * 60 * 60) ≈ 3,075 years
# Compared to 10.77 seconds, cracking would take approximately 3,075 years longer.
