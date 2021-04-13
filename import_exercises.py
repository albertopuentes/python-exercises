import function_exercises

 
print(function_exercises.is_vowel('a'))
print(function_exercises.apply_discount(100, .25))
print(function_exercises.remove_vowels('testme'))

from function_exercises import calculate_tip

print(calculate_tip(.15, 100))

from itertools import product
# 2.a.
print(len(list(product('abc', '123'))))

# 2.b.
from itertools import combinations
print(len(list(combinations('abcd', 2))))

#2.c. 
from itertools import permutations
print(len(list(permutations('abcd', 2))))

# 3

import json

json.load(open('profiles.json'))

profiles.listdir()

