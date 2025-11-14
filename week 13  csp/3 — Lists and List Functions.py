# Objective:
# Students will understand how to create, modify, and access elements in Python lists.

# Topics Covered:
# Creating lists, indexing, slicing, appending, popping, sorting, reversing.

# Collections are used to store multiplie items in a single variable
# lists are ordered collections of items
# lists are mutable, meaning that you can change thier content 
# list are created using square Brackets []

my_list = [1, 2, 3, 4, 5]
print(my_list) #[1, 2, 3, 4, 5]
print (type(my_list)) #<class 'list>

# instead of  creating seperated variables
# for eacvh items, we can store them in a list
# this makes our job easier 
# when we need to manage multiplie items 
    # (Performance Task Answer)

# Accessing elements

print(my_list[0]) # 1
print(my_list[1:4]) # [2, 3, 4]
print(my_list[0:]) # [1, 2, 3, 4, 5]

# Modifying list
# Adding an item to the end of the list

my_list.append(6)
print(my_list) #[1, 2, 3, 4, 5, 6]

# You could do this but its time comsuming
my_list.append(7)
my_list.append(8)
my_list.append(9)
print(my_list) #[1, 2, 3, 4, 5, 6, 7, 8, 9]

# the Extend command makes it efficent but could be time consuming 
my_list.extend( [10,11,12,13,14,15] )
print(my_list) 

# add 500 more numbers to the list (the most efficent)
my_list.extend(list(range(15, 515)))
print(my_list)


# Examples:

# my_list = ['apple', 'banana', 'cherry']
# print(my_list[0])         # apple
# print(my_list[1:])        # ['banana', 'cherry']

# my_list.append('grape')
# print(my_list)

# my_list.pop(1)
# print(my_list)

# numbers = [3, 1, 4, 2]
# numbers.sort()
# print(numbers)


# Practice Problems:

# Create a list with 5 of your favorite foods.

# Print the second and last item.

# Add a new item using .append().

# Remove the first item using .pop(0).

# Reverse your list using .reverse().

# Create a list of 3 lists (matrix), and access the middle element.