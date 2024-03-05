# Reverse the list and extract temperatures from the 5th to the 10th day of the reversed list.
# should output 102, 101, 100, 99, 98, and 97 (5, 6, 7, 8, 9 and 10 = 6 days)

temperatures = [72, 75, 78, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106]

temperatures.reverse()
print(temperatures) # for verification of reversal

print(temperatures[4:9]) # should show output excluding the 10th if the 10th day was meant to be excluded
print(temperatures[4:10]) # should show output including the 10th if the 10th day was meant to be included
