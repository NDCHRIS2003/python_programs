# Date January 2020
# A simple program to calculate the Area of a Triangle
# Author = Ndubuisi Okpala

import time

# This will give the user the directive on how to use this program

print("This program is used to calcualte the a compound interest")
print("You will be asked to provide some parameters to be able to calculate the compound interest")
time.sleep(0.5)
print("Let's start: ")

# ask for values for principal
principal = int(input("principal amount : "))

# ask for value of interest in percentage
interest_percent = float(input("interest in percentage : ")) / 100

# ask for value of year
year = int(input("year of investement : "))

# introduce a count
counter = 0

# print output in an organized manner
print("Year", "    ", "Balance")
while (counter < year):
    principal = principal * (1 + interest_percent)

    print(counter, "      ", "{:.2f}".format(principal))
    counter += 1
