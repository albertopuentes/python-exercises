1.a.


    day_input = input('What day is it?')
    if day_input.lower() == 'monday':
        print('Monday')
    else:
        print('Not Monday')

1.b. 

weekday = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday']

day_input = input('What day is it?')
if day_input.lower() in weekday:
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


2.a.

i = 5
while i <= 15:
    print(i)
    i += 1

i = 0
while i <= 100:
    print(i)
    i += 2

    i = 100
while i <= -10:
    print(i)
    i += -5

while i <= -10:
    print(i)
    i += -5

    i = 2
while i <= 1000000:
    print(i)
    i **= 2 

i = 100
while i >= 5:
    print(i)
    i += -5


2.b

num_input = input('Give me a positive number')
for n in range(1, 11):
    print(f'{int(num_input)} X {n} = {int(num_input) * n}')

for n in range (1,10):
    print(str(n) * n)

num_input = input('Give me an odd number between 1 and 50')
while:
    number_input 