'''
Filter out students who have grades below 80. Print the name, grade and activity.

students = ["John", "Doe", "Jane", "Smith"]
grades = [85, 90, 78, 88]
activities = ["Football", "Music", "Art", "Dance"]
'''

# The code below assumes that the positions for all variables relate to the same student.

students = ["John", "Doe", "Jane", "Smith"]
grades = [85, 90, 78, 88]
activities = ["Football", "Music", "Art", "Dance"]

profile: dict = {0: [students[0], grades[0], activities[0]], 1: [students[1], grades[1], activities[1]], 2: [students[2], grades[2], activities[2]], 3: [students[3], grades[3], activities[3]]}
print(profile) #for verification that variables were combined correctly
print() #for readability

# Add variable to print only Jane's profile
grade_under_80 = profile.pop(2)
print(grade_under_80)