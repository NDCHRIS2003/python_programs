# Date January 2020
# A simple program to calculate the Area of a Triangle
# Author = Ndubuisi Okpala

import time

# This will give the user the directive on how to use this program

print("This program is used to calcualte compound interest")
print("You will be asked to provide some parameters to be able to calcualte compound interest")
time.sleep(0.5)
print("Let's start: ")

# ask the user the principal amount
principal = int(input("What is your principal amount invested ? : "))

# ask the user the interest rate for all the years
interest_rate_in_percent = float(
    input("What is the interest rate for year 1 (in percent) ? : "))/100

# state the initial compound interest
compound_interest = 1000

# set a loop condition
while (interest_rate_in_percent != 0):
    compound_interest = compound_interest * (1 + interest_rate_in_percent)
    interest_rate_in_percent = float(
        input("What is the interest rate for year 1 (in percent) ? : ")) / 100
average_yearly_income = (compound_interest - principal) / 3

# print the accumulated interest
print(f"At the end of 3 years, your investment will be worth ${compound_interest:.2f} "
      f"Your average yearly income is ${average_yearly_income:.2f}")
