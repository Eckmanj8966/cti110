# This program calculates travel expenses
# 2/16/2023
# CTI-110 P1HW2 - Travel Expense
# Joshua Eckman
#



budget = int(input('What is your current budget?: '))

location = input('What is your travel destination?: ')

gas = int(input('How much will you spend on gas?: '))

sleep = int(input('How much will you spend on accomodation?: '))

food = int(input('How much will you spend on food?: '))

# Add expenses
expenses = gas + sleep + food

# Subtract expenses from budget
remaining = budget - expenses

# Display results
print("\n------------Travel Expenses-----------")
print("Location:", "\t\t", location)
print("Initial Budget:", "\t", f'${budget:.1f}')
print("Fuel:", "\t\t\t", f'${gas:.1f}')
print("Accomadation:", "\t\t", f'${sleep:.1f}')
print("Food:", "\t\t\t", f'${food:.1f}')
print("--------------------------------------")
print("Remaining Balance:", "\t", f'${remaining:.1f}')
