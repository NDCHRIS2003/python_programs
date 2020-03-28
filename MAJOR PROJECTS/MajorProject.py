# This program will assist in preparation of a pay slip to be included in
# a cheque envelope for the employees of a small business.The Pay Slip will also be used by the accountant to prepare
# the actual pay-cheques, and to record the deductions in a company ledger.
# input values will be asked by the user and after providing these values, a pay slip will be printed in an
# organized manner.

# The program was prepared by Ndubuisi Christopher Okpala
print("please provide the employee's details ")
# ask user for full name
first_name = input("What is the employee first name : ")
last_name = input("What is the employee last name : ")
# ask for employee number of hours worked weekly
hours_worked_weekly = float(
    input("What is the number hours worked by the employee : "))
# ask for employee hourly rate
hourly_of_pay = float(input("What is the employee hourly rate : "))
# whether the employee should have deductions removed from their gross pay (yes or no),
will_deduction_apply = input(f"Whether {first_name +' ' + last_name} "
                             f"should have deduction removed from gross pay ? (yes) or (no): ")
# introduce if condition to check if deduction will be applied
if will_deduction_apply == "yes":
    apply_deduction = True
else:
    apply_deduction = False
# calculate the applied deduction
if apply_deduction:
    percentage_of_deduction = int(
        input("what is the percentage of deduction?: "))/100
else:
    percentage_of_deduction = 0
# calculate the gross pay and over time of the employee
if hours_worked_weekly <= 40:
    regular_pay = hours_worked_weekly * hourly_of_pay
    over_time = 0
    gross_pay = regular_pay + over_time
else:
    over_time = hours_worked_weekly - 40
    gross_pay = over_time * 1.5 * hourly_of_pay + (40 * hourly_of_pay)
# calculate the dollar amount of deduction
dollar_amount_deducted = gross_pay * percentage_of_deduction
# calculate the net pay
net_pay = gross_pay - dollar_amount_deducted

# print the needed outs
print(" Below is the Employee's pay slip details")
print(f"Employee's name :             {first_name:}   {last_name:}")
print(f"Total hours worked :          {hours_worked_weekly:.2f}")
print(f"Over time hours :             {over_time:.2f}")
print(f"The hourly pay rate :         ${hourly_of_pay:.2f}")
print(f"Gross pay :                   ${gross_pay:,.2f}")
print(f"Deductions :                  ${dollar_amount_deducted:,.2f}")
print(f"Net pay :                     ${net_pay:,.2f}")

# Alternatively, The output can also be printed thus:
print(" Below is the Employee's pay slip details")
print("{:<30}{}, {}".format("Employee's name: ", first_name, last_name))
print("{:<30}{:.2f}".format("Total hours worked: ", hours_worked_weekly))
print("{:<30}{:.2f}".format("Over time hours: ", over_time))
print("{:<30}${:.2f}".format("The hourly pay rate: ", hourly_of_pay))
print("{:<30}${:,.2f}".format("Gross Pay: ", gross_pay))
print("{:<30}${:,.2f}".format("Deductions: ", dollar_amount_deducted))
print("{:<30}${:,.2f}".format("Net pay: ", net_pay))

