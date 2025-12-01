# Objective:
# Students will manipulate nested lists and understand basic list comprehensions.

list1= [1, 2, 3]
list2 = [4, 5, 6]
nested_list = [list1, list2]
print(nested_list)         # output: [[1, 2, 3], [4, 5, 6]]
print(nested_list[1][2]) # output 6 

fruit = ["apples", "orange", "banana", "coconut"]
vegi = ["celery","carrots", "potatoes"]
meats = ["chciken", " fish", "turkey"]

groceries = [fruit, vegi, meats]   # fruit [0] vegi[1] meats[2]

print(groceries[0][2]) # Banana

# for collection in groceries:     # ["apples", "orange", "banana", "coconut"] ["celery","carrots", "potatoes"] ["chciken", " fish", "turkey"]
#     print(collection)


# num_pad = ((1, 2, 3),
# (4, 5, 6),
# (7, 8, 9),)
# ("*", 0, "#")

# for row in num_pad:
#     for num in row:
#         print(num, end=" ")
#         print()
        




# Key Notes:

# A list can contain other lists.

# List comprehensions provide a concise way to create lists.
 
# Examples:Objective:
# Students will manipulate nested lists and understand basic list comprehensions.

# Key Notes:

# A list can contain other lists.

# List comprehensions provide a concise way to create lists.

# Examples:

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix[0][2])    # 3

# List comprehension
first_col = [row[0] for row in matrix]
print(first_col)       # [1, 4, 7]




# Practice Problems:

# Build a matrix variable containing 3 lists of 3 numbers each.

mx = [
    [5, 10, 15],
    [20, 25, 30],
    [35, 40, 45],
]



# Print the first list.
print(mx)

# Print the second item from the third list.
print(mx[1][2])

# Use a list comprehension to extract the last item from each sub-list.
mx_col = [row[0] for row in mx]
print(mx_col)       

# Challenge: Create a new list containing squares of numbers from 1–10 using a comprehension.


squared_numbers = [x**2 for x in range(1,11)]
#for x in range (1,11)
# squared= x**2
# print(squared)

print(squared_numbers)