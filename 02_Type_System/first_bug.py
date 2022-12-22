"""
First Bug
---------

Undesired behavior in programming is called as `Bug`.

Python is a dynamically typed language so it's easy to introduce a bug.
"""

box = "balloons"
print(f"Box contains: {box}")

box = 10
print(f"Box contains: {box}")

# ---------------------------------------------------------------------------------
# Introducing `Type Hinting` - Optional Static Type Checking in Python Using `Mypy`
# ---------------------------------------------------------------------------------

food: str = "Milk"
print(f"Ashwin is going to drink: {food}")

food = "eggs"
print(f"Ashwin is going to drink: {food}")

food = False
print(f"Ashwin is going to drink: {food}")
