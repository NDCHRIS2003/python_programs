# Date January 2020
# A simple program to calculate the Area of a Triangle
# Author = Ndubuisi Okpala

import time

# This will give the user the directive on how to use this program

print("This program is used to calcualte the Area of a triangle")
print("You will be asked to provide some parameters to be able to calculate the area")
time.sleep(0.5)
print("Let's start: ")

# Ask the user to provide the needed inouts

Base_in_cm = int(input("Base_in_cm : "))
Height_in_cm = int(input("Height_in_cm : "))
Area_of_Triangle_in_sq_m = 1/2 * Base_in_cm * Height_in_cm / 10000

# Introducing error validation and print area of triangle is the input is correct.

if Base_in_cm < 0:
    print(
        f"**Error - the base lenght must be a positive number. You entered {Base_in_cm}")
elif Height_in_cm < 0:
    print(
        f"** Error - the height must be a positive number. You entered {Height_in_cm}")
else:
    print(f"Area of Triangle square meter: {Area_of_Triangle_in_sq_m}")
