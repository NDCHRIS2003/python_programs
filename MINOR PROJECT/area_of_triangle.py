# Date January 2020
# A simple program to calculate the Area of a Triangle
# Author = Ndubuisi Okpala

import time

# This will give the user the directive on how to use this program

print("This program is used to calcualte the Area of a triangle")
print("You will be asked to provide some parameters to be able to calculate the area")
time.sleep(0.5)
print("Let's start: ")

# to provide the needed inputs

Base = input("Base : ")
Height = input("Height : ")
Area_of_Triangle = 1/2 * int(Base) * int(Height) / 10000
print(format(Area_of_Triangle, '.2f'))

# Alternatively, it can be done like this below

Base = input("Base : ")
Height = input("Height : ")
Area_of_Triangle = 1/2 * int(Base) * int(Height) / 10000
print(f'{Area_of_Triangle:.2f}')
