# sets & tuples ex:
set1 = {1, 2, 3, 4}
print(set1) # 1 2 3 4
print(type(set1)) # <class 'set'>
set1.add(6)
print(set1) # 1, 2, 3, 4, 6
set1.remove(2)
print(set1) # 1 3 4 5 6

set2 = { "apple" , "banana", "cherry", "cherry"}
print(set2)  # { "apple" , "banana", "cherry"}


# tuples example 
tuple1 = (1, 2, 3, 4, 5)
print(tuple1) # (1, 2, 3, 4, 5)
print(type(tuple1)) # <class 'tuple'>
# tuples are immuteable, meaning tehy cannot be changed after creation
# this amkes tuples useful for storing data that should not be changed 
Social_security_number = (123444, 4444445, 5676789)
print(Social_security_number) # (123444, 4444445, 5676789)