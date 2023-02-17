year = int(input('enter a year: '))
if (year % 4 == 0 and year % 100 != 0) or (year % 4 == 0 and year % 100 == 0 and year % 400 == 0):
    print(f'The year {year} is a leap year.')
else:
    print(f'The year {year} is not leap year.')
    
