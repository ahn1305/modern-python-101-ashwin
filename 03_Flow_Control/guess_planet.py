"""
Friends from Earth 🌏 want to know were is Louis, so Louis decides to
write a program that will make his friends guess the name of planet.
"""

correct_guess: bool = False
guess: str = ""
planet: str = "Zortan"

# ----------------------------------------------------
# Alternative 1
# ----------------------------------------------------

while correct_guess is not True:
    guess = input("Louis Says: Can you guess my planet? >>> ")
    if guess.lower() == planet.lower():
        print("Right, louis is at zorton")
        correct_guess = True
    else:
        print("Wrong choice")


# ----------------------------------------------------
# Alternative 2
# ----------------------------------------------------

while True:
    guess = input("Louis Says: Can you guess my planet? >>> ")
    if guess.lower() == planet.lower():
        print("Right, louis is at zorton")
        break
    else:
        print("Wrong choice")
