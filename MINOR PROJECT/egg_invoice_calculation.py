# Date January 2020
# A simple program to calculate the Area of a Triangle
# Author = Ndubuisi Okpala

import time

# This will give the user the directive on how to use this program

print("This program is used to calcualte the amount to be paid by a customer for eggs purchased")
print("You will be asked to provide some parameters to be able to calculate the amount to be paid")
time.sleep(0.5)
print("Let's start: ")

# get the inputs from the customer and also validate it based on the number of the eggs the customer
# purchased to be able to output the correct bill for the customer

number_of_egg = float(input("number_of_egg : "))
if number_of_egg >= 0 and number_of_egg < 48:
    price = 0.50/12
    print(f"Your bill is $ {price* number_of_egg:.2f}")
elif number_of_egg >= 48 and number_of_egg < 72:
    price = 0.45/12
    print(f"Your bill is $ {price* number_of_egg:.2f}")
elif number_of_egg >= 72 and number_of_egg < 132:
    price = 0.40/12
    print(f"Your bill is $ {price* number_of_egg:.2f}")
else:
    price = 0.35/12
    print(f"Your bill is $ {price* number_of_egg:.2f}")
