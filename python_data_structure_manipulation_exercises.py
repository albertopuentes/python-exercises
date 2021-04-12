students = [
    {
        "id": "100001",
        "student": "Ada Lovelace",
        "coffee_preference": "light",
        "course": "web development",
        "grades": [70, 91, 82, 71],
        "pets": [{"species": "horse", "age": 8}],
    },
    {
        "id": "100002",
        "student": "Thomas Bayes",
        "coffee_preference": "medium",
        "course": "data science",
        "grades": [75, 73, 86, 100],
        "pets": [],
    },
    {
        "id": "100003",
        "student": "Marie Curie",
        "coffee_preference": "light",
        "course": "web development",
        "grades": [70, 89, 69, 65],
        "pets": [{"species": "cat", "age": 0}],
    },
    {
        "id": "100004",
        "student": "Grace Hopper",
        "coffee_preference": "dark",
        "course": "data science",
        "grades": [73, 66, 83, 92],
        "pets": [{"species": "dog", "age": 4}, {"species": "cat", "age": 4}],
    },
    {
        "id": "100005",
        "student": "Alan Turing",
        "coffee_preference": "dark",
        "course": "web development",
        "grades": [78, 98, 85, 65],
        "pets": [
            {"species": "horse", "age": 6},
            {"species": "horse", "age": 7},
            {"species": "dog", "age": 5},
        ],
    },
    {
        "id": "100006",
        "student": "Rosalind Franklin",
        "coffee_preference": "dark",
        "course": "data science",
        "grades": [76, 70, 96, 81],
        "pets": [],
    },
    {
        "id": "100007",
        "student": "Elizabeth Blackwell",
        "coffee_preference": "dark",
        "course": "web development",
        "grades": [69, 94, 89, 86],
        "pets": [{"species": "cat", "age": 10}],
    },
    {
        "id": "100008",
        "student": "Rene Descartes",
        "coffee_preference": "medium",
        "course": "data science",
        "grades": [87, 79, 90, 99],
        "pets": [{"species": "cat", "age": 10}, {"species": "cat", "age": 8}],
    },
    {
        "id": "100009",
        "student": "Ahmed Zewail",
        "coffee_preference": "medium",
        "course": "data science",
        "grades": [74, 99, 93, 89],
        "pets": [{"species": "cat", "age": 0}, {"species": "cat", "age": 0}],
    },
    {
        "id": "100010",
        "student": "Chien-Shiung Wu",
        "coffee_preference": "medium",
        "course": "web development",
        "grades": [82, 92, 91, 65],
        "pets": [{"species": "cat", "age": 8}],
    },
    {
        "id": "100011",
        "student": "William Sanford Nye",
        "coffee_preference": "dark",
        "course": "data science",
        "grades": [70, 92, 65, 99],
        "pets": [{"species": "cat", "age": 8}, {"species": "cat", "age": 5}],
    },
    {
        "id": "100012",
        "student": "Carl Sagan",
        "coffee_preference": "medium",
        "course": "data science",
        "grades": [100, 86, 91, 87],
        "pets": [{"species": "cat", "age": 10}],
    },
    {
        "id": "100013",
        "student": "Jane Goodall",
        "coffee_preference": "light",
        "course": "web development",
        "grades": [80, 70, 68, 98],
        "pets": [{"species": "horse", "age": 4}],
    },
    {
        "id": "100014",
        "student": "Richard Feynman",
        "coffee_preference": "medium",
        "course": "web development",
        "grades": [73, 99, 86, 98],
        "pets": [{"species": "dog", "age": 6}],
    },
]

# 1) 14 students
print(len(students))

# 2)3 students prefer light roast
# 6 students prefer medium roast
# 5 students prefer dark roast
count_light = 0
count_medium = 0
count_dark = 0
for n in students:
    if n["coffee_preference"] == 'light':
       count_light += 1
    if n["coffee_preference"] == 'medium':
       count_medium += 1 
    if n["coffee_preference"] == 'dark':
       count_dark += 1 

print(f'{count_light} students prefer light roast')
print(f'{count_medium} students prefer medium roast')
print(f'{count_dark} students prefer dark roast')

#4) All students received 4 grades [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4]
num_of_grades = [len(x['grades']) for x in students]
print(num_of_grades)

#5) [78.5, 83.5, 73.25, 78.5, 81.5, 80.75, 84.5, 88.75, 88.75, 82.5, 81.5, 91.0, 79.0, 89.0]
# average grade for each student

grade_sum = [sum(x['grades']) for x in students]
grade_len = [len(x['grades']) for x in students]
grade_avg = [x / y for x, y in zip(grade_sum, grade_len)]
print(grade_avg)

#6) [1, 0, 1, 2, 3, 0, 1, 2, 2, 1, 2, 1, 1, 1] is list of number of pets each student has
student_pets = [len(x['pets']) for x in students]
print(student_pets)

#7) 7 students in the data science course & 7 students in the web development course
ds_count = 0
wd_count = 0
for n in students:
    if n["course"] == 'data science':
        ds_count += 1
    if n["course"] == 'web development':
        wd_count += 1
    
print(f'{ds_count} of students in data science')
print(f'{wd_count} of students in web development')

#8) 1.2857142857142858 is average number of pets for students in web development
web_pets = []
for n in students:
    if n["course"] == 'web development':
        web_pets.append(len(n['pets'])) 

x = sum(web_pets)/len(web_pets)
print(x)

#9) 5.444444444444445 is avg pet age for data science students
pet_ages = []
for n in students:
    if n["course"] == "data science":
        for n in n["pets"]:
            pet_ages.append(n["age"])
                    
print(sum(pet_ages)/len(pet_ages))

# 10) the most frequent coffee preference for data science students is medium @ 4
count_light = 0
count_medium = 0
count_dark = 0
for n in students:
    if n["course"] == 'data science':
        if n["coffee_preference"] == 'light':
           count_light += 1
        if n["coffee_preference"] == 'medium':
           count_medium += 1 
        if n["coffee_preference"] == 'dark':
           count_dark += 1 

print(f'{count_light} data science students prefer light roast')
print(f'{count_medium} data science students prefer medium roast')
print(f'{count_dark} data science students prefer dark roast')

# 11) the least frequent coffee preference for web dev students are medium & dark @ 2
count_light = 0
count_medium = 0
count_dark = 0
for n in students:
    if n["course"] == 'web development':
        if n["coffee_preference"] == 'light':
           count_light += 1
        if n["coffee_preference"] == 'medium':
           count_medium += 1 
        if n["coffee_preference"] == 'dark':
           count_dark += 1 

print(f'{count_light} web development students prefer light roast')
print(f'{count_medium} web development students prefer medium roast')
print(f'{count_dark} web development students prefer dark roast')

#12 the avg grade for students w/at least 2 pets is 83.8

grades_2pets = []
for n in students:
    if len(n["pets"]) >= 2:
        grades_2pets.append((sum(n["grades"]))/(len(n["grades"])))

print(grades_2pets)
print(len(grades_2pets))
print(sum(grades_2pets)/len(grades_2pets))

#13 1 student has 3 pets
count = 0
for n in students:
    if len(n["pets"]) == 3:
        count += 1

print(count)

#14 The avg grade for students w/0 pets is 82.125
grades_2pets = []
for n in students:
    if len(n["pets"]) == 0:
        grades_2pets.append((sum(n["grades"]))/(len(n["grades"])))

print(grades_2pets)
print(len(grades_2pets))
print(sum(grades_2pets)/len(grades_2pets))
