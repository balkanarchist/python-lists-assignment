# Replace any grade below 80 with the value Failed.

# variable_name[location] = <name of replacement item>

grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]
grades[2] = "Failed"
grades[4] = "Failed"
grades[-2] = "Failed"

print(grades)