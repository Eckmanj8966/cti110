# CTI-110
# P2HW2 - List
# Joshua Eckman
# 3/9/23
#

# Input
print('Enter grade for Module 1:', end=' ')
module1 = float(input())
print('Enter grade for Module 2:', end=' ')
module2 = float(input())
print('Enter grade for Module 3:', end=' ')
module3 = float(input())
print('Enter grade for Module 4:', end=' ')
module4 = float(input())
print('Enter grade for Module 5:', end=' ')
module5 = float(input())
print('Enter grade for Module 6:', end=' ')
module6 = float(input())

# List and Calculation
all_grades = [module1 ,module2 ,module3 ,module4 ,module5 ,module6]
average = sum(all_grades) / 6

# Output
print('')
print('------------Results------------')
print('Lowest Grade: \t', min(all_grades))
print('Highest Grade: \t', max(all_grades))
print('Sum of Grades: \t', sum(all_grades))
print('Average: \t', f'{average:.2f}')
print('-------------------------------')
