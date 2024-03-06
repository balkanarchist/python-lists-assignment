'''
Given the list: numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Use a list comprehension to create a new list containing numbers greater than 5.

'''
# modify list comprehension bit from last task to num>5 ?

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
new_numbers = [num for num in numbers if num > 5] #this should output all nums greater than 5
print(new_numbers)