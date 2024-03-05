'''
You have a list of daily temperatures for a month, and you'd like to extract specific data from it.

Task 1: Given the list of temperatures:

temperatures = [72, 75, 78, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106]

Extract the temperatures for the second week (7 days) of the month.
'''

# should extract 83, 85, 86, 87, 88, 89, and 90 (positions 7-13)
# variable_name[start position:position after end of range desired]

temperatures = [72, 75, 78, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106]

second_week_temps = temperatures[7:14]
print(second_week_temps)