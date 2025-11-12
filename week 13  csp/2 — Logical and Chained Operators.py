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
if 90 <= score >=100:
    print("Grade: A")
#if score is between 80 & 89
# Assign grade b
elif 80<= score >= 90:
    print("Grade: B")
# if socre is between 70 & 79
# assign grade C
elif 70<= score >= 80:
    print("Grade: C ")
#if score is between 60 & 69
#assign Grade D
elif 60<= score >= 70:
    print("Grade: C ")
# if score is below 60
#Assign Grade F
else:
    print("Grade: F ")



















# Practice Problems:

# Write an expression that checks if a number is between 50 and 100 (inclusive).

# Write an expression that checks if a number is NOT equal to 0 and greater than 10.

# Use chained comparison to check if 3 < 4 < 5.

# Challenge: Create a password rule using logical operators:

