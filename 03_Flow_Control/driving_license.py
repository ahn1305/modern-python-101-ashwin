"""
Ashwin wants to drive a car 🚙 and wants to know if he can
apply for a driving license or not.
"""

# ----------------------------------------------------
# If / Else Statement
# If condition true prints whatever inside the if block and skip else part, if false vice-versa
# ----------------------------------------------------


age: int = 13


if age < 16:
    print("You are not eligible for a license")
else:
    print("You are eligible for license")

# ----------------------------------------------------
# After couple of years
# ----------------------------------------------------

if age < 16:
    print("You are not eligible for a license")
else:
    print("You are eligible for license")

# ----------------------------------------------------
# Alternative Implementation - Without `Else` block
# ----------------------------------------------------

age = 19

if age < 16:
    print("You are not eligible for a license")

print("You are eligible for a license")

# ----------------------------------------------------
# After too many years
# ----------------------------------------------------

age = 100

if age < 16:
    print("You are not eligible for a license")
elif age >= 100:
    print("You are too old to get a license")
else:
    print("You are eligible for license")
