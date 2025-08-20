print("Arean")
print("*" * 10)

x = 1

# students_count = 1000
# print (students_count)


students_count = 1000  # int
rating = 2.8  # float
id = 1j  # complex

# Strings in python

course = "Python Programming"
print(len(course))  # output 18
# positive index
print(course[0])  # output: p
# negative index
print(course[-1])  # output: g

print(course[:])  # output: Python Programming

print(course[0:])  # output: Python Programming

# escape character in python

bite = "Python \"Programming"

print(bite)  # output: Python "Programming

# Formatted strings in Python

first_Name = "Armaan"
last_Name = "Jamaan"
full_Name = first_Name + " " + last_Name

print(full_Name)  # output: Armaan jamaan

x = 5
y = 10
result = f"The sum of {x} and {y} is {x + y}."
print(result)  # output: The sum of 5 and 10 is 15.

# String Methods in python

My_Name = " Armaan jamaan"
print(My_Name.upper())  # output: ARMAAN JAMAAN
print(My_Name.lower())  # output: armaan jamaan
print(My_Name.title())  # output: Armaan Jamaan
print(My_Name.strip())  # output:Armaan Jamaan
# this for find index in py
print(My_Name.find("jam"))  # output: 8
# this for replace any string in py
print(My_Name.replace("a", "z"))  # output: Armzzn jzmzzn
# this return Boolean of find method
print("jam" in My_Name)  # output:True
print("red" not in My_Name)  # output:True

# Working with numbers
print(round(2.9))  # output:3
print(abs(-2.9))  # output:2.9

# conditional Statments in python
temperature = 35

# if temperature > 30:  # this is true
#     print("it's warm")
#     print("Drink water")
# elif temperature > 20:
#     print("it is nice")
# print("Done")

# Ternary Operaror
# age = 12
# message = "Eligible" if age >= 18 else "Not eligible"
# print(message)

# Logical Operators
# and
# or
# not

# high_income = True
# good_credit = True
# student = True

# if high_income and good_credit:
#     print("Eligible")
# else:
#     print("Not eligible")

# if high_income and good_credit and not student:
#     print("Eligi")

# for loops in python
# successful = True
# for number in range(3):
#     print("Attempt", number)  # output: 3 time "Attempt"

# for..Else
# successful = False
# for number in range(3):
#     print("Attempt", number)  # output: 3 time "Attempt"
#     if successful:
#         print("Sucessful")
#         break
# else:
#     print("Attempted 3")

# # Nested Loops

# for x in range(5):
#     for y in range(3):
#         print(f"{x},{y}")

# Iterable
# for x in "Python":
#     print(x)

# while Loops

# number = 100
# while number > 0:
#     print(number)
#     number //= 2

# Infinite Loops
    # while True:
    #     command = input(">")
    #     print("ECHO", command)
    #     if command.lower() == "quit":
    #         break

# # function
def greet(first_name, last_name):
    print(f"Hi {first_name} {last_name}")
    print("Welcome aboard")


greet("Armaan", "Jamaan")

# type of function in Python
# 1- perform a task
greet("Armaan", "Jamaan")
# 2- Return a value

