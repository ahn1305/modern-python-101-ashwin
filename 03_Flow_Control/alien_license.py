"""
Louis wants to drive a car 🚙 and he hears that in planet
Zortan 🪐 there is no age limit for getting a license.

`AND` Table
------------
True and True => True
False and False => False
True and False => False
False and True => False

in 'AND' both the conditions must be true in order to execute the associated block.

`OR` Table
----------
True or True => True
False or False => False
True or False => True
False or True => True

in 'OR' if any one condition is satisfied then the block associated with it will be executed.
"""

age: int = 13
planet: str = "Earth"

# ----------------------------------------------------
# And / Or Statement
# ----------------------------------------------------


if age < 16 and planet == "Earth":
    # here in the above lines both the conditions are true so it will execute the
    # block that is associated with it
    print("you are not eligible to get a license on Earth")
    # ------------------------------------------------------------------------------
elif age > 16 and planet == "Earth":
    # here the first condition is false but the second condition is true the block associated
    # with it fails to execute
    print("you are eligible to get a license on earth")
    # ------------------------------------------------------------------------------
elif age < 16 or planet == "Zortan":
    # here both first true, false
    print("You are eligible to get a zotranian license.")
    # ------------------------------------------------------------------------------
