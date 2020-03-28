# Date January 2020
# A simple program to calculate the Area of a Triangle
# Author = Ndubuisi Okpala

import time

# This will give the user the directive on how to use this program

print("This program is used to calcualte the Area of a triangle")
print("You will be asked to provide some parameters to be able to calculate the area")
time.sleep(0.5)
print("Let's start: ")

# ask for the correct base_of_triangle
base_of_triangle = float(input("base_cm : "))
while base_of_triangle <= 0:
    print(
        f"**Error - the base length must be a positive number. You entered {base_of_triangle}")
    base_of_triangle = float(input("Base : "))

# ask for the correct height_of_triangle
height_of_triangle = float(input("height_cm : "))
while height_of_triangle <= 0:
    print(
        f"**Error - the base length must be a positive number. You entered {height_of_triangle}")
    height_of_triangle = float(input("eight_cm : "))

# print the area of the triangle
area_of_triangle = 1/2 * base_of_triangle * height_of_triangle
print(f"area of triangle : {area_of_triangle}")
