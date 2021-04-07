
Data Types, Operators, and Variables Exercises

# movie rental exercise

mermaid_days = 3
hercules_days = 1
bbear_days = 5

price = 3
days_held = mermaid_days + hercules_days + bbear_days
total = days_held * price

print(days_held)
print(total)

# Contractor exercise
Google_Pay = 400
Amazon_Pay = 380
Facebook_Pay = 350

Google_hours_worked = 6
Amazon_hours_worked = 4
Facebook_hours_worked = 10

Weekly_Pay = (Google_Pay * Google_hours_worked) + (Amazon_Pay * Amazon_hours_worked) + (Facebook_Pay * Facebook_hours_worked)

print(Weekly_Pay)

# Enrollment Exercise (if statement is True then can enroll, if False then can't enroll)
class_not_full = True
no_conflict = True

enroll = class_not_full and no_conflict

# product (if statement True offer can be applied, if False offer can't be applied)

person_items = x
not_expired = True
premium_member = True
not_expirend = True

offer_person = person_items >= 2 and not_expired
offer_premium_member = premium_member and not_expired

offer_either = (person_items >= 2 and not_expired) or (premium_member and not_expired)

# Username and Password
username = 'codeup'
password = 'notastrongpassword'

pass_user = (len(password) >= 5)
pass_passwored = (len(username) <= 20)
in_conflict = (username != password)

print(pass_user, pass_password, in_conflict)




