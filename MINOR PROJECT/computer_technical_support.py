# Date January 2020
# A simple program to calculate the Area of a Triangle
# Author = Ndubuisi Okpala

import time

# This will give the user the directive on how to use this program

print("This program is used to confirm the extent of computer technical issues and direct the user on what to do")
print("You will be asked to provide some answers to questions")
time.sleep(0.5)
print("Let's start: ")

# To get the user's questions
Y = True
N = False
Does_the_computer_beep_when_powered_on = input(
    "Does_the_computer_beep_when_powered_on : ")
Does_the_drive_spin_when_powered_on = input(
    "Does_the_drive_spin_when_powered_on : ")

# Introducing the conditions so as to assist the user with the right directive.

if Does_the_computer_beep_when_powered_on == 'Y' and Does_the_drive_spin_when_powered_on == 'Y':
    print("Contact Tech Support")
elif Does_the_computer_beep_when_powered_on == 'Y' and Does_the_drive_spin_when_powered_on == 'N':
    print("Check drive cables")
elif Does_the_computer_beep_when_powered_on == 'N' and Does_the_drive_spin_when_powered_on == 'N':
    print("Bring computer to repair centre")
else:
    print("Check the speaker contacts")
