'''
script: pinto_heart_rate_calculator.py
action: a. request user input for their age.
        b. perform max heart rate calculation.
        c. print maximum heart rate.
        d. perform target min & max heart rate calculation.
        e. print range of target heart rate.
author: John Pinto
date: 1/19/2026
'''

print("Welcome to the heart rate calculator!\n")

age = int(input("What is your age?: "))
max_rate = 220 - age
print(f"\nThe maximum heart rate based on your age is: {max_rate} BPM")

tgt_min_rate = int(max_rate * .50)
tgt_max_rate = int(max_rate * .85)
print(f"Your target heart rate range is {tgt_min_rate} - {tgt_max_rate} BPM.")
