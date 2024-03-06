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

profile1 = [students[0], grades[0], activities[0]]
profile2 = [students[1], grades[1], activities[1]]
profile3 = [students[2], grades[2], activities[2]] # the grade here is below 80
profile4 = [students[3], grades[3], activities[3]]

del profile3
remaining_students = (profile1, profile2, profile4)

print(remaining_students) #for verification

# I'm sure we're meant to write a code that would remove "profile3" automatically
# but based on information we've been given in the course so far, I don't know how
# to do that, except manually.