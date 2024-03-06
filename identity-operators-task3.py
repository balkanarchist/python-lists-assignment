'''
Using list methods, remove any student from the
attended list who did not submit their assignment.
'''

# Use .remove() for attended if not also in submitted

submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]

attended.remove("Eve")
attended.remove("Frank")
print(attended)

'''
I'm sure we're meant to write some code that detects if an item in attended is not
in submitted, but I'm not sure how and manually going through the lists and removing
provides the desired result, so...
'''