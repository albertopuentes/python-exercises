# 1.a.


    day_input = input('What day is it?')
    if day_input.lower() == 'monday':
        print('Monday')
    else:
        print('Not Monday')

# 1.b. 

weekday = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday']

day_input = input('What day is it?')
if day_input.lower() in weekday:
    print('Weekday')
else:
    print('Weekend')

# 1.c. 

hours_worked = 45
hourly_rate = 10

if hours_worked <= 40:
    weekly_pay = hours_worked * hourly_rate
else:
    weekly_pay = (40 * hourly_rate) + ((hours_worked - 40) * (1.5 * hourly_rate))
        
print(weekly_pay)


# 2.a.

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


# 2.b

num_input = input('Give me a positive number')
for n in range(1, 11):
    print(f'{int(num_input)} X {n} = {int(num_input) * n}')

for n in range (1,10):
    print(str(n) * n)

# 2.c

for n in range(1,51,2):
    num_input = input('Please enter an odd number between 1 and 50')
    if n % 2 == 1:
        continue
    print(f'Here is an odd number: {n}')

    num_input = input('Please enter an odd number between 1 and 50')
for num in range(1, 51, 2):
    if num == int(num_input):
        print(f'Yikes! Skipping number: {num}')
    else:
        print(f'Here is an odd number: {num}')

    
num_input = input('Please enter a positive number')
while num_input.isdigit() and int(num_input) > 0:
    for n in range (0, (int(num_input)+1)):
        if n <= int(num_input):
            print(n)
    else: break

# 2.d.

num_input = input('Please enter a positive number')
while num_input.isdigit() and int(num_input) > 0:
    n = int(num_input)
    for n in range(int(num_input), 1)
        while n >= 1
        n += -1
           
#2.e.

num_input = input('Please enter a positive number')
if num_input.isdigit() and int(num_input) > 0:
    n = int(num_input)
    while n >= 1:
        print(n)
        n += -1

# 3.  FizzBuzz

for n in range (1, 101, 1):
    if n % 3 == 0: 
        print("Fizz") 
    if n % 5 == 0: 
        print("Buzz") 
    if n % 5 == 0 and n % 3 == 0: 
        print("FizzBuzz") 
    else: 
        print(n)

# 5
while True:
    grade_inp = input("Please enter a grade from 0 to 100")
    if int(grade_inp) > 87:
        print('A')
    elif int(grade_inp) > 79 and int(grade_inp) < 88:
        print('B')
    elif int(grade_inp) > 66 and int(grade_inp) < 80:
        print('C')
    elif int(grade_inp) > 59 and int(grade_inp) < 60:
        print('D')
    else:
        print('F')
    cont_input = input("Would you like to continue?  Enter Y or N")
    if cont_input.lower() != "y": 
        break  

# 6