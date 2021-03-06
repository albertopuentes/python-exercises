# 1

def is_two(x):
    if x == 2 or x == '2':
        return True
    else:
        return False
print(is_two(4))
# 2

def is_vowel(x):
    if x in 'aeiouAEIOU':
        return True
    else: 
        return False
print(is_vowel(b))

# 3 

def is_vowel(x):
    if x not in 'aeiouAEIOU':
        return True
    else: 
        return False

# 4

def cap_word(x):
    if x[0] not in 'aeiouAEIOU':
        x = x.capitalize()
    return(x)

cap_word('today')

# 5

def calculate_tip(tip, bill):
    return tip*bill

# 6

def apply_discount(price, discount):
    return price-(price*discount)

# 7

def handle_commas(n):
    n = n.replace(',', '')
    return int(n)


# 8
def get_letter_grade(x):
    if x > 89:
        return 'A'
    elif x > 79:
        return 'B'
    elif x > 74:
        return 'C'
    elif x > 69:
        return 'D'
    else:
        return 'F'

get_letter_grade(55)

# 9

def remove_vowels(n):
    vowel = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    for x in n:
        if x in vowel:
            n = n.replace(x, "")
    return n

# 10

def normalize_name(x):
    x = x.lower()
    x = x.strip()
    x = x.replace(" ", "_")
    for y in x:
        if y.isalnum() == False and y != "_":
            x = x.replace(y, "")
    while x[0].isdigit() and x[0] != "_":
        x = x[1:]
    return x
# 11 

def cumulative_sum(x):
    x = [sum(x[:i]) for i in range(1, len(x)+1)]
    return x



    