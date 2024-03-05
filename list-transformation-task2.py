#  Calculate the average grade and display it.
#  Add up the numbers then divide by number of items in list (10)

grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]
sum_of_grades = sum(grades) # used the sum function
print(sum_of_grades) # to verify that it added all the items
average_of_grades = float((sum_of_grades) / 10) # used float instead of int for precision
print(average_of_grades)