'''
For the remaining students, add students name in a new list named students_approved

students = ["John", "Doe", "Jane", "Smith"]
grades = [85, 90, 78, 88]
activities = ["Football", "Music", "Art", "Dance"]
'''
# Only change from end of Task 2 should be creation of #students_approved variable
# with remaining students

students = ["John", "Doe", "Jane", "Smith"]
grades = [85, 90, 78, 88]
activities = ["Football", "Music", "Art", "Dance"]

# Per directions, we only need the name and not the grades and activities this time

students.pop(2)
students_approved = students #Jane should now be removed
print(students_approved)