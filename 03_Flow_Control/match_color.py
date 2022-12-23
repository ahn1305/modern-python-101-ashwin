"""
While traveling to Zortan, Louis packed lots of stuff. Let's
see if he has anything that matches your favorite color.

INFO -
------

`match` is a new operator introduced in Python 3.10
"""

color = input("Enter the name of the color >>> ").title()

match color:
    case "Red":
        print("louis has a red car")
    case "Blue":
        print("louis has a blue car")

    case "yellow":
        print("louis has a yellow car")
    case _:
        print(" the input color didn't match")
