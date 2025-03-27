#################################
#       Marcell Placencia       #
#                               #
#           3/27/2025           #
#                               #
#    Employee Pay Calculator    #
#                               #
#################################

import time
import os
import platform

# Changes text color to green
os.system('color 02')

# Function to clear text regardless of OS (Windows uses "cls" and unix-based OS use "clear")
def clear_screen():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

clear_screen()

# Prompts the user asking for their name
print('----------------------')
name = str(input('   What is your name? - '))

clear_screen()

# Title for calculator
print('-------------------------')
print(' Employee Pay Calculator')
print('-------------------------')

time.sleep(.5)

# Welcomes the user
print(f'\n   Welcome {name}!')

time.sleep(1.5)
clear_screen()

# Prompts the user asking if they get paid weekly or bi-weekly
print('---------------------------------------------------------------------')
payFreq = int(input('   Type "1" you get paid weekly | Type "2" if you get paid bi-weekly - '))

while True:
    if payFreq == 1:
        biWeekly = False
        weekly = True
        break
    elif payFreq == 2:
        weekly = False
        biWeekly = True
        break
    else:
        clear_screen()
        print('---------------------------------------------------------------------')
        int(input('   ERROR!!! Please enter either "1" for weekly or "2" for bi-weekly - '))

clear_screen()

# Prompts the user asking for their hourly rate and stores it in the variable "hourlyRate" [datatype: float]
print('---------------------------------')
hourlyRate = float(input('   Please enter your hourly rate - $'))

clear_screen()

# Prompts the user asking how many hours they worked in a week or in two weeks
if biWeekly:
    print('----------------------------------------------------')
    hours = float(input('   How many hours did you work these two weeks? - '))
elif weekly:
    print('----------------------------------------------------')
    hours = float(input('   How many hours did you work this week? - '))
else:
    print('ERROR')

clear_screen()

# Calculates how much was made in the period
totalPay = hours * hourlyRate

# Prints the total pay in the pay period
print('--------------------------------------------')
print(f'   You have made ${totalPay} in this period!')
print('--------------------------------------------')
