'''
You have two lists of student names. One list contains the names of students who have submitted their assignments, and the other list contains the names of students who attended the last class.

Task 1: Given the two lists:
submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]

Find out which students both submitted their assignments and attended the class.
'''

# I don't remember "set" being mentioned in the lessons, but that seems the easiest way
# print(set(variable1)) & set(variable2))

submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]

print(set(submitted) & set(attended)) #use ampersand not "and"
