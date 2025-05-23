import string
from collections import Counter

code_to_break = "19 17 17 19 14  20 23 18 19 8  12 16 19 8 3  21 8 25 18 14  18 6 3 18 8  15 18 22 18 11"

numbers = [int(num) for num in code_to_break.split()]

num_counter = Counter(numbers)

#find max letter
maxFreq = -1
maxLetter = None
for num, freq in num_counter.items():
    print(num, ":", freq)
    if num != " ":
        if freq > maxFreq:
            maxFreq = freq
            maxLetter = num
print("Max Ocurring Letter:", maxLetter)

#since number contain 3 to 25 and not '1 to 26' not all alphabet are mapped
#we have 19 (4), 17 (2), 14 (2), 8 (4), 3 (2)
# 1 time use =  6,7,9,11,12,15,16,20,21,22,23,25

# using most occururs common letters in English
# E = 11.1607% = 18
# A – 8.4966% = 19
# R – 7.5809% = 8
message = "A 17 17 A 14  20 23 E A 8  12 16 A 8 3  21 8 25 E 14  E 6 3 E 8  15 E 22 E 11"
message = "A 17 17 A 14  20 23EAR  12 16 AR 3  21 R 25 E 14  E 6 3 E R  15 E 22 E 11"

# I – 7.5448% = 17, try O – 7.1635%
message = "AIIA 14  20 23EAR  12 16 AR 3  21 R 25 E 14  E 6 3 E R  15 E 22 E 11"
message = "AOOA 14  20 23EAR  12 16 AR 3  21 R 25 E 14  E 6 3 E R  15 E 22 E 11"
# AIIA and AOOA we dont have this in english

# T – 6.9509% _ 17
# try "attack", so let N = C = 14
# C – 4.5388% = 14
# let k be 20
message = "ATTACK 23EAR  12 16AR 3 21R 25 ECE 6 3 ER  15 E 22 E 11"

# let P be 23
    # I – 7.5448% -
    # O – 7.1635% _
    # N – 6.6544% _
    # S – 5.7351%
    # L – 5.4893%
# sub all remaining letters to position 12
# Thus, L – 5.4893% = 12
message = "ATTACK PEARL 16AR 3 21R 25 ECE 6 3 ER  15 E 22 E 11"

# remaining:
    # I – 7.5448% -
    # O – 7.1635% _
    # N – 6.6544% _
    # S – 5.7351%

# message = "ATTACK PEARL 16AR 3 21R 25 ECE 6 3 ER  15 E 22 E 11"
# since attack pearl should follow 'harbor' = '16 A R 3 21 R'
# thus 16 = H, 3 = B , 21 = O, 'H A R B O R' matched
# message = "ATTACK PEARL HARBOR 25ECE6BER  15E22E11"

# '25ECE6BER' = december , '15E22E11' = seven
# since all the remaining number only map to one letter.
# message = "ATTACK PEARL HARBOR DECEMBER SEVEN"
