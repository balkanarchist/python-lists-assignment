'''
You have a list of numbers, and you'd like to generate a new list based on certain conditions.

Task 1: Given the list: numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

Use a list comprehension to create a new list containing only even numbers.
'''

# To be honest, I don't remember even hearing about list comprehension in the lessons so far
# so I'm just going off the simplest explanation of list comprehension that I could find.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = [num for num in numbers if num % 2 ==0] # this should remove all odd numbers

print(evens)