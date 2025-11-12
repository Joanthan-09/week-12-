# Objective:
# Students will learn how to compare values using Python’s comparison operators and interpret Boolean results.

# Topics Covered:
# ==, !=, >, <, >=, <=

# Key Notes:

# Comparison operators compare two values and return either True or False.

# Remember: = is assignment, while == is comparison.

a = 3
b = 4

print(a == b)   # False
print(a != b)   # True
print(a > b)    # False
print(a < b)    # True
print(a >= b)   # False
print(a <= b)   # True


#predict the output of the following comparisons:
10 > 5 # True 
7 == 2 * 3 + 1 # True 
8 != 8  # False
4 <= 2 + 2 #True


# Write 3 examples that result in True and 3 that result in False.

print(17 < 18)
print(9 == 3*3)
print(10 != 5)
print(10 == 1)
print(7 > 15)
print(8 != 8)


# Create a simple grade-checking condition:

# practice problem :
# where a student must check if their score is greater than or equal to 60 to pass a test.# The password must be at least 8 characters long and contain at least one digit.password = "mypassword1"


score = int(input("Enter your score: " ))
if score >= 60:
    print("you passed the test")
else:
    print("You did not pass the test.")

#password must be 8 characters long

    password = input("Enter your password: ")
    if len(password) >= 8 and any(char.isdigit() for char in password):
         print("password is valid")
    else:
        print("password is invalid")