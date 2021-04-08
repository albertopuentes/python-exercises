1.a.

while True:
    day_input = input('What day is it?')
    if day_input == 'Monday':
        print('Monday')
    else:
        print('Not Monday')

1.b. 

weekday = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

while True:
    day_input = input('What day is it?')
    if day_input in weekday:
        print('Weekday')
    else:
        print('Weekend')

1.c. 

hours_worked = 45
hourly_rate = 10

if hours_worked <= 40:
    weekly_pay = hours_worked * hourly_rate
else:
    weekly_pay = (40 * hourly_rate) + ((hours_worked - 40) * (1.5 * hourly_rate))
        
print(weekly_pay)