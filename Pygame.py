import random
import sys

def guess_a_number(_endval):
    choice = input("Hello, Gamer ! Do you wanna play this awesome number guessing game ? enter Y for YES and N for NO ")
    choice = choice.lower()
    if choice == "y" or "Y":
        print("Welcome")
        val = 0
        correct_val = random.randint(1, _endval)
        print(f"Guess the number between 1 to {_endval} >> ")
        while val != correct_val:
            val = int(input())
            if val > correct_val:
                print("Out of range!")
            elif val < correct_val:
                print("to low")
        print(f"Congrats You Guessed The Correct Number Which is {correct_val}")
    else:
        sys.exit()

_endval = random.randint(1, 50)
guess_a_number(_endval)
        
