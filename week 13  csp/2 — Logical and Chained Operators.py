# Objective:
# Students will use logical (and, or, not) and chained comparison operators in Python to build compound conditions.

# Key Notes:

# and → Both conditions must be True

# or → At least one condition must be True

# not → Inverts True/False

# You can chain comparisons: 1 < x < 5

# Examples:
x = 10
print(x > 5 and x < 15)   # True
print(x < 5 or x == 10)   # True
print(not(x == 10))       # False
print(1 < x < 20)         # True

#score calculator
score = int(input("Enter your score (0-100): "))
# if score is between 90 & 100
# assign grade A
if score >= 90 and score <= 100:
    print("Grade: A")
elif score >= 80 and score < 90:
    print("Grade: B")
elif score >= 70 and score < 80:
    print("Grade: C")
if score >= 60 and score < 70:
    print("Grade: D")
elif score < 60:
    print("Grade: F")  



# Practice Problems:

# Write an expression that checks if a number is between 50 and 100 (inclusive).
number = int(input("Enter a number: "))
if 50 <= number <= 100:
    print(f"{number}  Is between 50 & 100")
else:
    print(f"{number}  Is not between 50 & 100")


# Write an expression that checks if a number is NOT equal to 0 and greater than 10.
y = int(input("Enter another number:"))
print( y != 0 and y > 10)
# Use chained comparison to check if 3 < 4 < 5.
print(3<4>5)
# Challenge: Create a password rule using logical operators:

