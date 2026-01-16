'''
script: heart_rate_calculator.py
action: a. request user input for age.
        b. perform max heart rate calculation.
        c. perform target min & max heart rate calculation.
        c. print range of target heart rate.
author: John Pinto
date: 1/16/2026
'''

age = int(input("What is your age?: "))
max_rate = 220 - age
tgt_min_rate = max_rate * .50
tgt_max_rate = max_rate * .85
target_rate = print(f"Your target heart rate range is {tgt_min_rate} - {tgt_max_rate}.")
