'''
For the remaining students, add students name in a new list named students_approved

students = ["John", "Doe", "Jane", "Smith"]
grades = [85, 90, 78, 88]
activities = ["Football", "Music", "Art", "Dance"]
'''
# Only change from end of Task 2 should be creation of #students_approved variable with remaining students

students = ["John", "Doe", "Jane", "Smith"]
grades = [85, 90, 78, 88]
activities = ["Football", "Music", "Art", "Dance"]

profile1 = [students[0], grades[0], activities[0]]
profile2 = [students[1], grades[1], activities[1]]
profile4 = [students[3], grades[3], activities[3]]

students_approved = (profile1, profile2, profile4)
print(students_approved)