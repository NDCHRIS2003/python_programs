# Feb 5th 2020
# Assignment = Prepare Pay Slip based on information entered
# __author__ = Ndubuisi Okpala

import time

# show some basic discription of the program
print("This program is used calcute the Pay Slip for a employee")
print("You will be asked a series of questions, please answer acoordingly.",
      "\n", "After you answered all questions, a proper Pay Slip will be generated")
time.sleep(0.5)
print("Let's start: ")


# get the first and last name of the employee
firstName = input("What is the First Name of the employee?: ")
lastName = input("What is the Last Nmae of the employee?: ")

# get the number of hours worked
hrWorked = float(input(
    "Please enter the number of hours '{} {}' worked over the week: ".format(firstName, lastName)))

# get the hourly payment rate
hrPayRate = float(input(
    "Please enter the hourly pay rate for '{} {}': ".format(firstName, lastName)))

# get from operator whether there is any need to deduction
deduction = input("Whether '{} {}' should have any deduction removed from gross pay? (yes or no): ".format(
    firstName, lastName))
if deduction == "yes":
    haveDeduction = True
else:
    haveDeduction = False

# get from operator the percentage need to deduct from gross pay
if haveDeduction:
    deducPer = int(input(
        "Please enter the percentage of deduction from Gross Pay (whole number):  "))
else:
    deducPer = 0

# inform operator all info is entered and wait for result
print("You have entered all the information, please wait...")
time.sleep(1)

# calculate grosspay and overtime on all information entered
if hrWorked <= 40:
    grossPay = hrWorked * hrPayRate
    overTime = 0
else:
    overTime = hrWorked - 40
    grossPay = 40 * hrPayRate + overTime * 1.5 * hrPayRate

# calculate the deduction amount and netpay
amountDeduction = grossPay * deducPer / 100
netPay = grossPay - amountDeduction


# export all the information and calculated result
print("Pay Slip Results: ")
print("{:<22}{}, {}".format("Employee Name: ", firstName, lastName))
print("{:<22}{:.2f}".format("Total Hours Worked: ", hrWorked))
print("{:<22}{:.2f}".format("Overtime Hours: ", overTime))
print("{:<22}${:.2f}".format("Hourly Pay Rate: ", hrPayRate))
print("{:<22}${:,.2f}".format("Gross Pay: ", grossPay))
print("{:<22}${:,.2f}".format("Deductions: ", amountDeduction))
print("{:<22}${:,.2f}".format("Net Pay: ", netPay))

