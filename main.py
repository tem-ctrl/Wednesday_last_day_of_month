import numpy as np
import calendar as cal
from datetime import datetime as dt

# total number of 21 stcentury Wednesdays
Weds = np.busday_count('2001', '2101', weekmask = 'Wed')

# Number of Wednesdays falling on the last day of the month
Wed_end = 0 # Initialization
months = range(1,13) # Number of months in the year:13 − 1 = 12

for year in range(2001, 2101):
    for month in months:
        mr = cal.monthrange(year, month) # Length of the month
        if dt(year, month, mr[1]).weekday() == 2: # The days of the
            Wed_end += 1 # week range from 0 to 6
           
Percent_Wed = (Wed_end/Weds)*100

print(f'Number of Wednasdays ending months : {Wed_end}')
print(f'Total number of Wednesdays in the 21st Century : {Weds}')
print(f'Percentage Wednesdays ending months : {Percent_Wed:.2f}')
